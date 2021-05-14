from dataclasses import dataclass, astuple, asdict, field

#DATACLASS EVITA QUE ESCRIBAMOS MUCHO CODIGO AL DEFINIR CLASES.
#TAMBIEN TIENE MODULOS PARA CONVERTIR LA CLASE EN TUPLA O DICCIONARIO.

#ASI SE DECLARA UNA DATACLASS.
#FROZEN=TRUE VUELVE INMUTABLE A LA CLASE LO CUAL PERMITE CONVERTIRLA EN UN DICCIONARIO.
#ORDER=TRUE PROVEE LOS TIPOS DE ORDEN QUE PUEDAN SER UTILIZADOS.
@dataclass(frozen=True, order=True)
class Comment:
	id: int = field()
	text: str = field(default="") #Tiene un valor por defecto.
	#replies: list[int] = [] #ESTE VALOR POR DEFECTO NO SIRVE YA QUE ES MUTABLE.
	replies: list[int] = field(default_factory=list, compare=False, hash=False, repr=False) #Forma correcta del valor por defecto.

def main():
	comment = Comment(1, "Hola que tal xd.")

	#IMPRIMIR COMO CLASE:
	print(comment)
	#IMPRIMIR COMO TUPLA:
	print(astuple(comment))
	#IMPRIMIR COMO DICCIONARIO:
	print(asdict(comment))

main()