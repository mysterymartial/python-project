# prompt the user to enter digit between 0 to 1000
# user a selcetion statement to influnce the user input to be between that range you want
# separte the number with modulous and floor division
# sum up the numbers and print the sum

numbers = int(input("Enter set of integer \n"))
sum = 0


if numbers >= 0 and numbers <= 1000:
	
		last_number = (numbers % 10)
		last_division = numbers // 10
		second_number = last_division % 10
		second_division = last_division // 10
		first_number = second_division % 10
	

		sum = first_number + second_number + last_number
		
print(sum)