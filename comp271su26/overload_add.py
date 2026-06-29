# Demonstrates Python's isinstance() as a lightweight dispatch mechanism.
# If the caller passes a plain string, add() wraps it in a Station automatically.
# If the caller already has a Station object, it passes through unchanged.

def add(self, new_item):
    if isinstance(new_item, str):
        new_item = Station(new_item)
    if self._head is None:
        self._head = new_item
    else:
        self._tail.set_next(new_item)
    self._tail = new_item
