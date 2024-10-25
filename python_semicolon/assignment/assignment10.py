number1 = input("Enter your first number\n")
number2 = input("Enter your second number\n")
number1 = int (number1)
number2 = int (number2)
sum = number1 + number2
average = sum / 2
print("The sum of the numbers is ", + sum)
print("The average of the numbers is ", + average)
if number1 > number2:
	print("your first number", number1, "is larger than your second number", number2)
else:
	print("your second number", number2, "is larger than your frist number", number1)