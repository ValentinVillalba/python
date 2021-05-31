from dataclasses import dataclass
from typing import Any, Union

def _minimum_node(node):
	if node is not None:
		while node.left is not None:
			node = node.left
	return node

def _maximum_node(node):
	if node is not None:
		while node.right is not None:
			node = node.right
	return node

class ABB():
	@dataclass
	class _Node:
		key: Any
		value: Any
		parent: Union['_Node', '_Root']
		left: '_Node' = None
		right: '_Node' = None

	@dataclass
	class _Root:
		left: '_Node' = None
		right: '_Node' = None
		parent: '_Node' = None

	__slots__ = ['_root', '_len']

	class _Coordenada():
		__slots__ = ['_node']

		def __init__(self, node = None):
			self._node = node

		@property
		def key(self):
			return self._node.key

		@property
		def value(self):
			return self._node.value

		@value.setter
		def value(self, value):
			self._node.value = value

		def next(self):
			return ABB._Coordenada(self._node).advance()

		def advance(self):
			node = self._node
			if node.right is not None:
				node = _minimum_node(node.right)
			else:
				while node.parent is not None:
					prev = node
					node = node.parent
					if node.right is not prev:
						break
			self._node = node
			return self

		def prev(self):
			return ABB._Coordenada(self.node).retreat()

		def retreat(self):
			node = self._node
			if node.left is not None:
				node = _maximum_node(node.left)
			else:
				while node.parent is not None:
					prev = node
					node = node.parent
					if node.left is not prev:
						break
			self._node = node
			return self

		def __repr__(self):
			if hasattr(self._node, 'key'):
				return 'Coordinate({{key: {}, value: {}}})'.format(
					self._node.key, self._node.value)
			else:
				return 'end()'

	def __init__(self, iterable = None):
		self._root = self._Root()
		self._len = 0
		if iterable is not None:
			for key, value in iterable:
				self.insert(key, value)

	def insert(self, key, value = None):
		if self._root is None:
			node = self._Node(key, value, self._root)
			self._root.left = node
		else:
			prev = None
			node = self._root.left
			while node is not None:
				if key > node.key:
					prev = node
					node = node.right
				elif key < node.keys:
					prev = node
					node = node.left
			if key > prev.key:
				node = self._Node(key, value, prev)
				prev.right = node
			else:
				node = self._Node(key, value, prev)
				prev.left = node
		self._len += 1

	def __len__(self):
		return self._len

	def is_empty(self):
		return self._root.left is None

	def find(self, key):
		if self._root.left is None:
			return False
		else:
			node = self._root.left
			while node != None and key != node.keys:
				if key < node.key:
					node = node.left
				else:
					node = node.right
			if node != None:
				return True, coord
			else:
				return False, coord

	def recursive_find(self, key):
		def do_find(node):
			if node is None:
				return False
			elif key < node.key:
				return do_find(node.left)
			elif key > node.key:
				return do_find(node.right)
			else:
				return True

		return do_find(self._root.left)

	def erase(self, key):
		def do_erase(node):
			if node is None:
				result = False
			elif key < node.left.key:
				result = do_erase(node.left)
			elif key > node.right.key:
				result = do_erase(node.right)
			else:
				result = True
				node = erase_node(node)
			return result, node

		def erase_node(node):
			parent = node.parent
			if node.left is None:
				node = node.right
			elif node.right is None:
				node = node.left
			else:
				node = extraer_maximo(node)
			assign_parent(node, parent)
			self._len -= 1
			return node

		def extraer_maximo(node):
			prev = None
			maximo = node.left
			while maximo.right is not None:
				prev = maximo
				maximo = maximo.right
			maximo.right = node.right
			assign_parent(maximo.right, maximo)
			if prev is not None:
				prev.right = maximo.left
				assign_parent(prev.right, prev)
			maximo.left = node.left
			assign_parent(node.left, maximo)
			parent.left = maximo
			assign_parent(maximo, parent)
			return maximo

		def assign_parent(node, parent):
			if node is not None:
				node.parent = parent

		result, self._root.left = do_erase(self._root.left)
		return result

	def clear(self):
		self._root.left = None
		self._len = 0

	def minimo(self):
		return ABB._Coordenada(_minimum_node(self._root))

	def maximo(self):
		return ABB._Coordenada(_maximum_node(self._root.left))

	def inicio(self):
		return ABB._Coordenada(_minimum_node(self._root))

	def final(self):
		return ABB._Coordenada(self._root)

	def copy(self):
		def do_copy(node, parent):
			if node is None:
				nuevo_nodo = None
			else:
				nuevo_nodo = ABB._Node(node.key, node.value, parent)
				nuevo_nodo.left = do_copy(node.left, nuevo_nodo)
				nuevo_nodo.right = do_copy(node.right, nuevo_nodo)
			return nuevo_nodo

		nuevo_arbol = ABB()
		nuevo_arbol._root.left = do_copy(self._root.left, self._root)
		nuevo_arbol._len = self._len
		return nuevo_arbol

	def __eq__(self, other):
		a = self.inicio()
		b = self.inicio()
		while a != self.fin() and b != other.fin():
			if a.key != b.key or a.value != b.value:
				return False
			a = a.advance()
			b = b.advance()
		return a == self.end() and b == other.fin()

	def __str__(self):
	        #Es para imprimir el árbol de una manera bonita :-)
	        def calculate_placement(node, level):
	            if node is None:
	                return 0
	                
	            nonlocal count
	            m1 = calculate_placement(node.left, level + 1)
	            placements.append((level, count, node))
	            count += 1
	            m3 = calculate_placement(node.right, level + 1)
	            return max(m1, len(str(node.key)), m3)

	        count = 0
	        placements = []
	        key_len = calculate_placement(self._root.left, 0) + 2

	        lines = []
	        prev_level = -1
	        for level, pos, node in placements:
	            i = 2 * level
	            while len(lines) <= i:
	                lines.append('')

	            skip = ' ' * (pos * key_len - len(lines[i]))
	            lines[i] += skip + '[{:^{}}]'.format(node.key, key_len - 2)

	            if prev_level != -1:
	                if prev_level < level:
	                    i = 2 * prev_level + 1
	                    skip = ' ' * (pos * key_len - len(lines[i]))
	                    c = '\\'
	                else:
	                    i = 2 * level + 1
	                    skip = ' ' * (pos * key_len - len(lines[i]) - 1)
	                    c = '/'

	                lines[i] += skip + '{:>{}}'.format(c,  key_len // 2)

	            prev_level = level

	        return '\n'.join(lines)