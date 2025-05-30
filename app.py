from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=["post", "get"])
def index():
    return render_template('index.html', status = "index")

@app.route('/about', methods=["post", "get"])
def about():
    return render_template('aboutme.html', status = "about")

@app.route('/project', methods=["post", "get"])
def project():
    return render_template('project.html', status = "project")

@app.route('/article', methods=["post", "get"])
def article():
    return render_template('article.html', status = "article")

@app.route('/service', methods=["post", "get"])
def service():
    return render_template('service.html', status = "service")


if __name__ == '__main__':
    app.run(debug=True)
