def height_converter(height_in_feet):
	height_in_meter = height_in_feet / 0.305
	return f"{round(3,height_in_meter)}"


height = float(input("Enter your height in foot \n"))
result = height_converter(height)
print(result)


	

	