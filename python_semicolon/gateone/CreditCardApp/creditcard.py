def first_step(card_number):
	total = 0
	sum =0 
	for count in range(0,len(card_number),2):
		numbers = int(card_number[count])
		numbers = (numbers * 2)
		if numbers >=10:
			first_digit = numbers % 10
			second_digit = numbers // 10
			sum = first_digit + second_digit
			total = total + sum
		else:

			total += numbers
		
	return total

	
def second_step(card_number):
	sum = 0
	for counter in range(0,len(card_number)):

		numbers = int(card_number[counter])
		if counter % 2 != 0:
			sum += numbers


	return sum

def card_check(card_number):
	first = card_number[0]
	second = card_number[0]
	third1 = card_number[0]
	third2 = card_number[1]
	fourth = card_number[0]
	first = int(first)
	second = int(second)
	third1 = int(third1)
	third2 = int(third2)
	fourth = int(fourth)
	if first == 4:
		return "Visa Card"
	elif second == 5:
		return "Master Card"
	elif third1 == 3 and third2 == 7:
		return "American Express Card"
	elif fourth == 6:
		return "Discover Card"
	else:
		return "Invalid Card"

def validate_card(card_number):
	value1 = first_step(card_number)
	value2 = second_step(card_number)
	card_type = card_check(card_number)
	sumation = int(value1) + int(value2)
	card_length = int (len(card_number))
	card_len = str(card_length)
	feedback = ""
	if sumation % 10 == 0:
		feedback = "Valid"
	else:
		feedback = "Invalid"
	result = [card_type, card_number, card_len, feedback]
	return result
	
			
		
		
		
		
		
