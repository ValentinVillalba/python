#UN ARBOL BINARIO SIRVE PARA ENCONTRAR UN ELEMENTO ESPECIFICO ENTRE MUCHOS (MILLONES A VECES)
#SIN LA NECESIDAD DE INTERAR POR CADA UNO DE ESOS ELEMENTOS (LO CUAL SERIA MUY LENTO).
#LO QUE HACE EL ARBOL BINARIO ES DIVIDIR LA BUSQUEDA EN VARIAS MITADES HASTA QUE ENCUENTRA
#EL ELEMENTO SOLICITADO, BUSCANDO SOLO UNAS POCAS VECES EN LUGAR DE MILLONES.

#EL ELEMENTO (NODO) QUE ESTA ARRIBA DE TODO ES LA RAIZ.
#NO TODOS LOS ARBOLES SON ARBOLES BINARIOS PERO EN ESTOS ULTIMOS
#CADA NODO PUEDE TENER HASTA 2 NODOS HIJOS.

#CADA NODO DEBE SER MAS GRANDE QUE TODOS LOS NODOS EN SU SUB-ARBOL IZQUIERDO.
#OPERACIONES: INSERT - FIND - DELETE - GET_SIZE - TRAVERSALS (RECORRE EL ARBOL NODO POR NODO)

#INSERT: SE ARRANCA A COMPARAR POR LA RAIZ Y SIEMPRE SE INSERTA EL NUEVO NODO ABAJO DE TODO.
#SI EL ELEMENTO A INGRESAR ES MAYOR QUE EL NODO CON EL QUE ESTA SIENDO COMPARADO
#SE BAJA POR EL LADO DERECHO.
#SI EL ELEMENTO A INGRESAR ES MENOR ENTONCES SE BAJA POR EL LADO IZQUIERDO.
#Y ASI SUCESIVAMENTE HASTA LLEGAR A LA BASE DEL ARBOL.

#FIND: FUNCIONA SIMILAR A INSERT Y EN CASO DE ENCONTRAR AL NUMERO RETORNAR TRUE O FALSE
#EN CASO CONTRARIO.

#DELETE: EL ELEMENTO A BORRAR PUEDE ESTAR ABAJO DE TODO, TENER 1 NODO HIJO O 2 NODOS HIJOS.
#PARA CADA CASO SE REALIZA UNA OPERACION DIFERENTE.
#EN EL PRIMER CASO SIMPLEMENTE SE BORRA EL NODO.
#SI TIENE 1 NODO HIJO SE DEBE MOVER AL HIJO HACIA LA POSICION DEL NODO QUE SE QUIERE BORRAR.
#SI TIENE 2 NODOS HIJOS SE DEBE ENCONTRAR AL SIGUIENTE NODO MAS GRANDE Y HACER QUE
#CAMBIE DE LUGAR CON EL NODO A BORRAR, PARA ESTO SE PUEDE BAJAR POR LA DERECHA
#DEL NODO A BORRAR Y LUEGO A LA IZQUIERDA DEL NODO QUE SIGUE.
#DE ESTA FORMA SE OBTIENE EL SIGUIENTE NODO MAS GRANDE.
#SOLO FALTA CAMBIARLOS DE POSICION.

#SIZE: EL TAMAÑO ES 1 MAS EL TAMAÑO DE LOS SUB-ARBOLES IZQUIERDO Y DERECHO.

#TRAVERSAL: HAY DIFERENTES FORMAS DE "TRAVERSAL".

#LOS ARBOLES DE BUSQUEDA BINARIA TIENEN UNA VELOCIDAD DE O(LOG N)

#LOS ARBOLES NO USAN LA CLASE NODO.

class Tree:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

	def insert(self, data):
		if self.data == data:
			return False #VALOR DUPLICADO
		elif self.data > data:
			if self.left is not None:
				return self.left.insert(data)
			else:
				self.left = Tree(data)
				return True
		else:
			if self.right is not None:
				return self.right.insert(data)
			else:
				self.right = Tree(data)
				return True

	def find(self, data):
		if self.data == data:
			return data
		elif self.data > data:
			if self.left is None:
				return False
			else:
				return self.left.find(data)
		elif self.data < data:
			if self.right is None:
				return False
			else:
				return self.right.find(data)

	def get_size(self):
		if self.left is not None and self.right is not None:
			return 1 + self.left.get_size() + self.right.get_size()
		elif self.left:
			return 1 + self.left.get_size()
		elif self.right:
			return 1 + self.right.get_size()
		else:
			return 1

	#TRAVERSALS:
	def preorder(self):
		if self is not None:
			#EN PREORDER EL PRINT VA ANTES DE LOS CONDICIONALES:
			print(self.data, end=' ')
			if self.left is not None:
				self.left.preorder()
			if self.right:
				self.right.preorder()

	def inorder(self):
		if self is not None:
			#EN INORDER EL PRINT VA ENTRE LOS CONDICIONALES:
			if self.left is not None:
				self.left.inorder()
			print(self.data, end=' ')
			if self.right is not None:
				self.right.inorder()

	#FALTA DELETE():

tree = Tree(3)
for i in [9,8,4,6,1,64,32,18,47,94,8]:
	tree.insert(i)
print(tree.find(64))
print(tree.find(594))
print("size=" , tree.get_size())

tree.preorder()
print()
tree.inorder()
print()