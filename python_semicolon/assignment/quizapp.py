import random
print("Welcome to my quiz app")


def problems():
	collect = ["calculate 2+2 =", "calculate 2 +1", "calculate 2 x3", "calculate 1+1:", "calculate 4+4", "calculate 7 x 1", "calculate 1 x 10:", "what number is after 10", "calculate 3x3", "calculate for x in 2x + 2=0"]
	random_quiz= random.choice(collect)
	return random_quiz

def result(attempt,question):
	if question == "calculate 2+2 =" :
		if attempt == 4:
			return "passed"
		else:
			return "falied"

	elif question == "calculate 2+1" :
		if attempt == 3:
			return "passed"
		else:
			return "falied"
	elif question == "calculate 2x3":
		if attempt == 6:
			return "passed"
		else:
			return "failed"
	elif question == "calculate 1+1":
		if attempt == 2:
			return "passed"
		else:
			return "falied" 
	elif question == "calculate 4+4":
		if attempt == 8:
			return "passed"
		else:
			return "failed"
	elif question == "calculate 7 x 1":
		if attempt == 7:
			return "passed"
		else:
			return "failed"
	elif question == "calculate 1 x 10":
		if attempt == 10:
			return "passed"
		else:
			return "falied"
	elif question == "what is the number after 10":
		if attempt == 11:
			return "passed"
		else:
			return "failed"
	elif question == "calculate 3 x 3":
		if attempt == 6:
			return "passed"
		else:
			return "failed"
	elif question == "calculate for x in 2x + 2 = 0":
		if attempt == 1:
			return "passed"
		else:
			return "failed"

total_question_passed = 0
question_attempt =0
computer_feedback= " "
question_at = 0
for attempt in range(1,11):
	question = problems()
	print(question)
	question_attempt = 0
	while question_attempt < 10:
		attempt= int(input("Enter your answer:\n"))
		computer_feedback = result(attempt,question)
		print("Thanks",  computer_feedback)
		


		if computer_feedback == "passed":
			continue
			total_question_passed = total_question_passed + 1
		else:
			question_attempt = question_attempt + 1
print(" ")

	
print("The total question you got correctly is " , total_question_passed)
print("The total question you failed is " , question_attempt)
	