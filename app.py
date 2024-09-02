from flask import Flask, render_template, request

app = Flask(__name__)

COLORS = [
    "Red",
    "White",
    "Blue"
]

@app.route("/")
def index():
    return render_template("index.html", colors = COLORS)

@app.route("/flags")
def flags():
    if not request.form.get("colors"):
        return "failure"
    if request.form.get("color") not in COLORS:
        return "failure"
    return render_template("flags.html")