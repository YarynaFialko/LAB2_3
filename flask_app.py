
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
import create_map
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("ask_id.html")


@app.route("/redirecting", methods=["POST"])
def redirecting():
    if request.method == "POST":
        dct = request.form
        user_name = dct["name"]
        create_map.main(user_name)
        return render_template("map.html")
      
