class BankAccount:

    def __init__(self, name, account_number, pin, balance=0):

        self.name = name
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def display_details(self):

        print("\n------ ACCOUNT DETAILS ------")

        print("Name:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

    def check_balance(self):

        print("Available Balance:", self.balance)

    def deposit(self, amount):

        if amount <= 0:
            print("Invalid deposit amount!")

        else:
            self.balance += amount
            print("Deposit successful!")
            print("New Balance:", self.balance)

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid withdrawal amount!")

        elif amount > self.balance:
            print("Insufficient balance!")

        else:
            self.balance -= amount
            print("Withdrawal successful!")
            print("Remaining Balance:", self.balance)