import math
def divide_square(number):

	square = 1
	
	if number % 5 == 0:
		square = math.sqrt(number)

		return square

	else:

		return number % 5





number = int(input("Enter a number \n"))
square = divide_square(number)
print(f"{square:.2f}")

	

	