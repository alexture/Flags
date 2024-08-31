from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        return render_template("blue.html", name = name)
    return render_template("index.html") # else is implicit since i've returned something