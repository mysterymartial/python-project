def largest(numbers):
	large = 0
	for number in numbers:
		if number > large:
			large = number
	return large
		
		



numbers = [2, 14, 4, 44, 66]
result = largest(numbers)
print(result)