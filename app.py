from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Oscar en Alexander zijn de allerbeste"

if __name__ == "__main__":
    # Elastic Beanstalk sets PORT automatically
    port = int(os.environ.get("PORT", 8080))
    application.run(host="0.0.0.0", port=port)
