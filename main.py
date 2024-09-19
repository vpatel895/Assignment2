from SavingAccount import SavingAccount
from CheckingAccount import CheckingAccount

# Creating instances of the SavingAccount and CheckingAccount
savingAccount1 = SavingAccount("Victor", 15000, 600, "85621358", "796320145", 0.02)
savingAccount2 = SavingAccount("Sarah", 9000, 1000, "23659874", "563214708", 0.05)
checkingAccount1 = CheckingAccount("Smith", 5000, 200, "56321487","214632589", 500)
checkingAccount2 = CheckingAccount("Jaden", 6000, 1000, "52632145", "962541485", 300)


savingAccount1.deposit(300)
savingAccount1.withdraw(500)
savingAccount1.apply_interest()
savingAccount1.print_customer_information()

savingAccount2.apply_interest()
savingAccount2.print_customer_information()

checkingAccount1.deposit(500)
checkingAccount1.withdraw(700)
checkingAccount1.print_customer_information()

checkingAccount2.deposit(900)
checkingAccount2.withdraw(700)
checkingAccount2.print_customer_information()
