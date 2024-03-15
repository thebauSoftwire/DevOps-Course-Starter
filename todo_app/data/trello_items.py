import os
import requests
from todo_app.data.item import Item

def add_item(title):
    """
    Adds a new item with the specified title to the To Do list.

    Args:
        title: The title of the item.

    """
    url = f"{os.getenv('TRELLO_API_BASE_URL')}/cards"

    request_params = {
        'idList': os.getenv("TRELLO_TODO_LIST_ID"),
        'key': os.getenv("TRELLO_API_KEY"),
        'token': os.getenv("TRELLO_API_TOKEN"),
        'name': title
    }

    requests.request(
        "POST",
        url=url,
        params=request_params
    )

def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    url = f"{os.getenv('TRELLO_API_BASE_URL')}/boards/{os.getenv('TRELLO_BOARD_ID')}/lists"

    request_params = {
        'key': os.getenv("TRELLO_API_KEY"),
        'token': os.getenv("TRELLO_API_TOKEN"),
        'cards': 'open',
        'card_fields': ['id', 'name']
    }

    response = requests.request(
        "GET",
        url=url,
        params=request_params
    )

    response_json = response.json()
    cards = []
    for trello_list in response_json:
        for card in trello_list['cards']:
            cards.append(Item.from_trello_card(card, trello_list))

    return cards

def  complete_item(item_id):
    """
    Marks an item with the associated ID as "Done".
    """
    url = f"https://api.trello.com/1/cards/{item_id}"

    request_params = {
        'key': os.getenv("TRELLO_API_KEY"),
        'token': os.getenv("TRELLO_API_TOKEN"),
        'idList': os.getenv("TRELLO_DONE_LIST_ID")
    }

    requests.request(
        "PUT",
        url=url,
        params=request_params
    )
    