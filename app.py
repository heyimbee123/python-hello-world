import os
from flask import Flask

# WSGI callable must be named 'application'
application = Flask(__name__)

@application.route("/")
def hello():
    return "Oscar en Alexander zijn de allerbeste"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    application.run(host="0.0.0.0", port=port)
