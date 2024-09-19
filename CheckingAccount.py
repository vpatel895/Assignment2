from BankAccount import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name , current_balance, minimum_balance, account_number, routing_number ,transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit


    #Method to set a transfer limit on customer's account
    def transfer(self, amount):
        if amount > self.transfer_limit:
            print(f"Transfer of ${amount} exceeds limit of ${self.transfer_limit}")

        elif amount < self.transfer_limit:
            print(f"Minimum transfer amount ${amount}")


        elif self.current_balance - amount < self.minimum_balance:
            print(f"Insufficient funds to transfer. You need to maintain your balance of ${self.minimum_balance}")

        else:
            self.current_balance -= amount
            print(f"Transfer completed. ${amount} transferred from {self.customer_name}'s account. Current balance is ${self.current_balance}")