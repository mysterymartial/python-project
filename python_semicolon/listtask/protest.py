from random import choice

def protest_demands():

	demand = ["end hunger", "end eletion malpratices", "increase salary", "end tinubu", "end Bad Governance","we want tinubu","protest will lead to killings","the people protesting are foolish", "bribe us", "give us peter obi" ]

	feedback = choice(demand)

	return feedback



name = input("Enter your name \n")
age = input("Enter your age \n")
feedback = protest_demands()
print("This is a demand from the protester " , feedback)
		
