def paystack (amount, years):
	result = 0
	annualrate = 7
	ratecalc = 1 + annualrate
	result = amount * (ratecalc ** years)
	return result
	


amount = int(input("Enter the amount of your monthly pay \n"))
for count in range (1,31):
	answer = paystack(amount, count)
	print(f"this is the intreset {answer} and this is the years {count}")
	
	
	
