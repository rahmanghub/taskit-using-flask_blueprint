from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class UserForm(FlaskForm):
    name = StringField('Name: ')
    taskId = IntegerField('Task ID: ')
    submit = SubmitField('Assign User')
