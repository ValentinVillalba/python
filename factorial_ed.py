def factorial_iter(num):
	result = 1
	for i in range(1, num + 1):
		result *= i
	return result

def factorial_recur(num):
	if num == 0:
		return 1
	else:
		return num * factorial_recur(num - 1)

numero = int(input("Ingresar un numero: "))
print("Iterativo: ", factorial_iter(numero))
print("Recursivo: ", factorial_recur(numero))