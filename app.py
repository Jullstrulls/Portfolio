from flask import Flask, render_template, url_for
from api import *

app = Flask("Portfolio")

@app.route('/')
def index():
    courses = load("courses.json")
    projects = load("projects.json")
    return render_template("index.html", courses=courses, projects=projects)

@app.route("/project/<int:id>")
def info(id):
    data = load("data.json")
    #info_project = get_project(data, id)                               #Use function from api to get project dict from id
    #if info_project == None:                                           #If there is no project that matches id, abort to errorhandler 404
     #   abort(404)
    #else:                                                             
     #   return render_template("info.html", data = info_project, id = id)


#debug live with flask
if __name__ == "__main__":
    app.run(debug=True)