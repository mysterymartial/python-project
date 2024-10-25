def discounting(price, discount_percent):
	discount = 0
	calc = price * (discount_percent/100)
	discount1 = calc - price
	discount = discount1 * -1

	return discount




price = int(input("Enter the price of your item \n"))
discount_percentage = int(input("Enter your discount percentage \n"))
discount = discounting(price, discount_percentage)
print("your discount is ", discount)

	