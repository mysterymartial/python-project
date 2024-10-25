class Account:
    def __init__(self,account_number,pin):
        self.account_number = account_number
        self.pin = pin
        self.balance = 0
    def getBalance(self,pin):
        if pin == self.pin:
            return self.balance
        else:
            raise ValueError("Pin is not valid")

    def deposit(self,account,amount):
        is_amount_valid =  amount > 0
        if is_amount_valid:
            self.balance +=  amount
        else:
            raise ValueError("invalid amount")
    def withdraw(self,pin,amount):
        self.pin = pin
        is_amount_valid = amount > 0 and amount < self.balance
        if is_amount_valid:
            self.balance -= amount
        else:
            raise ValueError("invalid amount")

    def update_pin(self,old_pin,new_pin):
        old_pin == new_pin
        self.pin = new_pin


