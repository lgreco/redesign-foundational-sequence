# Python containers -- list, dict, set, tuple -- are generic: they hold
# elements of any type without knowing in advance what those elements will be.
# A list can hold strings, integers, or custom objects, and the same list
# operations (append, index, len) work regardless. Node is a container in the
# same sense: it holds one piece of data and a pointer to the next node, and it
# should not care what kind of data that is. Python's typing module gives us a
# way to express this formally with TypeVar and Generic. A TypeVar named T
# stands for "whatever type the caller chooses." Declaring Node(Generic[T]) tells
# the type checker that Node[str] holds a string, Node[int] holds an integer,
# and Node[Student] holds a Student -- and that get_data() returns the same type
# that __init__ received. This is exactly how list[T] and dict[K, V] are typed
# in the standard library.

from __future__ import annotations
from typing import TypeVar, Generic

T = TypeVar('T')


class Node(Generic[T]):
    # T is fixed at construction time: Node[str] stores a string, Node[int]
    # stores an integer. The type checker propagates T through get_data()'s
    # return type so callers always know what they get back.

    def __init__(self, data: T):
        self._data: T = data
        # from __future__ import annotations makes this annotation legal here:
        # Node is not yet fully defined when Python reads this line, but because
        # annotations are treated as lazy strings, the forward reference resolves
        # correctly. Without that import, you would need '_next: Node | None'.
        self._next: Node | None = None

    def __str__(self) -> str:
        # Delegates to whatever __str__ the payload defines, so a Node holding
        # a Student prints the student, not the node wrapper.
        return str(self._data)

    def set_data(self, data: T) -> None:
        self._data = data

    def get_data(self) -> T:
        return self._data

    def set_next(self, next: Node) -> None:
        self._next = next

    def get_next(self) -> Node | None:
        return self._next

    def has_next(self) -> bool:
        return self._next is not None
