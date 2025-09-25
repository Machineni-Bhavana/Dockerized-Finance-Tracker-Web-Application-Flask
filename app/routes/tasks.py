from flask import Blueprint , render_template ,request , redirect , url_for ,flash
from flask_login import login_required, current_user
from app import db
from app.models import Task 

tasks_bp = Blueprint('tasks',__name__)

@tasks_bp.route('/')
@login_required
def view_tasks():
    q = Task.query
    if current_user.is_authenticated:
        q = q.filter(Task.user_id == current_user.id)
    tasks = q.order_by(Task.id.desc()).all()
    return render_template('tasks.html', tasks=tasks)

@tasks_bp.route('/add',methods=["POST"])
@login_required
def add_task():
    title = request.form.get('title')
    if title:
        new_task = Task(title=title,status= 'Pending', user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully','success')

    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/toggle/<int:task_id>',methods=["POST"])
@login_required
def toggle_status(task_id):
    task = Task.query.get(task_id)
    if task:
        if task.status == 'Pending':
            task.status = 'Working'
        elif task.status == 'Working':
            task.status = 'Done'
        else:
            task.status = 'Pending'
        db.session.commit()
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/clear' , methods =["POST"])
@login_required
def clear_task():
    Task.query.delete()
    db.session.commit()
    flash('All tasks cleared!','info')
    return redirect(url_for('tasks.view_tasks'))
