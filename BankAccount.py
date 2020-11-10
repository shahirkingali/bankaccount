class BankAccount(object):
    interestRate = 0.00083
    AccountNum = 87654672
    RoutingNum = 223344556

    def __init__(self, name, bal):
        self.__name = name 
        self.__balance = bal 
        self.__accountnumber = BankAccount.nextAccountNum
        BankAccount.nextAccountNum += 1

    def __str__(self):
        output = "Name: " + str(self.__name) + "\n"
        output += "AccNum: " + str(self.__accountNumber) + "\n"
        output += "Balance:$ " + str(self.__balance) + "\n"

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Amount Withdrawn " + str(self.__accountNumber))
            print("Insufficient funds ", amount)

    def addIntrest(self):
        amount = self.__balance * BankAccount.interestRate
        self.addIntrest(amount)

    def get_balance(self):
        self.show_details()
        print("Account balance: $", self.balance)

if __name__== '__main__':
    account1 = BankAccount("Shahir", 10000.00)
    print(account1)
    account1.addIntrest()
    print(account1)
