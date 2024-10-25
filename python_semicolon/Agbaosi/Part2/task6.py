def get_sorted_number(number1,number2,number3):
		large = 0
		lowest = 0
		middle = 0

		if number1 > number2 and number1 > number3:
			large = number1
		elif number1 < number2 and number1 < number3:
			lowest = number1
		else:
			middle = number1 

		if number2 > number1 and number2 > number3:
			large = number
		elif number2 < number1 and number2 < number3:
			lowest = number1
		else:
			middle = number2 

		if number3 > number2 and number3 > number1:

			large = number3
		elif number3 < number2 and number3 < number1:
			lowest = number3
		else:
			middle = number1
		result = [lowest,middle,large]
		return result	

number1 = input("Enter the first number \n")
number2 = input("Enter the second number \n")
number3 = input("Enter the third number \n")
result = get_sorted_number(number1,number2,number3)
print(result)

	