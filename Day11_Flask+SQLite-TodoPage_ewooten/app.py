from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__)

# Initialize the database and create tables if they don’t exist
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Function to establish database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # Allows fetching rows as dictionaries
    return conn

# Route: Home - Display all tasks
@app.route('/')
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

# Route: Add Task
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (title) VALUES (?)', (task,))
    conn.commit()
    conn.close()
    return redirect('/')

# Route: Delete Task (With Confirmation)
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect('/')

# NEW FEATURE: Edit Task
@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == 'POST':  # If form is submitted, update task
        new_title = request.form['title']
        cursor.execute('UPDATE tasks SET title = ? WHERE id = ?', (new_title, task_id))
        conn.commit()
        conn.close()
        return redirect('/')
    
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    task = cursor.fetchone()
    conn.close()
    return render_template('edit.html', task=task)  # Show edit form

if __name__ == '__main__':
    app.run(debug=True)
