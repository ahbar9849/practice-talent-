from bank import BankAccount


account1 = BankAccount(
    "Ahbar",
    "10001",
    "1234",
    10000
)


while True:

    print("\n========== MY BANK ==========")

    print("1. Account Details")
    print("2. Check Balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")

    try:

        choice = int(input("Enter your choice: "))

        if choice == 1:

            account1.display_details()

        elif choice == 2:

            account1.check_balance()

        elif choice == 3:

            amount = float(input("Enter deposit amount: "))

            account1.deposit(amount)

        elif choice == 4:

            amount = float(input("Enter withdrawal amount: "))

            account1.withdraw(amount)

        elif choice == 5:

            print("Thank you for banking with us!")
            break

        else:

            print("Invalid choice!")

    except ValueError:

        print("Please enter a valid number!")

    except KeyboardInterrupt:

        print("\nApplication interrupted!")
        break

    finally:

        print("Banking operation completed.")