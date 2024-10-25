def only_float(value1, value2):
	
	flag = 2.0

	if type(value1) == type(flag) and type(value2) == type(flag):
		return 2

	elif type(value1) == type(flag) or type(value2) == type(flag):
		return 1

	elif type(value1) != type(flag) and type(value2) != type(flag):
		return 0 


answer = only_float(22.4, 8.0)
print(answer)


