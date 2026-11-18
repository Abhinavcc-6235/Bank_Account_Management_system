#create an objct of current account
from CurrentAccount import CurrentAccount
from simple import SimpleAccount
from BankAccount import BankAccount
from SavingsAccount import SavingsAccount

# creating an object of class simpleaccount
# simp1=SimpleAccount()
# simp1.methode1()
# # not possible beacuse we can't create an object of an abstract class
# bankac1=BankAccount()
# bankac1.deposit()
print('-------curreent account deposit----------')
cu1=CurrentAccount()
# cu1.dummy()         #methode defined in child class
cu1.deposit(1000)   # methode is defined in parent class
# print(f'balance amount is:{cu1.__account_balance}')   # this can't be done beacuse varible is protected from  being acces from outside
# to display the balance use the function from the parent class
cu1.display_balance()

cu1.deposit(-500)

cu1.display_balance()
print('--------withdraw-----------')

cu1.withdraw(500)
cu1.display_balance()

cu1.withdraw(-500)
cu1.display_balance()

cu1.withdraw(1200)
cu1.display_balance()

print('---------intrest----------')
print('intrest amount is:',cu1.calculate_interest())

print('-------------savings account deposit-----------')

sav1=SavingsAccount()
sav1.deposit(100)
sav1.display_balance()

sav1.deposit(-400)
sav1.display_balance()

print('--------withdraw details---------')

sav1.withdraw(50)
sav1.display_balance()

sav1.withdraw(-50)
sav1.display_balance()

sav1.withdraw(100)
sav1.display_balance()
print('--------intrest for savings acc-------')
print('intrest amount is:',sav1.calculate_interest())
print('helooo')