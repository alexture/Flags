from flask import Flask, render_template, request

app = Flask(__name__)

COLORS = [
    "Red",
    "White",
    "Blue"
]

@app.route("/")
def index():
    return render_template("index.html")#, colors=COLORS)