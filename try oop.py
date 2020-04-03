from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

@app.route("/name")
def name():
    return "Name"


if __name__ == "__main__":
    app.run(debag=True)