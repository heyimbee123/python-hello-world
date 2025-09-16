from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Oscar en Alexander zijn de allerbeste"
