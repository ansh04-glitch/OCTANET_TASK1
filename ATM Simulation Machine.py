class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def authenticate(self, input_pin):
        return self.pin == input_pin

    def balance_inquiry(self):
        return self.balance

    def cash_withdrawal(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount}")
            return f"Withdrew {amount}. New balance: {self.balance}"

    def cash_deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")
        return f"Deposited {amount}. New Balance: {self.balance}"

    def change_pin(self, old_pin, new_pin):
        if self.authenticate(old_pin):
            self.pin = new_pin
            return "PIN Changed Successfully."
        else:
            return "Incorrect old PIN."

    def get_transaction_history(self):
        return self.transactions

def main():
    atm = ATM(pin=1234, balance=1000)

    while True:
        print("\nATM Machine")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. PIN Change")
        print("5. Transaction History")
        print("6. Exit")

        choice = int(input("Choose an option: "))

        if choice == 1:
            pin = int(input("Enter PIN: "))
            if atm.authenticate(pin):
                print(f"Your balance is {atm.balance_inquiry()}")
            else:
                print("Incorrect PIN")

        elif choice == 2:
            pin = int(input("Enter PIN: "))
            if atm.authenticate(pin):
                amount = float(input("Enter Amount To Withdraw: "))
                print(atm.cash_withdrawal(amount))
            else:
                print("Incorrect PIN")

        elif choice == 3:
            pin = int(input("Enter PIN: "))
            if atm.authenticate(pin):
                amount = float(input("Enter Amount To Deposit: "))
                print(atm.cash_deposit(amount))
            else:
                print("Incorrect PIN")

        elif choice == 4:
            old_pin = int(input("Enter Old PIN: "))
            new_pin = int(input("Enter New PIN: "))
            print(atm.change_pin(old_pin, new_pin))

        elif choice == 5:
            pin = int(input("Enter PIN: "))
            if atm.authenticate(pin):
                print("Transaction History:")
                for transaction in atm.get_transaction_history():
                    print(transaction)
            else:
                print("Incorrect PIN")

        elif choice == 6:
            print("Thank you for using the ATM. Come Soon !!")
            break

        else:
            print("Invalid option !!, Please Try Again.")

if __name__ == "__main__":
    main()
