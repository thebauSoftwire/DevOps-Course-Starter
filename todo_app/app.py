from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.trello_items import get_items, add_item, complete_item
from todo_app.view_models.todo_list_view_model import TodoListViewModel

from todo_app.flask_config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/')
    def index():
        todoItems = get_items()
        app.logger.info(todoItems)
        items_view_model = TodoListViewModel(todoItems)
        return render_template('index.html', view_model=items_view_model)

    @app.route('/add-task', methods=["POST"])
    def add_todo_item():
        title = request.form.get('todoItemTitle')
        add_item(title)
        return redirect(url_for('index'))

    @app.route('/complete-item/<item_id>', methods=["POST"])
    def complete_todo_item(item_id):
        complete_item(item_id)
        return redirect(url_for('index'))
    
    return app