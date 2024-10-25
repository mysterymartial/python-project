fristname=input("Enter your Firstname: ")
lastname=input("Enter your  Lastname: ")
age= input("Enter your age: ")
age= int(age)
#print("Your fullname is " + fristname,lastname, "and your age is " +age)
#message=""" my name is miracle mystery
		#am 24   """
#print(message)
if age >= 20 and age<=45:
	print('you are an adult')
	print('you can nak')
	print('get a babe')
elif age >= 13 and age <=19:
	print("you are still a teenager")
	print("you don't need a girl friend")
elif age >0 and age<13:
	print("you are a child")
	print("don't even near girls")

else:
	print('you are too old to nak')