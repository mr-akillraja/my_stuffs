from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append({"task": task, "completed": False})
    return render_template('index.html', tasks=tasks)

@app.route('/mark_task_completed', methods=['POST'])
def mark_task_completed():
    task_index = int(request.form['completed_task']) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
    return redirect(url_for('index'))

@app.route('/remove_task', methods=['POST'])
def remove_task():
    task_index = int(request.form['removed_task']) - 1
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
