def get_product(*numbers):
	product = 1
	for number in numbers:
		product *= number

	return product






print(get_product (1,4,5))
print(get_product (2,4,8, 10))
print(get_product (5)) 