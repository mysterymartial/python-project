name= input("Enter your name")
matric_number = input("Enter your matric number")
score = int(input('Enter your score'))
if score >= 75:
	print("your grade is A")
elif score < 75 and score >=65:
	print("Your grade is B")
elif score < 65 and score >=50:
	print("Your grade is C")
elif score < 50 and score >= 40:
	print("Your garde is D")

else:
	print("your grade is F you are a stupid boy")