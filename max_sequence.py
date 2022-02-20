def max_sequence(arr):
	max_sum,result = 0,0
	for i in arr:
		result += i
		if result < 0:result = 0
		if result > max_sum:max_sum = result
	return max_sum

print(max_sequence([2, -1, 3, -4, 1, -2, 1, -5, 4]))
