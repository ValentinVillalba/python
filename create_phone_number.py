def create_phone_number(number):
	#funciona para todo y queda bastante cortito
	phone = ""
	for i in number:
		phone += str(i)
	return "(" + phone[0:3] + ") " + phone[3:6] + "-" + phone[6:len(number)]

print(create_phone_number([7, 5, 7, 0, 3, 1, 2, 4, 7, 4]))
