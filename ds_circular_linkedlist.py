#LAS LISTAS CIRCULARES FUNCIONAN IGUAL QUE LAS LINKED LIST
#PERO EN LAS CIRCULARES EN LUGAR DE QUE EL ULTIMO NODO APUNTE A NONE
#ESTA VEZ APUNTA DE NUEVO A LA RAIZ (ROOT).

#UN NUEVO OBJETO SE DEBE INSERTAR EN LA SEGUNDA POSICION PARA NO ROMPER EL BUCLE.
#SON IDEALES PARA MODELAR BUCLES CONTINUOS DE OBJETOS (UNA PISTA DE CARRERAS POR EJEMPLO).

class Node:
	def __init__(self, d, n=None, p=None):
		self.data = d
		self.next_node = n
		self.prev_node = p

	def __str__(self):
		return ('('+str(self.data)+')')

class CircularLinkedList:
	def __init__(self, r = None):
		self.root = r
		self.size = 0

	def add(self, d):
		if self.size == 0:
			self.root = Node(d)
			self.root.next_node = self.root
		else:
			new_node = Node(d, self.root.next_node)
			self.root.next_node = new_node
		self.size += 1

	def find(self, d):
		this_node = self.root
		while  True:
			if this_node.data == d:
				return d
			elif this_node.next_node == self.root:
				return False
			this_node = this_node.next_node

	def remove(self, d):
		this_node = self.root
		prev_node = None

		while True:
			if this_node.data == d: #SE ENCONTRO
				if prev_node is not None:
					prev_node.next_node = this_node.next_node
				else:
					while this_node.next_node != self.root:
						this_node = this_node.next_node
					this_node.next_node = self.root.next_node
					self.root = self.root.next_node
				self.size -= 1
				return True #SE BORRO
			elif this_node.next_node == self.root:
				return False #NO SE ENCONTRO
			prev_node = this_node
			this_node = this_node.next_node

	def print_list(self):
		if self.root is None:
			return
		this_node = self.root
		print(this_node, end='->')
		while this_node.next_node != self.root:
			this_node = this_node.next_node
			print(this_node, end='->')
		print()

cll = CircularLinkedList()
for i in [5,7,3,8,9]:
	cll.add(i)

print("size= "+str(cll.size))
print(cll.find(8))
print(cll.find(12))

my_node = cll.root
print(my_node, end='->')

for i in range(16): #LA LISTA SE PUEDE REPETIR LAS VECES QUE SE NECESITE.
	my_node = my_node.next_node
	print(my_node, end='->')
print()

print("-------------------------")

cll.print_list()
cll.remove(8)
print(cll.remove(27))
print("size= "+str(cll.size))
cll.remove(5) #BORRA EL ROOT
cll.print_list()
print("size= "+str(cll.size))