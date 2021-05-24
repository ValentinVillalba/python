def anagrams(word, words):
	result = []
	dicc1 = {}

	for i in word:
		if i not in dicc1:
			dicc1[i] = 1
		else:
			dicc1[i] += 1

	for e in words:
		dicc2 = {}
		for letter in e:
			if letter not in dicc2:
				dicc2[letter] = 1
			else:
				dicc2[letter] += 1
		if dicc2 == dicc1:
			result.append(e)

	return result

print(anagrams("racer", ['crazer', 'carer', 'racar', 'caers', 'racer']))