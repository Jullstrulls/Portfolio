from flask import Flask, render_template

app = Flask("Portfolio")

@app.route('/')
def index():
    return render_template("index.html")

#debug live with flask
if __name__ == "__main__":
    app.run(debug=True)