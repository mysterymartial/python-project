def for_total(number):
	
	sum = 0
	for number in numbers:
		sum += number

	return sum

def while_total(numbers):
	counter = 0
	total = 0
	while counter < len(numbers):
		total += numbers[counter]
		counter = counter + 1
	return total



numbers = [1,2,3,4,5]
result = for_total(numbers)
result1 = while_total(numbers)
print(result)
print(result1)
	