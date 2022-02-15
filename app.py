from flask import Flask, render_template
from api import *

app = Flask("Portfolio")

@app.route('/')
def index():
    courses = load("courses.json")
    print(courses)
    return render_template("index.html", courses=courses)

#debug live with flask
if __name__ == "__main__":
    app.run(debug=True)