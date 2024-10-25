def vowels(words):
	count = 1
	vowel_count = 0
	while count <= 5:
		if count == 1 and 'a' in words:
			vowel_count = vowel_count + 1
		elif count == 2 and 'e' in words:
			vowel_count = vowel_count + 1
		elif count == 3 and 'i' in words:
			vowel_count = vowel_count +1
		elif count == 4 and 'o' in words:
			vowel_count = vowel_count +1
		elif count == 5 and 'u' in words:
			vowel_count = vowel_count +1
		
		count = count + 1

	return vowel_count


def consonant(words):
	count = 1
	consonant_count = 0
	while count <= 21:
		if count == 1 and 'b' in words:
			consonant_count = consonant_count + 1
		if count == 2 and 'c' in words:
			consonant_count = consonant_count + 1
		if count == 3 and 'd' in words:
			consonant_count = consonant_count + 1
		if count == 4 and 'f' in words:
			consonant_count = consonant_count + 1
		if count == 5 and 'g' in words:
			consonant_count = consonant_count + 1
		if count == 6 and 'h' in words:
			consonant_count = consonant_count + 1
		if count == 7 and 'j' in words:
			consonant_count = consonant_count + 1
		if count == 8 and 'k' in words:
			consonant_count = consonant_count + 1
		if count == 9 and 'l' in words:
			consonant_count = consonant_count + 1
		if count == 10 and 'm' in words:
			consonant_count = consonant_count + 1
		if count == 11 and 'n' in words:
			consonant_count = consonant_count + 1
		if count == 12 and 'p' in words:
			consonant = consonant_count + 1
		if count == 13 and 'q' in words:
			consonant_count = consonant_count + 1
		if count == 14 and 'r' in words:
			consonant_count = consonant_count + 1
		if count == 15 and 's' in words:
			consonant = consonant_count + 1
		if count == 16 and 't' in words:
			consonant_count = consonant_count + 1
		if count == 17 and 'v' in words:
			consonant_count = consonant_count + 1
		if count == 18 and 'w' in words:
			consonant_count = consonant_count + 1
		if count == 19 and 'x' in words:
			consonant_count = consonant_count + 1
		if count == 20 and 'y' in words:
			consonant_count = consonant_count + 1
		if count == 21 and 'z' in words:
			consonant_count = consonant_count + 1
		count = count + 1
	
	return consonant_count


	

userinput = input("Enter a word \n")
vowel_word = vowels(userinput.lower())
consonant_word = consonant(userinput.lower())
print(f"we have {vowel_word} of vowels and { consonant_word} of consonant")












































	




