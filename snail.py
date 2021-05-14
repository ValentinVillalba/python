#QUE CAPO QUE SOOOOOOOOOOOOOOOOOOOOOY
#AAAAAAAAAAAAAAAAAAAAAAAAAAAA
#literalmente un genio de los algoritmos
def snail(snail_map):
	result = []
	while len(snail_map) > 0:
		for i in snail_map[0]:
			result.append(i)
		snail_map.pop(0)
		for i in range(len(snail_map)):
			result.append(snail_map[i][-1])
			snail_map[i].pop(-1)
		if len(snail_map) < 1:
			break
		for i in reversed(snail_map[-1]):
			result.append(i)
		snail_map.pop(-1)
		for i in reversed(snail_map):
			result.append(i[0])
		for i in snail_map:
			i.pop(0)
	return result

print(snail(	[[1,2,3,4,5],
         		 [14,15,16,17,6],
         		 [13,20,19,18,7],
         		 [12,11,10,9,8]
         		]
     ))