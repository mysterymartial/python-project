number = input("Enter your frist decimal number\n")
number = float (number)
number1 = input("Enter your second decimal number\n")
number1 = float (number1)
number2 = input("Enter your third decimal number\n")
number2 = float (number2)
if (number > number1 and number1 > number2):
	print("your first number", number, "is larger")
elif (number1 > number and number1 > number2):
	print("your second number", number1, "is larger")
else:
	print("your third number", number2, "is larger")