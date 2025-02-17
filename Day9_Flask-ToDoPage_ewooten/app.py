from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "secret"

# Sample data structure: each task is a dictionary with 'task', 'completed', and 'due_date'
tasks = []

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    due_date = request.form.get('due_date')

    if task:
        tasks.append({"task": task, "completed": False, "due_date": due_date})  # Store task with completion status
        flash('Task added successfully', 'success')

    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        flash('Task deleted successfully', 'danger')

    return redirect('/')

@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = not tasks[task_id]['completed']  # Toggle completion status
        flash('Task status updated!', 'info')

    return redirect('/')

@app.route('/clear_all')
def clear_all():
    tasks.clear()
    flash('All tasks cleared!', 'warning')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
