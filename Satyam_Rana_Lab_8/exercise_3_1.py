class BankAccount:
    def __init__(self, acc_number):
        self.__acc_number = acc_number
        self.__balance = 100.0
    def get_account(self):
        return self.__acc_number
    def get_balance(self):
        return self.__balance
    def deposit(self, amount):
        if(amount > 0):
            self.__balance = self.__balance + amount
        else:
            print("Enter amount greater than 0")
    def withdraw(self, amount):
        if(amount > 0):
            if(self.__balance - amount >= 0):
                self.__balance = self.__balance - amount
            else:
                print("Insufficient Balance")
        else:
            print("Enter amount greater than 0")
    def transfer(self, amount, acc):
        if 0 <= amount <= self.__balance:
            self.withdraw(amount)
            acc.deposit(amount)

a1 = BankAccount(1001)
a2 = BankAccount(1002)

a1.withdraw(40)
a2.withdraw(40)

print(a1.get_balance())
print(a2.get_balance())

a1.deposit(20)
a2.deposit(20)

print(a1.get_balance())
print(a2.get_balance())

a2.transfer(20, a1)
print(a1.get_balance())
print(a2.get_balance())