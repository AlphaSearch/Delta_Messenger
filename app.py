from flask import *
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

app.run(port=55671)