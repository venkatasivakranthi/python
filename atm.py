
# ATM Transaction Sequence Simulation

balance = float(input("Enter initial balance: Rs. "))
max_withdrawal = 10000
transactions = []
total_deposits = 0
total_withdrawals = 0
rejected = 0

if balance < 0:
    print("Invalid initial balance!")

else:
    n = int(input("Enter number of transactions: "))

    for i in range(n):
        print("\n1. Deposit")
        print("2. Withdraw")

        choice = input("Enter transaction type (1/2): ")
        amount = float(input("Enter amount: Rs. "))

        if amount <= 0:
            print("Rejected: Invalid amount.")
            rejected += 1
            transactions
