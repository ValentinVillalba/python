#UNA LISTA ENLAZADA SE COMPONE DE NODOS, CADA UNO TIENE DOS PARTES
#EL DATO Y UN PUNTERO QUE SEÑALA AL SIGUIENTE NODO.
#CUANDO SE LLEGA AL FINAL NO HAY OTRO NODO ASI QUE SE GUARDA "NONE" EN EL PUNTERO.

#ATRIBUTOS: raiz(puntero que señala el inicio de la lista) - tamaño
#OPERACIONES: find(data) - add(data) - remove(data) - print_list()

#ESTE NODO SIRVE PARA TODAS LAS LISTAS:
class Node:
	def __init__(self, d, n=None, p=None):
		self.data = d
		self.next_node = n
		self.prev_node = p

	def __str__(self):
		return ('('+str(self.data)+')')

class LinkedList:
	def __init__(self, r=None):
		self.root = r
		self.size = 0

	def add(self, d):
		new_node = Node(d, self.root)
		self.root = new_node
		self.size += 1

	def find(self, d):
		this_node = self.root
		while this_node is not None:
			if this_node.data == d:
				return d
			else:
				this_node = this_node.next_node
		return None

	def remove(self, d):
		this_node = self.root
		prev_node = None
		while this_node is not None:
			if this_node.data == d:
				if prev_node is not None: #EL DATO NO ESTA EN LA RAIZ
					prev_node.next_node = this_node.next_node #SALTA AL NODO SIGUIENTE
				else: #EL DATO ESTA EN LA RAIZ
					self.root = this_node.next_node
				self.size -= 1
				return True #SE BORRA EL DATO
			else:
				prev_node = this_node
				this_node = this_node.next_node
		return False #NO SE ENCONTRO EL DATO

	def print_list(self):
		this_node = self.root
		while this_node is not None:
			print(this_node, end='->')
			this_node = this_node.next_node
		print('None')

lista = LinkedList()
lista.add(5)
lista.add(8)
lista.add(12)
lista.print_list()

print("size="+str(lista.size))
lista.remove(8)
print("size="+str(lista.size))
print(lista.find(5))
print(lista.root)