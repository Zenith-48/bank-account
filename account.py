initial=float(input("Enter the initial amount: "))
deposit=float(input("Enter the deposit amount: "))
print("Initial amount:",initial)
print("Deposit amount:",deposit)
balance = initial + deposit
print(f"Updated balance after deposit: ₹{balance:.2f}")
withdraw_amount = float(input("Enter the amount to withdraw: "))

if withdraw_amount <= balance:
    balance -= withdraw_amount
    print(f"Withdrawal successful! New balance: ₹{balance:.2f}")
else:
    print("Insufficient balance!")