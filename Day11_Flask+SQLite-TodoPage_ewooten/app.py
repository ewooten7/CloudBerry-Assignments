from flask import Flask, request, jsonify, redirect, render_template
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    sql = '''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
        '''
    cursor.execute(sql)
    conn.commit()
    conn.close()

init_db()

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = 'SELECT * FROM tasks'
    cursor.execute(sql)
    tasks = cursor.fetchall()
    tasks1 = []
    for task in tasks:
        print(dict(task))
        tasks1.append(task['title'])
    conn.close()
    return render_template('index.html',tasks = tasks1)

@app.route('/add', methods=['POST'])
def add_task():  
    task = request.form['task'] 
    conn = get_db_connection()
    cursor = conn.cursor()
    # sql = 'INSERT INTO tasks (title) VALUES (?)'
    cursor.execute('INSERT INTO tasks (title) VALUES (?)',(task,))
    print (task)
    print (cursor)
    conn.commit()
    conn.close()
    return redirect('/')


if __name__ == '__main__':
    app.run()