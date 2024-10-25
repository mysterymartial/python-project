def vowel_consonant_checker(word):
	vowel = ''
	consonant = ''

	for character in word:
		if character.lower() in ['a', 'e', 'i', 'o', 'u']:
			vowel += character

		else:
			consonant += character
		
	

	return f"the number of vowels in your word is {len(set(vowel))} and the number of consonant is {len(set(consonant))}"

  

userinput = input("Enter your chossen word \n")
result = vowel_consonant_checker(userinput)
print(result)
