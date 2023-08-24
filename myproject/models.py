from myproject import db

class Tasks(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer,primary_key=True)
    task = db.Column(db.Text)
    user = db.relationship('Users', backref='tasks', uselist=False)

    def __init__(self,task):
        self.task=task

    def __repr__(self):
        # return f"{self.user.name}"
        if self.user:
            return f"Id: {self.id}, Task: {self.task}, Assigned To: {self.user.name}"
        else:
            return f"Id: {self.id}, Task: {self.task}, Assigned To: Not assigned Yet"

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))


    def __init__(self,name,task_id):
        self.name=name
        self.task_id = task_id

    def __repr__(self):
        return f"User : {self.name}, Task: {self.task_id}"