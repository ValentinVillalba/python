def make_readable(ss):
	return "".join("{:02}"+":"+"{:02}"+":"+"{:02}").format(ss // 3600, (ss % 3600) // 60, ss % 60)

#3600 es la cantidad de segundos que hay en una hora
#la funcion recibe segundos
print(make_readable(39147))