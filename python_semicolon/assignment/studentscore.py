
counter1 = 0
counter2 = 0
score = 0
for count in range(1,16):
	score = int(input("Enter a score for a student \n"))
	if score >= 45:
		print("this student pass my course")
		counter1 = counter1 + 1
	else:
		print("this student failed my course")
		counter2 = counter2 + 1



print("The total number  of student that passed my course is " , counter1)
print("The total number of student that falied my course is " , counter2)
	