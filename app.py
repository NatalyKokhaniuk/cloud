'''from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Привіт з на Render! Це Коханюк Наталя"

'''

'''
from flask import Flask, request, redirect, render_template

app = Flask(__name__)
items = []

@app.route("/")
def index():
    return render_template("index.html", items=items)

@app.route("/create", methods=["POST"])
def create():
    item = request.form["item"]
    if item:
        items.append(item)
    return redirect("/")

@app.route("/delete/<int:item_id>")
def delete(item_id):
    if 0 <= item_id < len(items):
        items.pop(item_id)
    return redirect("/")'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index2.html")
