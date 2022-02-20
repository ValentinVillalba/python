#EL MAX HEAP ES MUY RAPIDO (DEMOSTRADO EN NOTACION O)
#LOS ELEMENTOS SE ALINEAN EN FILAS Y "COLUMNAS"
#LA REGLA ES QUE LOS ELEMENTOS MAS GRANDES ESTEN ARRIBA
#Y LOS MAS CHICOS ABAJO.
#LA REGLA PARA ESTO ES QUE SI EL MAS GRANDE ES 25
#EN LA FILA DE ABAJO TODOS LOS NUMEROS DEBEN SER MENORES
#ESTO SE APLICA IGUAL PARA LAS FILAS QUE ESTEN DEBAJO DE ESTA.

#i = 4 este es el indice
#parent(i) = i//2
#left_parent(i) = i*2
#right_parent(i) = i*2 +1

class MaxHeap():
	def __init__(self, items=[]):
		super().__init__()
		self.heap = [0]
		for item in items:
			self.heap.append(item)
			self.__floatUp(len(self.heap) - 1)
	def push(self, data):
		self.heap.append(data)
		self.__floatUp(len(self.heap) - 1)
	def peek(self):
		if self.heap[1]:
			return self.heap[1]
		else:
			return False
	def pop(self):
		if len(self.heap) > 2:
			self.__swap(1, len(self.heap) - 1)
			max = self.heap.pop()
			self.__bubbleDown(1)
		elif len(self.heap) == 2:
			max = self.heap.pop()
		else:
			max = False
		return max
	def __swap(self, i, j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
	def __floatUp(self, index):
		parent = index//2
		if index <= 1:
			return
		elif self.heap[index] > self.heap[parent]:
			self.__swap(index, parent)
			self.__floatUp(parent)
	def __bubbleDown(self, index):
		left = index * 2
		right = index * 2 + 1
		largest = index
		if len(self.heap) > left and self.heap[largest] < self.heap[left]:
			largest = left
		if len(self.heap) > right and self.heap[largest] < self.heap[right]:
			largest = right
		if largest != index:
			self.__swap(index, largest)
			self.__bubbleDown(largest)
	def __str__(self):
		return str(self.heap)

mh = MaxHeap([95,30,2,1,6,24,46,12,31])
mh.push(10)
print(mh)
print(mh.pop())
print(mh.pop())
mh.push(140)
print(mh)
print(mh.pop())
print(mh.peek())

#CAMBIANDO DE LUGAR ALGUNOS SIMBOLOS SE PUEDE CONVERTIR EN UNA MIN HEAP