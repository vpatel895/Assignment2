class BankAccount:
    Bank_Title = "Trust Bank"
    # Constructor
    def __init__(self,  customer_name , current_balance, minimum_balance, account_number, routing_number):

          self.customer_name = customer_name
          self.current_balance = current_balance
          self.minimum_balance = minimum_balance
          self._account_number = account_number
          self.__routing_number = routing_number

          #Method to deposit money
    def deposit(self, amount):
             if amount > 0:
              self.current_balance += amount
              print(f"${amount} has been deposited to {self.customer_name}'s account")
             else:
                    print("Please deposit a positive amount.")


          #Method of withdraw money
    def withdraw(self, amount):
           if amount > 0 and self.current_balance - amount >= self.minimum_balance:
             self.current_balance -= amount
             print(f"${amount} has been withdrawn from {self.customer_name}'s account")
           elif amount <= 0:
                  print("Invalid amount")
           else:
              print(f"You cannot withdraw {amount} because you need to keep minimum balance")

       #Merhod to print_customer_information including bank name
    def print_customer_information(self):
      print(f"Bank:{BankAccount.Bank_Title}")
      print(f"Customer Name:{self.customer_name}")
      print(f"Current Balance:{self.current_balance}")
      print(f"Minimum Balance:{self.minimum_balance}")
      print(f"Account Number:{self._account_number}")
      print(f"Routing Number:{self.__routing_number}")

    def ___routing_number(self):
        return self.__routing_number



