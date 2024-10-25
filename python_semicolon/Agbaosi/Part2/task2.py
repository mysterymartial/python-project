# collect a word from the user
# collect a set of integer from the user
# iterate through the both of them
# count the occurance
# print the the occcurance






alphabet = input("Enter a word \n")
number = input("enter a set of numbers \n")
numbers = list(number)
count = ""
counter = ""
for character in alphabet:
	count += character
for length in numbers:
	 counter += length

print(f"{len(count)} {len(counter)}")
	