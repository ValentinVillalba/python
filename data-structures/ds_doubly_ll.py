#EN LAS LISTAS DOBLEMENTE ENLAZADAS CADA NODO APUNTA AL ANTERIOR Y AL SIGUIENTE
#LA VENTAJA SOBRE LAS LISTAS ENLAZADAS COMUNES ES QUE LAS DOBLEMENTE ENLAZADAS
#PUEDEN ITERAR EN AMBAS DIRECCIONES Y PUEDEN BORRAR UN NODO SIN NECESIDAD DE ITERAR.
#POR LO QUE SON MUCHO MAS RAPIDAS.

#PARA BORRAR UN NODO SE DEBE HACER QUE EL NODO PREVIO Y EL SIGUIENTE
#AL NODO QUE SE VA A BORRAR SE APUNTEN ENTRE SI
#DE ESTA MANERA DE IGNORA AL QUE SE QUERIA BORRAR Y QUEDA FUERA DE LA LISTA.

class Node:
	def __init__(self, d, n=None, p=None):
		self.data = d
		self.next_node = n
		self.prev_node = p

	def __str__(self):
		return ('('+str(self.data)+')')

class DoublyLinkedList:
	def __init__(self, r=None):
		self.root = r
		self.last = r
		self.size = 0

	def add(self, d):
		if self.size == 0:
			self.root = Node(d)
			self.last = self.root
		else:
			new_node = Node(d, self.root)
			self.root.prev_node = new_node
			self.root = new_node
		self.size += 1

	def find(self,d):
		this_node = self.root
		while this_node is not None:
			if this_node.data == d:
				return d
			elif this_node.next_node == None:
				return False
			else:
				this_node = this_node.next_node

	def remove(self, d):
		this_node = self.root
		while this_node is not None:
			if this_node.data == d:
				if this_node.prev_node is not None:
					if this_node.next_node is not None:
						this_node.prev_node.next_node = this_node.next_node
						this_node.next_node.prev_node = this_node.prev_node
					else:
						this_node.prev_node.next_node = None
						self.last = this_node.prev_node
				else:
					self.root = this_node.next_node
					this_node.next_node.prev_node = self.root
				self.size -= 1
				return True #SE BORRO EL DATO
			else:
				this_node = this_node.next_node
		return False #NO SE ENCONTRO EL DATO

	def print_list(self):
		if self.root is None:
			return
		this_node = self.root
		print(this_node, end='->')
		while this_node.next_node is not None:
			this_node = this_node.next_node
			print(this_node, end='->')
		print()

dll = DoublyLinkedList()
dll.add(9)
dll.add(17)
dll.add(3)
dll.print_list()

print("------------------------------")

print(dll.remove(20))
print(dll.remove(17))
dll.add(305)
dll.print_list()

print("------------------------------")

print(dll.find(5))
print(dll.find(305))
dll.add(79)
dll.print_list()

print("------------------------------")

dll.add(21)
dll.add(76)
dll.add(49)
dll.print_list()