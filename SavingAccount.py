from BankAccount import BankAccount

class SavingAccount(BankAccount):
    def __init__(self, customer_name , current_balance, minimum_balance, account_number, routing_number, interest_rate):
        super().__init__(customer_name , current_balance, minimum_balance, account_number, routing_number)
        self.interest_rate = interest_rate


    #method to apply interest rate on customer's account balance
    def  apply_interest(self):
        interest = self.current_balance * self.interest_rate
        self.current_balance = self.current_balance + interest
