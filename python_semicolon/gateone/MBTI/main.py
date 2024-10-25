import mbti
answer = []
my_question = mbti.get_questions() 
for type in my_question:

	print(type)
	selection = input("Enter A or B \n")
	if selection.upper() != "A" and selection.upper() != "B":
		flag = True
		while   flag: 
		
			selection = input("Enter A or B \n")
			if selection.upper() == "A" or selection.upper() == "B":
				flag = False
		 
	answer += selection

first_response = mbti.get_first_response(answer)
second_response = mbti.get_second_response(answer)
third_response = mbti.get_third_response(answer)
fourth_response = mbti.get_fourth_response(answer)

personality = mbti.get_personality(first_response, second_response, third_response, fourth_response)

  
print(personality)
