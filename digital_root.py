def digital_root(n):
	result = 0
	while n > 0:
		result += n % 10
		n = n // 10
	if result >= 10:
		while result >= 10:
			result = result % 10 + result // 10
	return result