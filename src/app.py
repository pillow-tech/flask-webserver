from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/up_check")
def up_check():
    return "OK"

@app.route("/test_endpoint")
def test_endpoint():
    msg = ""
    msg = msg + "<p>Hello, World!</p>"
    msg = msg + "<p>This is a new endpoint for simple flask webserver!</p>"
    return msg