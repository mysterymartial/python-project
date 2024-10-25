def big_odd(number):
	
	numbers = number.split()
	integer_list = [int (count) for count in numbers]
	odd_number = [count for count in integer_list if count % 2 != 0]
	if odd_number:
	
		return max(odd_number)




number = input("Enter a set of number separeted by space \n")
answer = big_odd(number)
print(answer)
	
	
	