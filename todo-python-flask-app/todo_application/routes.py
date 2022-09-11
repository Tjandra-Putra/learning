from flask import render_template, url_for, flash, redirect, request
from todo_application import app, db
from todo_application.models import Todos


# To run: python app.py

@app.route('/', methods=['POST', 'GET'])
def home():
    # retrieve all records
    db_records = Todos.query.all()

    return render_template("home.html", db_records=db_records)


@app.route('/create', methods=['POST', 'GET'])
def create_todos():
    form_desc = request.form['create_input']

    db_obj = Todos(description=form_desc)

    db.session.add(db_obj)
    db.session.commit()

    return redirect(url_for('home'))


@app.route('/edit/<todo_id>', methods=['GET', 'POST'])
def edit_todos(todo_id):
    if request.method == "POST":
        # get single row
        db_record = Todos.query.filter_by(id=todo_id).first()

        # update db
        db_record.description = request.form['edit_input']

        db.session.commit()

    return redirect(url_for('home'))


@app.route('/mark_todo/<todo_id>', methods=['GET', 'POST'])
def mark_todo(todo_id):
    if request.method == "POST":
        # get single row
        db_record = Todos.query.filter_by(id=todo_id).first()

        # update db
        db_record.completed = "yes"
        db.session.commit()

    return redirect(url_for('home'))


@app.route('/delete_todo/<todo_id>', methods=['GET', 'POST'])
def delete_todo(todo_id):
    if request.method == "POST":
        Todos.query.filter_by(id=todo_id).delete()

        db.session.commit()

    return redirect(url_for('home'))
