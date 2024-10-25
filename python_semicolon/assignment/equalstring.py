def equal_string(word, reverse):
	sorted_word = ''
	if (len(reverse)) == (len(word)):
		spliteed_word = list(word)
		for character in spliteed_word: 
			if character in reverse:
				sorted_word = sorted_word + character
		if word == sorted_word:
			return True
		else: 
			return False
	else :
		return False



word = input("Enter a word\n")
reverse = input("Enter another word \n")
response = equal_string(word, reverse)
print(response)