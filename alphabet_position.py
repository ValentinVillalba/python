import string
import re
from collections import OrderedDict

regex = re.compile('[^a-zA-Z]')

def alphabet_position(text):
	alphabet = OrderedDict(zip(string.ascii_lowercase, range(1,27)))
	final_list = []
	new_text = regex.sub('', text)
	for i in new_text.lower().replace(" ", ""):
		final_list.append(alphabet[i])
	joined_string = ' '.join([str(v) for v in final_list])
	return joined_string

print(alphabet_position("AXPOKF sjfapsj zxx aaaaa zzz !!!%!=?? 894891 111 2 xd ñññ"))