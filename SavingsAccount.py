# refering class defined in another module/file
from BankAccount import BankAccount
class SavingsAccount(BankAccount):
  def dummy(self):
    pass
  def calculate_interest(self):
      interset=self.get_account_balance() * 5/100
      return interset