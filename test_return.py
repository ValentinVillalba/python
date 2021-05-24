def xdlol(p1, p2):
	a = p1
	b = p2
	return a, b #los retorna en forma de tupla

print(xdlol(5,6))

#aca estaba testeando la comparacion de diccionarios
dic1 = {"a":1,"b":2}
dic2 = {"b":2,"a":1}

if dic1 == dic2:
	print("son iguales")
else:
	print("son diferentes")

#aca testeo filter y lambda
lista = [1,2,3,4,5,6,7,8,9,10]

result = list(filter(lambda x: x%2==0 , lista)) 
#SE DEBE CONVERTIR AL TIPO DE DATO QUE CORRESPONDA O SI NO RETORNARA UNA UBICACION

print(result)

words = ["xd","lol","aaaa"]
word = "xd"
jkl = [i for i in words if sorted(i)==sorted(word)]
print(jkl)