from abc import ABC,abstractmethod
class BankAccount(ABC):
    def __init__(self):    #constructor of the class
        self.__account_balance=0          # its a private variable -encapsulation
    #    self .account_name=bank_name
    
    @abstractmethod                  #child class must be inerited by the child class
    def calculate_interest(self):
        pass
    
    def display_balance(self):
        # print('bank name is:',self.account_name)
        print('account balance is:',self.__account_balance)
        # return self.__account_balance
        
    def get_account_balance(self):    # to the balance amount
        return self.__account_balance
    
    def deposit(self,amount):
        self.amount=amount
        if amount>0:
          self.__account_balance=self.__account_balance+amount
          print ('deposited amount:',self.__account_balance) #print
        else:
            print("deposit amount must be greater than zero")

    def withdraw(self,amount):
        self.amount=amount    
        if ((amount>0) and (amount<self.__account_balance)): #>0
            self.__account_balance=self.__account_balance-amount 
            print('withdrawing money:',self.__account_balance)
        elif amount>self.__account_balance:
            print('insuficcent fund')   
        else:
            print('withdraw amount should be positive')  

