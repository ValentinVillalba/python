def duplicate_encode(word):
	result=""
	word_list=[]
	for i in word:
		word_list.append(i.lower())
	for i in word_list:
		if word_list.count(i) > 1:
			result += ")"
		else:
			result += "("
	return result

print(duplicate_encode("(())())"))