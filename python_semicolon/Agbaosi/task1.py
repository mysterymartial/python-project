#prompt the user to enter a radius and length of the cylinder
# raise constant pie to the power of 2 and label the output area
# multiply the cylinder and length and label the output as your volume
# print volume and area



def area ():
	pie =3.14159
	calc = pie **2
	

	return calc





def volume(length):
	area = 3.14159 **2
	calc = area * length


	return calc






length = float(input("Enter the length of your cylinder \n"))
result1 = area()
result2 = volume(length)
print("your area is ",round(result1,2))
print("your volume is  ", round(result2,2))