correct_pin = "1234"
balance = 50000
attempts = 0
pin_correct = False

# PIN code verification loop (Maximum 3 attempts)
while attempts < 3:
    pin = input("Enter your PIN code: ")

    if pin == correct_pin:
        pin_correct = True
        break
    else:
        attempts += 1
        print(f"Incorrect PIN. Attempts remaining: {3 - attempts}")
        
if not pin_correct:
    print("Your card has been blocked. Please contact the bank.")
else:
    # Main ATM Menu Loop
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            print(f"Your current balance is: {balance} AMD")

        elif choice == "2":
            # Safety check: Prevent program crash if the user enters letters instead of numbers
            try:
                amount = int(input("Enter the amount to withdraw: "))
                
                if amount > balance:
                    print("Insufficient funds on your account.")
                elif amount <= 0:
                    print("Invalid amount. Please enter a positive number.")
                else:
                    balance -= amount
                    print(f"Successfully withdrew {amount} AMD. Remaining balance: {balance} AMD")
            
            except ValueError:
                print("Error: Please enter numbers only.")

        elif choice == "3":
            print("Exiting system. Thank you for using our ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
