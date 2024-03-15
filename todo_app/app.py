from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.trello_items import get_items, add_item, complete_item
from todo_app.view_models.view_model import ViewModel

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    todoItems = get_items()
    item_view_model = ViewModel(todoItems)
    return render_template('index.html', view_model=item_view_model)

@app.route('/add-task', methods=["POST"])
def add_todo_item():
    title = request.form.get('todoItemTitle')
    add_item(title)
    return redirect(url_for('index'))

@app.route('/complete-item/<item_id>', methods=["POST"])
def complete_todo_item(item_id):
    complete_item(item_id)
    return redirect(url_for('index'))