from flask import Flask, render_template, request, flash, redirect, session

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Store feedback in session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html', name='John Doe', fact='I am a web developer')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('greet.html', name=name)
    return render_template('form.html')

# Feedback Route (Modified)
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if "feedback_list" not in session:
        session["feedback_list"] = []  

    if request.method == 'POST':
        feedback_text = request.form.get('feedback')
        if feedback_text:
            session["feedback_list"].append(feedback_text)  
            flash("Feedback submitted successfully!", "success")
            session.modified = True  
            return redirect('/feedback')

    return render_template('feedback.html', feedback_list=session["feedback_list"])

@app.route('/api/data')
def get_data():
    return jsonify({'name': 'John Doe', 'age': 30})

if __name__ == '__main__':
    app.run(debug=True)
