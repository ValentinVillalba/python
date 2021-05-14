def puedeTomar(edad):
	#con esto evito que se ingrese algo erroneo
	if type(edad) == int :
		#con esto el codigo se vuelve mas corto y no necesita usar "else"
		if (edad < 18):
			return "No puede tomar."
		if (edad < 21):
			return "No puede tomar en EEUU."
		return "Si puede."
	return "Error: no se ingresó un entero."

print(puedeTomar(26))