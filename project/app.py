from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List to store tasks
tasks = []

@app.route('/')
def home():
  return render_template('home.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
  task = request.form['task']
  tasks.append(task)
  return redirect(url_for('home'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
  if task_id < 0 or task_id >= len(tasks):
    return redirect(url_for('home'))  # Handle invalid task ID
  tasks.pop(task_id)
  return redirect(url_for('home'))

if __name__ == '__main__':
  app.run(debug=True)