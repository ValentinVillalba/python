#LOS NOMBRES SON LOS SIGUIENTES (ORDENADOS DE MEJOR A PEOR):
#Constante = O(1)
#Logaritmica = O(log(n))
#Lineal	= O(n)
#Log Lineal	= O(n log(n))
#Quadratica = O(n^2)
#Exponencial = O(2^n)

#SIEMPRE SE IGNORAN LAS CONSTANTES Y CASI SIEMPRE SE BUSCA EL PEOR CASO.
#(AUNQUE EN LA VIDA REAL ESTAS COSAS SI SON TOMADAS EN CUENTA).

#SIEMPRE UN CASO ES IGNORADO CUANDO SE ENCUENTRA UNO PEOR QUE LO REEMPLACE.

#DE FORMA SIMPLE: SE BUSCAN TODOS LOS O() DE UN PROGRAMA ENTERO,
#EL PROGRAMA SERA CALIFICADO CON EL PEOR O() ENCONTRADO.

#EN CASO DE BUSCAR EL MEJOR CASO: SE DEBE CALIFICAR A PARTIR DEL MEJOR O() ENCONTRADO.

#Este codigo es O(n) ya que depende de la cantidad de entradas:
datos_0 = ['A','B','C']

for z in datos_0:
	print(z)

#Este codigo es O(n + a) ya que depende de la cantidad de entradas de ambos casos:
datos_1 = ['A','B','C']
datos_2 = [1,2,3,4,5,6,7,8,9]

for i in datos_1:
	print(i)

for j in datos_2:
	print(j)

#Este es O(n * a) ya que para cada "n" se iteran todos los "a" (NESTED FOR, MUY LENTO):
#Se podria decir que en realidad es O(n * a + a) pero se debe ignorar todo lo que sea menor
#al calculo principal, se debe ignorar toda constante.
datos_3 = ['A','B','C'] #n
datos_4 = [1,2,3,4,5,6,7,8,9] #a

for x in datos_3:
	print(x)
	for y in datos_4:
		print(y)

#Este codigo es O(n ^ 2) ya que en cada "n" se recorre "n" hasta el final otra vez (HORRIBLE):
datos_5 = ['A','B','C','D','F','G']

for s in datos_5:
	for e in datos_5:
		print(s + e)

#Este codigo es O(2 ^ n) ya que crece exponencialmente con cada entrada:
#NO ENCONTRE UN CODIGO PARA PYTHON PERO USUALMENTE LOS ALGORITMOS RECURSIVOS TIENEN
#ESTE TIPO DE NOTACION.