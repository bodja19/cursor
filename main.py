from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello"

@app.route("/name")
def name():
    return "Name"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "POST"
    else:
        return "GET"

if __name__ == "__main__":
    app.run(debug=True)
