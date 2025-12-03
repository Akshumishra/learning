# 4 Pillars of Oops ( Inheritance, Abstraction, Polymorphism, Encapsulation )
from abc import ABC, abstractmethod


class BankAccount(ABC):  # Base Class 1
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance

    @property
    def owner(self):
        return self.__owner

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative!")
        else:
            self.__balance = amount

    @abstractmethod
    def withdraw(self, amount):  # Abstraction
        pass

    def deposit(self, amount):
        print(self)
        self.balance = self.balance + amount
        print(f"Amount Deposited in {self.owner} account: {amount}")
        print(self)

    def __str__(self):
        return f"Account Owner: {self.owner}, Balance: {self.balance}"


class KYC:  # Base Class 2
    def verify_kyc(self, owner):
        print(f"KYC verified for {owner}")


class SavingAccount(BankAccount):  # 1. Single Inheritance
    def withdraw(self, amount):  # Overriding
        if amount > self.balance:
            print(f"Insufficient Balance")
        else:
            print(self)
            self.balance = self.balance - amount
            print(f"Amount Withdraw from {self.owner} account: {amount}")
            print(self)


class CurrentAccount(BankAccount):  # 2. Hierarchical Inheritance
    minBalanceAllowed = 10000

    def withdraw(self, amount):  # Overriding
        if amount > self.balance - self.minBalanceAllowed:
            print(f"Insufficient Balance")
        else:
            print(self)
            self.balance = self.balance - amount
            print(f"Amount Withdraw from {self.owner} account: {amount}")
            print(self)


class SalaryAccount(SavingAccount):  # 3. Multilevel Inheritance
    def credit_salary(self, salary):
        print(self)
        print(f"Credit Salary Amount in {self.owner} account: {salary}")
        self.balance = self.balance + salary
        print(self)


class GeneralAccount(BankAccount, KYC):  # 4. Multiple Inheritance
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)
        print(f"General Account created for {owner} with balance {balance}")

    def withdraw(self, amount):  # Overriding
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}, Remaining Balance: {self.balance}")


class PremiumSavingAccount(SavingAccount, KYC):  # 5. Hybrid Inheritance
    def offer_rewards(self):
        print("Premium Reward Added Successfully!")


class LoanAccount:  # Method Overloading
    def calculate_interest(self, amount=None, rate=None, years=None):
        if amount is not None and rate is None:
            print(f"Interest on {amount} at default 10% = {amount * 0.10}")
        elif amount is not None and rate is not None and years is None:
            print(f"Interest on {amount} at {rate}% = {amount * (rate/100)}")
        elif amount and rate and years:
            total = amount * (1 + (rate / 100) * years)
            print(f"Total amount after {years} years = {total}")
        else:
            print("Invalid parameters")


class TransferAccount:  # Operator Overloading
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"{self.owner} → Balance: {self.balance}"

    def __sub__(self, amount):
        if amount > self.balance:
            print(f"Transfer Failed: {self.owner} has insufficient balance.")
            return self
        print(f"{self.owner} is transferring ₹{amount}...")
        new_balance = self.balance - amount
        return TransferAccount(self.owner, new_balance)

    def __add__(self, amount):
        print(f"{self.owner} received ₹{amount}.")
        new_balance = self.balance + amount
        return TransferAccount(self.owner, new_balance)


class UPI:  # Duck Typing
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")

class DebitCard:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Debit Card.")

class NetBanking:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Net Banking.")

def make_payment(payment_method, amount):
    payment_method.pay(amount)


print("\n----Single Inheritance----")
saving = SavingAccount("Akshita", 1000)
saving.withdraw(500)

print("\n----Hierarchical Inheritance----")
curr = CurrentAccount("Ansh", 10000)
curr.withdraw(500)
curr.deposit(1500)
curr.withdraw(500)

print("\n----Multilevel Inheritance----")
salary = SalaryAccount("Rudra", 20000)
salary.credit_salary(25000)
salary.withdraw(1000)

print("\n----Multiple Inheritance----")
general = GeneralAccount("Mohan")
general.verify_kyc("Mohan")
general.deposit(500)
general.withdraw(300)

print("\n----Hybrid Inheritance----")
premium = PremiumSavingAccount("Priya", 5000)
premium.verify_kyc(premium.owner)
premium.deposit(1000)
premium.offer_rewards()

print("\n----Method Overloading----")
loan = LoanAccount()
loan.calculate_interest(10000)
loan.calculate_interest(10000, 12)
loan.calculate_interest(10000, 12, 3)

print("\n----Operator Overloading----")
a1 = TransferAccount("Akshita", 5000)
a2 = TransferAccount("Ansh", 3000)
print(a1)
print(a2)
a1 = a1 - 1500  # Akshita sends ₹1500
a2 = a2 + 1500  # Ansh receives ₹1500
print("\nAfter Transfer :-")
print(a1)
print(a2)

print("\n----Duck Typing----")
make_payment(UPI(), 500)
make_payment(DebitCard(), 1500)
make_payment(NetBanking(), 2000)