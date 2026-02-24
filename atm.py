balance = 10000

while True:
    print("\n=== ATM SIMULATOR ===")
    print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        print(f"Current balance: ₹{balance}")
    elif choice == '2':
        amt = float(input("Enter amount to deposit: "))
        if amt > 0:
            balance += amt
            print(f"Deposit successful! New balance: ₹{balance}")
        else:
            print("Invalid amount.")
    elif choice == '3':
        amt = float(input("Enter amount to withdraw: "))
        if amt > balance:
            print("Insufficient funds!")
        elif balance - amt < 500:
            print("Transaction failed. Minimum balance of ₹500 must be maintained.")
        else:
            balance -= amt
            print(f"Withdrawal successful! New balance: ₹{balance}")
    elif choice == '4':
        print("Thank you for banking with us!")
        break
    else:
        print("Invalid choice.")