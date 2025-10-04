initial=float(input("Enter the initial amount: "))
deposit=float(input("Enter the deposit amount: "))
print("Initial amount:",initial)
print("Deposit amount:",deposit)
balance = initial + deposit
print(f"Updated balance after deposit: ₹{balance:.2f}")