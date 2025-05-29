from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <html>
      <head>
        <style>
          body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: sans-serif;
            background-color: #f5f5f5;
          }
          h1 {
            color: #333;
          }
        </style>
      </head>
      <body>
        <h1>Привіт з Render! Це Коханюк Наталя</h1>
      </body>
    </html>
    """
