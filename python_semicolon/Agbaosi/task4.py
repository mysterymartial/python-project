# prompt the user to enter subtotal and gravitiy rate
# divide gravitiy rate by 100 and multiply by subtotal
# label the output as gratutity
# add subtotoal to gratutity
# label the output as total
# print gratutity and total

subtotal = int(input("Enter your subtotal \n"))
gravitity = int(input("Enter yout gravitity \n"))
gratutity = (gravitity /100) * subtotal
total = subtotal + gratutity
print(f"your gratutity is {gratutity} and your total is {total}")