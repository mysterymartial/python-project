def taxrate(price):
	tax= 0
	if price < 1000000:
		tax = price * (10/100)

		return tax
	

	elif price >= 100000 and price <= 3000000:
		tax = price * (15/100)

		return tax

	elif price >= 3000000 and price <= 5000000:
		tax = price * (20/100)
		return tax
	

	elif price > 5000000:
		tax = price * (25/100)
		return tax
	







carprice = int(input("Enter the price of your car to check your road tax \n"))
road_tax = taxrate(carprice)
print("your road tax is " , road_tax)





	
		