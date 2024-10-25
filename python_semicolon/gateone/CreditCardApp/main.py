import creditcard

print("Welcome my friend to my credit card validation app")
name = input("Enter your name \n")

age = input("Enter your age \n")
card_number = input("Enter your card number \n")
result = creditcard.validate_card(card_number)
print("Credit card type: ", result[0])
print("Credit card number: ", result[1])
print("Credit card digits length: ", result[2])
print("Credit card validility status: ", result[3])