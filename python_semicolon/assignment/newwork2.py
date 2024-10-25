sum = 0
average = 0
product = 1
largest = 0
smallest = 0


for count in range(4):
	firstnumber = int(input("enter first integer number \n"))
	secondnumber= int(input("enter second integer number \n"))
	thirdnumber= int(input("enter third integer number \n"))
	fourthnumber= int(input("enter fourth integer number \n"))	

	sum = (firstnumber + secondnumber + thirdnumber + fourthnumber)
	product = firstnumber * secondnumber * thirdnumber * fourthnumber
	average = sum / 4
	largest = max(firstnumber, secondnumber, thirdnumber, fourthnumber)
	smallest = min(firstnumber, secondnumber, thirdnumber, fourthnumber)
	
	print("your sum is " , sum)
	print("your average is " , average)
	print("your product is " , product)
	print("your smallest number is " , smallest)
	print("your largest number is " , largest)

