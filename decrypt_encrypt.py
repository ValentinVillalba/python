def decrypt(encrypted_text, n):
	pass

def encrypt(text, n):
    times=0
    result=text
    while times < n:
    	to_edit=result
    	result=to_edit[1::2] + to_edit[0::2]
    	times += 1
    return result

print(encrypt("This is a test!",1))
#print(decrypt("hsi  etTi sats!",1))

#result=encrypted_text[len(encrypted_text)//2:len(encrypted_text)] + encrypted_text[0:len(encrypted_text)//2]