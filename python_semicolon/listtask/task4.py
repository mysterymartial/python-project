def odd_position(numbers):

	odd_numbers = [int (num) for num in numbers if num % 2 != 0]
	return odd_numbers



numbers = [1,2,3,4,5]
result = odd_position(numbers)
print(result)