def get_length(word):
	total_length = 0
	for character in word:
		 total_length = total_length + 1

	return total_length



userinput = ("Enter a word or list")
result = get_length([1,2,3,4,5])
result1 = get_length("dunni")
print(result)
print(result1)