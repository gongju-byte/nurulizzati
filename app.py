from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=["post", "get"])
def index():
    return render_template('index.html', status = "index")

@app.route('/about', methods=["post", "get"])
def about():
    return render_template('aboutme.html', status = "about")

@app.route('/project', methods=["post", "get"])
def projcet():
    return render_template('project.html', status = "project")


if __name__ == '__main__':
    app.run(debug=True)
