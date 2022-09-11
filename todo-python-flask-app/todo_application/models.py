from todo_application import db, app


class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.String(10), default="no", nullable=False)
