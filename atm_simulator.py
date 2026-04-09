initial_balance = 10000
while True:
    print("===========================")
    print("        WELCOME TO ATM")
    print("===========================")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("===========================")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        print(f"Your current balance is ₹{initial_balance:.2f}")
    elif choice == 2:
        deposit_amount = int(input("Enter amount to deposit: "))
        if deposit_amount <= 0:
            print("Invalid amount. Please enter a positive value.")
        else:
            print(f"₹{deposit_amount:.2f} deposited successfully.")
            initial_balance = initial_balance + deposit_amount
            print(f"Your new balance is ₹{initial_balance:.2f}")
    elif choice == 3:
        withdrawal_amount = int(input("Enter amount to withdraw: "))
        if withdrawal_amount <= 0 :
            print("Invalid amount. Please enter a positive value.")
        elif withdrawal_amount > initial_balance:
            print(f"Insufficient funds. Your balance is ₹{initial_balance:.2f}")
        else:
            print(f"₹{withdrawal_amount:.2f} withdrawn successfully.")
            initial_balance = initial_balance - withdrawal_amount
            print(f"Your new balance is ₹{initial_balance:.2f}")
    elif choice ==4:
        print("Thank you for using our ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")
