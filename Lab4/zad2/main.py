from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)


class Task():
    def __init__(self, name, description, done):
        self.name = name
        self.description = description
        self.done = done


task_list = {}


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/tasks', methods=['GET'])
def tasks():
    return render_template("tasks.html", tasks=task_list)


@app.route('/tasks', methods=['POST'])
def add():
    name = request.form['name']
    description = request.form['description']
    if len(name) > 0 and len(description) > 0:
        task_list[len(task_list)] = Task(name, description, False)
    return redirect(url_for("tasks"))


@app.route('/tasks/<int:task_id>/done', methods=['GET'])
def done(task_id):
    task = task_list[task_id]
    task.done = True
    return redirect(url_for("tasks"))


@app.route('/tasks/<int:task_id>/delete', methods=['GET'])
def delete(task_id):
    del task_list[task_id]
    return redirect(url_for("tasks"))

@app.route('/api/tasks', methods=['GET'])
def api_task():
    return jsonify(task_list)


if __name__ == '__main__':
    app.run(debug=True)
