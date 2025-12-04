import logging
import logging.config

logging.config.fileConfig("logging.conf")

# logging.basicConfig(
#     filename="test.log",
#     level=logging.DEBUG,
#     format="%(asctime)s %(name)s: %(levelname)s %(message)s",
#     filemode='w' 
# )

logger = logging.getLogger("atmLogger")

# logging.disable(logging.INFO)


class InvalidPinError(Exception):
    pass


class InsufficientFundsError(Exception):
    pass


class ATM:
    def __init__(self, balance, pin):
        self.balance = balance
        self.pin = pin
        logger.info("ATM initialized with balance $%s", balance)

    def verify_pin(self, entered_pin):
        logger.debug("Verifying PIN...")
        if entered_pin != self.pin:
            logger.error("Invalid PIN entered!")
            raise InvalidPinError("Incorrect PIN")
        logger.info("PIN verified successfully")

    def withdraw(self, amount):
        logger.debug("Attempting withdrawal of $%s", amount)

        if amount > self.balance:
            logger.error("Withdrawal failed: Insufficient balance!")
            raise InsufficientFundsError("Not enough balance")

        self.balance -= amount
        logger.info(
            "Withdrawal of $%s successful. Remaining balance: $%s", amount, self.balance
        )
        return self.balance

    def deposit(self, amount):
        logger.debug("Attempting deposit of $%s", amount)

        if amount <= 0:
            logger.warning("Deposit failed: Invalid amount")
            raise ValueError("Deposit amount must be positive")

        self.balance += amount
        logger.info("Deposit of $%s successful. New balance: $%s", amount, self.balance)
        return self.balance


if __name__ == "__main__":

    atm = ATM(balance=5000, pin=1234)

    try:
        pin = int(input("Enter PIN: "))
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
        logger.error("Authentication failed: %s", e)
        print("Incorrect PIN!")

    except InsufficientFundsError as e:
        logger.error("Transaction failed: %s", e)
        print("Insufficient balance!")

    except Exception as e:
        logger.error("Unexpected error: %s", e)
        print("Something went wrong!")

    else:
        print("Success!")

    finally:
        logger.info("ATM session ended")
        print("\nThank you for using the ATM")
