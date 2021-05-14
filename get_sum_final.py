def get_sum(a, b):
	#esto es literalmente la formula de gauss
	#((a + b) * n) // 2
    return (a + b) * (abs(a - b) + 1) // 2

print(get_sum(-11,7))