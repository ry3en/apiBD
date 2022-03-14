from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
#BD config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250))
    check = db.Column(db.Boolean)
    date = db.Column(db.DateTime, auto_now_add=True)

    def __init__(self, name, check):
        self.name = name
        self.check = check

    def __repr__(self):
        return '<Task %s>' % self.name

#db.create_all()

class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'check')

tasks_Schema = TaskSchema() #Una sola tarea
tasks_Schema = TaskSchema(many = True) #todas las tareas

upd_task = Task.query.get_or_404(3)
upd_task.name = "Debo Cambiarlo"
db.session.commit()

all_tasks = Task.query.all()
print(all_tasks)

if __name__ == '__main__':
    app.run(debug=True)
