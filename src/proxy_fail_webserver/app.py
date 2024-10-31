import os
import random

from flask import Flask, render_template, render_template_string, request

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", random.randbytes(16))
USE_SSL = os.getenv("USE_SSL", "false").lower() == "true"
CONTENT_HTML_FILE = os.getenv("CONTENT_HTML_FILE")
if CONTENT_HTML_FILE and CONTENT_HTML_FILE.startswith('"'):
    CONTENT_HTML_FILE = CONTENT_HTML_FILE[1:-1]


def get_content():
    if CONTENT_HTML_FILE:
        with open(CONTENT_HTML_FILE, "r") as f:
            return render_template_string(f.read())
    return render_template("content.html")


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    to_req_url = request.url
    if USE_SSL:
        to_req_url = to_req_url.replace("http://", "https://")
    return render_template("index.html", url=to_req_url, content=get_content()), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
