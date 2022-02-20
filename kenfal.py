#ayuda para un trabajo de la facultad de un amigo
numero = 0

while numero >= 0:
	numero = int(input("Ingresar numeros enteros positivos: "))
	if numero < 0:
		break
	numero_original=numero
	pares=0
	impares=0
	cant_dos=0
	cant_digitos=0
	if (numero % 10) % 5 == 0:
		print("El último dígito del número ingresado es múltiplo de 5")
	else:
		print("El último dígito del número ingresado no es múltiplo de 5")
	while numero > 0:
		digito = numero % 10
		numero //= 10
		if digito % 2 == 0:
			pares += 1
		else:
			impares += 1
		if digito == 2:
			cant_dos += 1
		cant_digitos += 1
	print("El número ",numero_original,"tiene: ",impares," dígitos impares y ",pares," dígitos pares.")
	print("El número ",numero_original,"posee: ",cant_digitos," digitos.")
