def get_palindrome(user_input):

	item_list = list(user_input)
	new_userinput = ''
	for count in range(1, len(item_list)+1):
		new_userinput = new_userinput + item_list [-count]

	if new_userinput == user_input:
		return f"{user_input} is a palindrome"

	else:

		return f"{user_input} is not a palindrome"



words = get_palindrome('obo')
print(words)