def smallerOne(a,b):
	#Es una funcion de una linea que usa matematica y bool para dar un resultado
	#funciona haciendo un calculo en el que uno de los dos lados dara como resultado 0
	#y el otro lado dara como resultado el numero ingresado y se retornará.
	#Hay que recordar que True y False, tambien son 1 y 0, respectivamente.
	#Es un ejemplo de funcion sin ramas, evitando usar "if" y acelerando el programa.
	return a * (a < b) + b * (b <= a)

print(smallerOne(56,23))