from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL',
    'postgresql://database_fyzl_user:fT4Up7uMKWAgcjhJtbFNbyUIcaxAQMD8@dpg-d0s8ukadbo4c73bfcicg-a/database_fyzl'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Item {self.id}: {self.content}>'


local_items = []


@app.route('/')
def index():
    return render_template('index.html', items=local_items)

@app.route('/create', methods=['POST'])
def create_local_item():
    item = request.form.get("item")
    if item:
        local_items.append(item)
    return redirect('/')

@app.route('/delete/<int:index>')
def delete_local_item(index):
    if 0 <= index < len(local_items):
        local_items.pop(index)
    return redirect('/')

@app.route('/3')
def quotas():
    return render_template('3.html')

@app.route('/4')
def show_items():
    db_items = Item.query.all()
    return render_template('4.html', items=db_items)

@app.route('/db/create', methods=['POST'])
def create_db_item():
    content = request.form.get('item')
    if content:
        new_item = Item(content=content)
        db.session.add(new_item)
        db.session.commit()
    return redirect('/4')

@app.route('/db/delete/<int:item_id>')
def delete_db_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect('/4')

with app.app_context():
    db.create_all()
if __name__ == '__main__':
    app.run(debug=True)
