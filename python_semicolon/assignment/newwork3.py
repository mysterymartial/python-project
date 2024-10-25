print("Welcome to my palindrome checker app")


number =  input("Enter a set of integer \n")
number = int (number)
reverse = 0
orgnumber = number
while number != 0:

	reverse = reverse * 10 + number % 10
	number = number // 10
	

	 

if orgnumber == reverse:
	print("your number is a palindrome number")

else:
	print("your number is not a palindrome number")
	

		



