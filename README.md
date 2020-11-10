# BankAccount
This bank account should all a user to do the following:

Your Python program should be created in one file called BankAccount.py.

Define a BankAccount class.

A bank account should have the following attributes:

full_name - the full name of the bank account account owner.
account_number - randomly generated 8 digit number, unique per account.
routing_number - 9 digit number, this number is the same for all accounts.
balance - the balance of money in the account, should start at 0.
Then define the following methods for the BankAccount class:

The deposit method will take one parameter amount and will add amount to the balance. Also, it will print the message: “Amount Deposited: $X.XX”

The withdraw method will take one parameter amount and will subtract amount from the balance. Also, it will print a message, like “Amount Withdrawn: $X.XX”. If the user tries to withdraw an amount that is greater than the current balance, print ”Insufficient funds.” and charge them with an overdraft fee of $10.

The get_balance method will print a user-friendly message with the account balance and then also return the current balance of the account.

The add_interest method adds interest to the users balance. The annual interest rate is 1% (i.e. 0.083% per month). Thus, the monthly interest is calculated by the following equation: interest = balance *  0.00083 .

The print_receipt method prints a receipt with the account name, account number, and balance like this:

Elon Musk
Account No.: ****5678
Routing No.: 98765432
Balance: $100.00 
Outside of the BankAccount class, define 3 different bank account examples using the BankAccount() object.

Your examples should show you using the different methods above to demonstrate them working.
