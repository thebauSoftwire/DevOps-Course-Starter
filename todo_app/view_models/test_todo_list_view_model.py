import pytest
from todo_app.view_models.todo_list_view_model import TodoListViewModel

test_items = [
    {'id': 1, 'name': 'some-name', 'status': 'To Do'},
    {'id': 2, 'name': 'some-name', 'status': 'Done'},
    {'id': 3, 'name': 'some-name', 'status': 'To Do'},
    {'id': 4, 'name': 'some-name', 'status': 'Done'},
]

def test_view_model_sets_items():
    items_view_model = TodoListViewModel(test_items)

    assert items_view_model.items == test_items

def test_view_model_returns_done_items():
    items_view_model = TodoListViewModel(test_items)

    assert len(items_view_model.done_items) == 2
    assert all([item['status'] == 'Done' for item in items_view_model.done_items])

def test_view_model_returns_to_do_items():
    items_view_model = TodoListViewModel(test_items)

    assert len(items_view_model.to_do_items) == 2
    assert all([item['status'] == 'To Do' for item in items_view_model.to_do_items])