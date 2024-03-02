'''Create a class for managing a bank account, emphasizing encapsulation with 
private attributes and methods.
Requirements
Create a class named BankAccount with private attributes:
__account_number: A unique identifier for the bank account.
__balance: The current balance of the bank account.
__owner: The owner's name.
Implement the following methods within the BankAccount class:
A constructor __init__ to initialize the attributes.
Getter methods for each attribute (get_account_number, get_balance, get_owner).
Setter methods for each attribute (set_balance, set_owner).
A method deposit to add funds to the account.
A method withdraw to deduct funds from the account.
Implement input validation in the setter methods:
Ensure that the balance is a non-negative value.
Ensure that the owner's name is not empty.
Implement input validation in the withdraw method:
Ensure that the withdrawal amount is less than or equal to the current balance.
Demonstrate the usage of the BankAccount class in the main program by 
creating an instance, setting attributes, depositing and withdrawing funds, 
and displaying account information.'''
class BankAccount:
    def __init__(self, account_number , balance , owner):
        self.__account_number = account_number
        self.__balance = balance
        self.__owner = owner

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def get_owner(self):
        return self.__owner

    def set_account_number(self , new_account_number):
        self.account_number = new_account_number

    def set_balance(self , new_balance):
        if new_balance < 0:
            print(f"Invalid Balance i.e. Balance can't be negative.")
        else:
            self.balance = new_balance

    def set_owner(self , new_owner):
        if new_owner.strip():
            self.__owner = new_owner
        else:
            print("Owner's name cannot be empty.")

    def check_details(self):
        print(f"Account Number : {self.__account_number} Balance : {self.__balance} and Owner Name : {self.__owner}")
            
    def deposit(self , amount):
        if amount < 0 :
            print("Amount can't be negative")
        else:
            self.__balance = self.__balance + amount
            print(f"Balance after deposit is : {self.__balance}")

    def withdraw(self , withdraw_amount):
        if withdraw_amount <= 0:
            print(f"Invalid withdraw amount")
        elif withdraw_amount > self.__balance:
            print(f"Insufficeint Balance")
        else:
          self.__balance = self.__balance - withdraw_amount  
          print(f"Withdraw amount is : {withdraw_amount} and new balance is : {self.__balance}:")

account = BankAccount("07891121", 1000, "Sinja")

account.set_balance(-1221) 
account.set_owner("")  

account.deposit(10000)
account.withdraw(20000) 
account.check_details()