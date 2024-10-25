def shop(amount, pay):
	change = 0
	change = (amount - pay)
	changes = change * -1

	return changes



item = int(input("Enter the amount of the goods customer is buying \n"))
payment = int(input("Enter the amount the customer give to you \n"))
pay = shop(item, payment)
print(f" the customer change is {pay} pennies")
