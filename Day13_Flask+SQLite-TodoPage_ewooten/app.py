from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for session-based authentication

# 🟢 Configure SQLite Database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
@app.before_first_request
def create_tables():
    db.create_all()

# 🟢 Home Route - Show All Tasks
@app.route('/')
def home():
    filter_option = request.args.get('filter', 'all')  # Get filter option from URL parameter
    if filter_option == 'uncompleted':
        tasks = Task.query.filter_by(completed=False).all()
    else:
        tasks = Task.query.all()
    return render_template('index.html', tasks=tasks, filter_option=filter_option)

# 🟢 Add Task Route
@app.route('/add', methods=['POST'])
def add_task():
    if 'user' not in session:  # Ensure user is logged in
        return redirect('/login')
    
    title = request.form['title']
    new_task = Task(title=title)
    db.session.add(new_task)
    db.session.commit()
    return redirect('/')

# 🟢 Complete Task Route
@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    if 'user' not in session:  # Ensure user is logged in
        return redirect('/login')
    
    task = Task.query.get_or_404(task_id)
    task.completed = True
    db.session.commit()
    return redirect('/')

# 🟢 Delete Task Route
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 'user' not in session:  # Ensure user is logged in
        return redirect('/login')
    
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/')

# 🟢 NEW FEATURE: User Authentication (Login & Logout)
users = {"admin": "password123"}  # Simple hardcoded user credentials

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['user'] = username  # Store user session
            return redirect('/')
        else:
            return "Invalid credentials. Try again."

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)  # Remove user session
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
