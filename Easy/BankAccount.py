class Bank:
    def __init__(self, name, monetaryCapacity):
        self.name = name
        self.capacity = monetaryCapacity
        self.accounts = []
        self.employees = []


class Account:

    def __init__(self, accountHolderName, initialValue):
        self.name= accountHolderName
        self.value = initialValue

    def getBalance(self):
        print(f'Your current balance is ${self.value}')

    def deposit(self, depositAmount):
        self.value += depositAmount
    
    def withdraw(self, withdawalAmount):

        if self.value >= withdawalAmount:
            self.value -= withdawalAmount
            print(f'Congrats! you have withdawn {withdawalAmount}')
            print(f'Your current Balance is: {self.value}')
        else:
            print("I'm sorry you Don't have Enough in your account")
            print(f'Your current Balance is: {self.value}')
            