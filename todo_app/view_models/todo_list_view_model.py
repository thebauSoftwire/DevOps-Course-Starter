class TodoListViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items
    
    @property
    def done_items(self):
        print(self.items)
        complete_items = filter(lambda item: item.status == 'Done', self.items)
        return list(complete_items)
    
    @property
    def to_do_items(self):
        to_do_items = filter(lambda item: item.status == 'To Do', self.items)
        return list(to_do_items)
