from dataclasses import dataclass
from typing import Any

class Stack():
	@dataclass
	class _Node:
		value: Any
		next:'_Node'
	
	__slots__=['_top']

	def __init__(self):
		self.top = None

	def push(self, item):
		self._top = Stack._Node(item, self._top)

	def pop(self):
		assert not self.is_empty(), 'LA PILA ESTA VACIA'
		value = self._top.value
		self._top = self._top.next
		return value

	def copy(self):
		new_stack = Stack()
		if not self.is_empty():
			node = self._top
			new_node = Stack._Node(node.value, None)
			new_stack._top = new_node
			while node.next is not None:
				node = node.next
				new_node.next = Stack._Node(node.value, None)
				new_node = new_node.next
		return new_stack

	def clear(self):
		self._top = None

	#OBSERVADORES:
	def is_empty(self):
        return self._top is None