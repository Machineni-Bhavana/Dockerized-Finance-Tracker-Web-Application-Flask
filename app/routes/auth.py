from flask import Blueprint, render_template, request,redirect,url_for,flash
from flask_login import login_user, logout_user, login_required, current_user
from app import db, login_manager
from app.models import User
from sqlalchemy.exc import OperationalError

auth_bp = Blueprint('auth',__name__)


@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(int(user_id))
    except OperationalError:
        db.session.rollback()
        db.create_all()
        return None

@auth_bp.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            user = User.query.filter_by(username=username).first()
        except OperationalError:
            db.session.rollback()
            db.create_all()
            user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Login Successful' , 'success')
            return redirect(url_for('finance.dashboard'))
        flash('Invalid username or password','danger')
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out','info')
    return redirect(url_for('auth.login'))


@auth_bp.route('/register', methods=["GET","POST"])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        if not username or not email or not password:
            flash('Username, email and password are required', 'danger')
            return render_template('register.html')

        try:
            existing_username = User.query.filter_by(username=username).first()
            existing_email = User.query.filter_by(email=email).first()
        except OperationalError:
            db.session.rollback()
            db.create_all()
            existing_username = User.query.filter_by(username=username).first()
            existing_email = User.query.filter_by(email=email).first()

        if existing_username:
            flash('Username already taken', 'danger')
            return render_template('register.html')

        if existing_email:
            flash('Email already registered', 'danger')
            return render_template('register.html')

        user = User(username=username, email=email)
        user.set_password(password)
        try:
            db.session.add(user)
            db.session.commit()
        except OperationalError:
            db.session.rollback()
            db.create_all()
            db.session.add(user)
            db.session.commit()
        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html')

