from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql  # Ensure PyMySQL is used for MySQL connections

# 🟢 Initialize Flask App
app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for session-based authentication

# 🔹 Use RDS MySQL Instead of SQLite
DB_USERNAME = "admin"  # Replace with your actual RDS username
DB_PASSWORD = "password123"  # Replace with your actual RDS password
DB_ENDPOINT = "my-todoapp-flask-database.cb6yegc2ilb6.us-east-1.rds.amazonaws.com"
DB_NAME = "todoapp"
DB_PORT = 3306  # Default MySQL port

# 🔹 Configure Flask SQLAlchemy for MySQL
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_ENDPOINT}:{DB_PORT}/{DB_NAME}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# 🔹 Initialize SQLAlchemy
db = SQLAlchemy(app)

# 🟢 Task Model
class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Task {self.title}>'

# 🟢 Create Tables on First Request
# Ensure the database tables are created at the start of the application
with app.app_context():
    db.create_all()


# 🟢 Home Route - Show All Tasks
@app.route('/')
def home():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

# 🟢 Add Task Route
@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    new_task = Task(title=title)
    db.session.add(new_task)
    db.session.commit()
    return redirect('/')

# 🟢 Complete Task Route
@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = True
    db.session.commit()
    return redirect('/')

# 🟢 Delete Task Route
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Allows access from any IP