from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.session_items import get_items, add_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    todoItems = get_items()
    return render_template('index.html', items=todoItems)

@app.route('/add-task', methods=["POST"])
def add_todo_item():
    title = request.form.get('todoItemTitle')
    add_item(title)
    return redirect(url_for('index'))
