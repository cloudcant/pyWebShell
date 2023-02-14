import subprocess
import flask
from flask import request, jsonify

host = "0.0.0.0"
port = 80

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET"])
def home():
    with open("index.html", "r") as f:
        html = f.read()
    return html


@app.route("/api", methods=["GET"])
def api_api():
    if "command" in request.args:
        outputraw = subprocess.Popen(
            request.args["command"], shell=True, stdout=subprocess.PIPE
        ).stdout
        output = outputraw.read()
        return output.decode()
    else:
        return "404"


app.run(host=host, port=port)
