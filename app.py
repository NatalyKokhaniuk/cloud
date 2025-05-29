'''from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Привіт з на Render! Це Коханюк Наталя"

'''

from flask import Flask, render_template, request, redirect, send_from_directory
import os

app = Flask(__name__)

# Простий список для зберігання елементів (у реальних додатках — база даних)
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
    # Припускаємо, що 3.html лежить у папці templates
    return render_template("3.html")

# Якщо 3.html у static, використай це замість render_template:
# @app.route("/3.html")
# def page3():
#     return send_from_directory('static', '3.html')

if __name__ == "__main__":
    app.run(debug=True)
