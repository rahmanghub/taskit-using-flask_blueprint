from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.models import Tasks
from myproject.tasks.forms import AddForm,DelForm

tasks_blueprint = Blueprint('tasks',__name__,template_folder='templates/tasks')

@tasks_blueprint.route('/add',methods = ['GET','POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        task = form.task.data
        newTask = Tasks(task)
        db.session.add(newTask)
        db.session.commit()
        return redirect(url_for('tasks.list'))
    return render_template('add.html',form=form)

@tasks_blueprint.route('/list')
def list():
    tasks = Tasks.query.all()
    return render_template('list.html',tasks = tasks)

@tasks_blueprint.route('/del',methods = ['GET','POST'])
def delete():
    form = DelForm()
    if form.validate_on_submit():
        idFilter = form.id.data
        task = Tasks.query.filter_by(id=idFilter).first()
        if task:
            db.session.delete(task)
            db.session.commit()
            return redirect(url_for('tasks.list'))
        else:
            return redirect(url_for('tasks.list'))
    return render_template('delete.html',form=form)