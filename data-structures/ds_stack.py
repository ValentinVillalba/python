#LAS PILAS SON UNA ESTRUCTURA LIFO:
#EL ULTIMO ELEMENTO EN ENTRAR SERA EL PRIMERO EN SALIR.

#EJEMPLO DE USO: CUANDO USAMOS CTRL+Z EN UN PROGRAMA HACEMOS POP
#EN LA PILA DE COMANDOS UTILIZADOS PREVIAMENTE
#VOLVIENDO AL PUNTO EN EL QUE ESE COMANDO NO SE HABIA INGRESADO.

class Stack():
	def __init__(self):
		self.stack = list()
	def push(self, item):
		self.stack.append(item)
	def pop(self):
		if len(self.stack) > 0:
			return self.stack.pop()
		else:
			return None
	def peek(self):
		if len(self.stack) > 0:
			return self.stack[len(self.stack)-1]
		else:
			return None
	#__str__ SE USA PARA QUE AL IMPRIMIR SE MUESTRE ALGO LEGIBLE
	#EN LUGAR DE LA DIRECCION DE MEMORIA DONDE SE ENCUENTRA LA PILA.
	def __str__(self):
		return str(self.stack)

pila = Stack()
pila.push(5)
pila.push(6)
pila.pop()
pila.push(7)
#PILA COMPLETA:
print(pila)

#MUESTRA EL NUMERO QUE ESTA ARRIBA DE TODO EN LA PILA:
print(pila.peek())

pila.pop()
pila.pop()

#PILA VACIA:
print(pila)