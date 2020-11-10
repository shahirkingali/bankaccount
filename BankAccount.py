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
def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insefficient funds")
    def print_balance(slef):
        return self.balance

#Create an isntance
account = BankAccount()

#Will desposit amount into account
account.deposit(100)
print(account.print_balance)