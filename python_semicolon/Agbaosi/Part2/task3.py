# create a function
# pass a two parameters into your function
# convert the to integer and sum up
# return the result as string




def total(number1, number2):
	
	 add = int(number1) + int(number2)
	 return str(add)



number1 = input("Enter your first number \n")
number2 = input("Enter your second number \n")
result = total(number1,number2)
print(result)