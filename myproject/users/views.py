from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.models import Users
from myproject.users.forms import UserForm

users_blueprint = Blueprint('users',__name__,template_folder='templates/users')

@users_blueprint.route('/add',methods = ['GET','POST'])
def user():
    form = UserForm()
    if form.validate_on_submit():
        name = form.name.data
        taskId = form.taskId.data
        new_user = Users(name,taskId)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('tasks.list'))
    return render_template('user.html',form=form)