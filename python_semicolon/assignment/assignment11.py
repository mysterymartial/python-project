number = input("Enter five integer\n")
number = int (number)
firstinteger = number // 10
number =  number % 10
secondinteger = firstinteger // 10
firstinteger = firstinteger % 10
thirdinteger = secondinteger // 10
secondinteger = secondinteger % 10
fourthinteger = thirdinteger // 10
thirdinteger = thirdinteger % 10
fifthinteger = fourthinteger // 10
fourthinteger = fourthinteger % 10
print(fourthinteger, thirdinteger, secondinteger, firstinteger, number);