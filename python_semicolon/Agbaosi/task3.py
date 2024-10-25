#prompt the the user to enter a weight in pound
#store what the user entered in a varriable
# divide the user input by 2.2046
# stored the calcultion in varriable
# print out the varriable


def weight_converter(weight_in_pound):
	weight_in_kg = weight_in_pound / 2.2046
	return weight_in_kg



weight = float(input("Enter weight in pound \n"))
result = weight_converter(weight)
print("your weight in kilogram is ", round(result,3))