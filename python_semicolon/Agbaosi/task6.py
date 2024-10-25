def minitues_to_days(mintues): 

	days = mintues / 1440
	return days






def minitues_to_years(minitues):

	years = minitues / 525600
	return years





minitues = int(input("Enter your minitues \n"))
result1 = minitues_to_days(minitues)
result2 = minitues_to_years(minitues)
print(f"your minitues in days is {round(result1,3)} and minitues in years is {round(result2,3)}") 