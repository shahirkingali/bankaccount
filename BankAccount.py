#Intaialze the class
#Class attributes
class BankAccount:
    def __init__(self, fullname, accountnumber, routingnumber, accountbalance):
      self.fullname = fullname
      self.accountnumber = accountnumber
      self.routingnumber = routingnumber 
      self.accountbalance = accountbalance

 def __init__(self):
        self.balance = 0
#Function takes in the amount you put in
def deposit(self, amount):
        self.balance = self.balance + amount
#Function will take away amount from accotunt