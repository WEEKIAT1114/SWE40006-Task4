from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>SWE40006 Task 4.2</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f6f8;
                margin: 0;
                padding: 50px;
                text-align: center;
            }

            .card {
                max-width: 700px;
                margin: auto;
                background: white;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 4px 14px rgba(0,0,0,0.1);
            }

            h1 {
                margin-bottom: 10px;
            }

            .status {
                margin-top: 25px;
                padding: 12px;
                background: #eef5ee;
                border-radius: 8px;
            }
        </style>
    </head>

    <body>

        <div class="card">

            <h1>Hello World from Docker!</h1>

            <p>
                SWE40006 Software Deployment and Evolution
            </p>

            <p>
                Deployment Portfolio Task 4.2
            </p>

            <div class="status">
                Python Flask web server is running successfully.
            </div>

        </div>

    </body>
    </html>
    """


@app.route("/health")
def health():
    return {
        "service": "task4-hello-web",
        "status": "healthy"
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080
    )