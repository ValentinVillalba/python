#LAS COLAS SON UNA ESTRUCTURA FIFO
#EL PRIMER ELEMENTO EN ENTRAR SERA EL PRIMERO EN SALIR
#LOS ELEMENTOS ENTRAN "POR UN LADO" Y SALEN "POR EL OTRO"

#EJEMPLO DE USO: SIRVEN PARA MODELAR CUALQUIER COSA QUE DEBA ESPERAR SU TURNO
#COMO LOS PEDIDOS EN UN RESTAURANTE.

from dataclasses import dataclass
from typing import Any # Any representa "cualquier tipo"

class Queue():

	@dataclass
    class _Node:
        value: Any
        next: '_Node'

	def __init__(self):
		self.queue = _Node

	def inqueue(self,item):
		self.queue.insert(0,item)

	def dequeue(self):
		self.queue.pop()

	def __str__(self):
		return str(self.queue)

	def peek(self):
		if len(self.queue) > 0:
			return self.queue[len(self.queue)-1]
		else:
			return None

cola = Queue()
cola.inqueue(1)
cola.inqueue(2)
cola.inqueue(3)
cola.inqueue(4)
print(cola)
cola.dequeue()
print(cola)
print(cola.peek())