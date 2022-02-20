def solution(number):
	#funciona para todos los casos pero considero que podria estar mejor
	n=number - 1
	total=0
	while n > 0:
		if n % 3 == 0 or n % 5 == 0:
			total += n
		n -= 1
	return total

print(solution(10))
