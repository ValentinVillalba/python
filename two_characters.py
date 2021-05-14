def two_characters(word):
	#funciona piola pero podria ser mejor
	result=[]
	for i in range(len(word)):
		result.append(word[i*2:(i+1)*2])
		if len(result[i]) < 1:
			del result[i]
			break
		if len(result[i]) < 2:
			result[i] += "_"
			break

	return result

print(two_characters("abcdef"))