from dataclasses import dataclass
from typing import Any

class Stack():
    @dataclass
    class _Node:
        value: Any
        next: '_Node'

    __slots__=['_top']

    def __init__(self):
        self._top = None

    def push(self, value):
        self._top = Stack._Node(value, self._top)

    def pop(self):
        assert not self.is_empty(), 'LA PILA ESTA VACIA'
        value = self._top.value
        self._top = self._top.next
        return value

    #EL COPY ES RECURSIVO
    def copy(self):
        def do_copy(node):
            if node == None:
                return None
            else:
                new_node = Stack._Node(node.value, None)
                new_node.next = do_copy(node.next)
                return new_node

        new_stack = Stack()
        if not self.is_empty():
            new_node = Stack._Node(self._top.value, None)
            new_node.next = do_copy(self._top.next)
            new_stack._top = new_node
        return new_stack

    def clear(self):
        self._top = None

    #OBSERVADORES:
    def is_empty(self):
        return self._top is None
	    
    def __repr__(self):
        values = []
        node = self._top
        while node is not None:
            values.insert(0, node.value)
            node = node.next
        return 'Stack([' + ', '.join(repr(x) for x in values) + '])'
