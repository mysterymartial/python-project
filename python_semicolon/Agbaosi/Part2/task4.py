def even_odd(number):
	if number % 2 == 0:

		return f"your number is an even number"

	else:
		return f"your number is an odd number"



number = int(input("Enter a number \n"))
result = even_odd(number)
print(result)