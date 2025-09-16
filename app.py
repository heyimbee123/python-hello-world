import os
from flask import Flask

# Use 'app' for Azure, 'application' for EB
app = Flask(__name__)
application = app  # Elastic Beanstalk expects 'application'

@app.route("/")
def hello():
    return "Oscar en Alexander zijn de allerbeste"

if __name__ == "__main__":
    # Use PORT from environment (EB sets it, Azure sets it too)
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
