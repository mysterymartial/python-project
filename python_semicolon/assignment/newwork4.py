number = 0
while 'True':
	number = int(input("Enter five integers"))
	lastnumber= number % 10   #3
	lastdivide = number // 10    #12
	fourthnumber = lastdivide % 10  #2
	fourthdivide = lastdivide // 10
	thridnumber = fourthdivide % 10
	thirddivide = fourthdivide // 10
	secondnumber = thirddivide % 10
	seconddivide = thirddivide // 10
	firstnumber = seconddivide % 10


   
	print(firstnumber,secondnumber,thridnumber,fourthnumber,lastnumber)

	
	