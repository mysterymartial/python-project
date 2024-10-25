def even_position(numbers):
	even_number = [ int (number) for number in numbers if number % 2 == 0]
	return even_number


numbers = [1,2,3,4,5]
result = even_position(numbers)
print(result)