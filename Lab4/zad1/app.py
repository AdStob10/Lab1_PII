from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/users')
def users():
    users = {
        1: {"name": "Ala", "age": 22},
        2: {"name": "Bartek", "age": 25},
        3: {"name": "Celina", "age": 30}
    }
    return render_template("users.html", users= users)

@app.route('/user/<name>')
def user(name):
    founded_user = None
    users = {
        1: {"name": "Ala", "age": 22},
        2: {"name": "Bartek", "age": 25},
        3: {"name": "Celina", "age": 30}
    }
    for x in users:
        print(x)
        if users[x]["name"] == name:
            founded_user = users[x]
    return render_template("user.html", user=founded_user)


if __name__ == '__main__':
    app.run(debug=True)