# create a iterator from 1000 to 3000
# create a condition that check if the number is an even number
# print the result



for number in range(1000,3000):
	if number % 2 == 0:
	
		for count in iter(str (number)):
			if int(count) % 2 == 0:
				print(f"{count:^5}", end =" ," )