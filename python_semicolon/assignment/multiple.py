print("This are the number that are divisible by 7 and not multiple of 5, between 770 to 4200")
for count in range(770,4200):
	if count % 7 == 0:
		if count % 5 != 0:
			print(f"{count:^4}  ",  end= ', ')
		