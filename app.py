from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>CI/CD Flask App</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light text-center p-5">
        <div class="container">
            <h1 class="display-4 text-primary">🚀 CI/CD Flask App</h1>
            <p class="lead">Welcome! This Flask app is running inside a Docker container,<br>built & deployed using GitHub Actions on Kubernetes Cluster.</p>
            <hr>
            <p class="text-muted">This is my <b>Final Project</b> on DevOps Internship in ELEVATE LABS</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
