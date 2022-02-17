from flask import Flask, render_template, url_for, abort
from api import *

app = Flask("Portfolio")

@app.route('/')
def index():
    courses = load("courses.json")
    projects = load("projects.json")
    techniques = get_techniques(projects)
    print(techniques)
    return render_template("index.html", courses=courses, projects=projects, techniques=techniques)

@app.route("/project/<int:id>")
def info(id):
    data = load("projects.json")
    project = get_project(data, id)      
    print(project)                        
    if project:
        return render_template("project.html", project = project)                                   
    else:     
        abort(404)                                                        
        

@app.errorhandler(404)
def page_not_found_404(e):
    return render_template("error.html")

#debug live with flask
if __name__ == "__main__":
    app.run(debug=True)