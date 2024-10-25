print("Welcome to my miles gallon calculator")
userinput = int(input("Enter any number to procced or -1 to exit \n"))
sum = 0
counter = 0
average = 0
while userinput != -1:
	
	miles_driven = int (input("Enter miles driven \n"))
	gallon = int (input("Enter the amount of gallons used \n"))
	counter + 1
	miles_gallons = miles_driven / gallon
	print("your milepergallon fof this trip is ", miles_gallons)
	sum += miles_gallons
	average = sum / 3
	userinput = int(input("Enter any number to procced or -1 to exit \n"))


print("Your total miles per gallon is " , sum)
print(" Your average miles per gallon is " , average)