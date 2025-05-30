from flask import Flask, render_template, request, redirect, send_from_directory
import os

app = Flask(__name__)

items = []

@app.route("/")
def index():
    return render_template("index.html", items=items)

@app.route("/create", methods=["POST"])
def create():
    item = request.form.get("item")
    if item:
        items.append(item)
    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(items):
        items.pop(index)
    return redirect("/")

@app.route("/3.html")
def page3():
    return render_template("3.html")

@app.route("/4")
def page4():
    items = Item.query.all()
    return render_template("4.html", items=items)

@app.route("/5.html")
def page5():
    return render_template("5.html")

if __name__ == "__main__":
    app.run(debug=True)
