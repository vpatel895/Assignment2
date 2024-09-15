class BankAccount:
    Bank_Title = "Trust Bank"
    # Constructor
    def __init__(self,  customer_name , current_balance, minimum_balance):

          self.customer_name = customer_name
          self.current_balance = current_balance
          self.minimum_balance = minimum_balance

          #Method to deposit money
    def deposit(self, amount):
             if amount > 0:
              self.current_balance += amount
              print(f"${amount} has been deposited to {self.customer_name}")
             else:
                    print("Please deposit a positive amount.")


          #Method of withdraw money
    def withdraw(self, amount):
           if amount > 0 and self.current_balance - amount >= self.minimum_balance:
             self.current_balance -= amount
             print(f"${amount} has been withdrawn from {self.customer_name}")
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

  #Creating two instances of the BankAccount class
acc1 = BankAccount("John",5000,100)
acc2 = BankAccount ("Jane", 15000, 500)

acc1.deposit(300)
acc1.withdraw(800)
acc1.print_customer_information()

acc2.deposit(500)
acc2.withdraw(16000)
acc2.print_customer_information()