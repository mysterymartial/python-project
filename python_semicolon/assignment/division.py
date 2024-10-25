def division(*numbers):
	average = 0

	
	for number in numbers:
		if number == 0:
			return "Zero division"
		average +=number/number;
	return average




numbers = division(1,2,3)
print(numbers)