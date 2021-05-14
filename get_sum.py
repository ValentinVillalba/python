def get_sum(a,b):
	#pasó 12 de 16 pruebas.
	if b < 0:
		n = a - b
		total = a
		result = a
		while n > 0:
			total -= 1
			n -= 1
			result += total
		return result
	else:
		n = abs(a - b)
		total = a
		result = a
		while n > 0:
			total += 1
			n -= 1
			result += total
		return result

print(get_sum(-11,7))