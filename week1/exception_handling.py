class InsufficientFundsError(Exception):  # User defined Exception
    pass


class InvalidPinError(Exception):
    pass


class ATM:
    def __init__(self, balance, pin):
        self.balance = balance
        self.pin = pin

    def verify_pin(self, user_pin):
        if user_pin != self.pin:
            raise InvalidPinError("Incorrect PIN entered!")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Not enough balance to withdraw!")
        self.balance -= amount
        return f"${amount} withdrawn successfully. Remaining balance: ${self.balance}"

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive!")
        self.balance += amount
        return f"${amount} deposited successfully. Total balance: ${self.balance}"


if __name__ == "__main__":
    atm = ATM(balance=5000, pin=1234)

    try:
        pin = int(input("Enter your ATM PIN: "))
        atm.verify_pin(pin)

        while True:
            print("\n1. Withdraw")
            print("2. Deposit")

            choice = int(input("Choose an option: "))

            if choice == 1:
                amount = int(input("Enter amount to withdraw: "))
                print(atm.withdraw(amount))

            elif choice == 2:
                amount = int(input("Enter amount to deposit: "))
                print(atm.deposit(amount))

            else:
                print("Invalid choice!")
                break

    except InvalidPinError as e:
        print("PIN Error:", e)

    except InsufficientFundsError as e:
        print("Balance Error:", e)

    except ValueError as e:
        print("Input Error:", e)

    except Exception as e:
        print("Something went wrong:", e)

    else:
        print("Success!")

    finally:
        print("\nThank you for using the ATM")
