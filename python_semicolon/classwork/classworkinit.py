from random import randint

print("Welcome to my guess game")
mygame = randint(1,1000)
sentel= -1
factor1 = 0
factor2 = 0
sum = 0

userguess = int(input("enter any number to start and -1 to exit \n"))




while userguess != sentel:
	guess = int(input("Try to guess my lucky number enter a number between 1 to 1000 \n")) 
	if guess == mygame:
		print("Congratulation you have correctly guessed my lucky number")

	elif guess > mygame:
		print(" your guess is too high")
		factor1= factor1 +1

	else:

		print("your guess is too low")
		factor2 = factor2 + 1
		userguess = int(input("Enter any number to continue and -1 to exist \n"))



	sum = factor1 + factor2

print("Total amount ot trials is ", sum)		