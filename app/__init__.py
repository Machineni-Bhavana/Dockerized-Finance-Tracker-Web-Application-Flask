from flask import Flask, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

#create database object globally

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'your-secret-key'
    # Ensure a single consistent DB file under instance folder
    os.makedirs(app.instance_path, exist_ok=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.__init__(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from app.models import Transaction, User

    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp
    from app.routes.finance import finance_bp
    app.register_blueprint(auth_bp,url_prefix = "/auth")
    app.register_blueprint(tasks_bp,url_prefix="/tasks")
    app.register_blueprint(finance_bp,url_prefix="/finance")

    @app.template_filter('inr')
    def inr_currency(value):
        try:
            num = float(value)
        except Exception:
            return value
        # Format with Indian number system grouping
        s = f"{num:,.2f}"
        # Convert to Indian grouping (e.g., 12,34,567.89)
        parts = s.split('.')
        whole = parts[0].replace(',', '')
        if len(whole) > 3:
            head = whole[:-3]
            tail = whole[-3:]
            groups = []
            while len(head) > 2:
                groups.insert(0, head[-2:])
                head = head[:-2]
            if head:
                groups.insert(0, head)
            whole = ','.join(groups) + ',' + tail
        else:
            # keep as is (<= 3 digits)
            pass
        return f"₹{whole}.{parts[1]}"

    @app.route('/')
    def index():
        return redirect(url_for('finance.dashboard'))

    # Ensure tables exist when the app is created (Flask 3.x compatible)
    with app.app_context():
        from app.models import User, Task, Transaction
        try:
            db.create_all()
        except Exception:
            pass
        # Seed a default admin user if none exists (robust against fresh DBs)
        try:
            if not User.query.filter_by(username='admin').first():
                u = User(username='admin', email='admin@example.com')
                from werkzeug.security import generate_password_hash
                u.password_hash = generate_password_hash('admin123')
                db.session.add(u)
                db.session.commit()
        except Exception:
            db.session.rollback()
            db.create_all()
            if not User.query.filter_by(username='admin').first():
                u = User(username='admin', email='admin@example.com')
                from werkzeug.security import generate_password_hash
                u.password_hash = generate_password_hash('admin123')
                db.session.add(u)
                db.session.commit()

    return app

