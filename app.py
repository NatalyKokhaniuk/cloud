'''from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Привіт з на Render! Це Коханюк Наталя"

'''

'''
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
'''

from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL',
    'postgresql://database_fyzl_user:your_password@dpg-d0s8ukadbo4c73bfcicg-a/database_fyzl'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Item {self.id}: {self.content}>'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/3')
def quotas():
    return render_template('3.html')


@app.route('/4', methods=['GET'])
def show_items():
    items = Item.query.all()
    return render_template('4.html', items=items)

@app.route('/create', methods=['POST'])
def create_item():
    content = request.form.get('item')
    if content:
        new_item = Item(content=content)
        db.session.add(new_item)
        db.session.commit()
    return redirect('/4')

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect('/4')

if __name__ == '__main__':
    app.run(debug=True)

