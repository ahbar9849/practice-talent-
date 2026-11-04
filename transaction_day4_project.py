
# ==========================================
# TRANSACTION PROCESSOR
# ==========================================

# Step 1: Transaction data
transactions = [
    1000,
    25000,
    -500,
    75000,
    0,
    45000,
    120000,
    3000,
    80000
]

# Step 2: Initialize counters
successful_transactions = 0
invalid_transactions = 0
high_value_transactions = []

print("=" * 45)
print("       BANK TRANSACTION PROCESSOR")
print("=" * 45)

# Step 3: Process transactions
for amount in transactions:

    print(f"\nProcessing transaction: {amount}")

    # Rule 1: Stop processing at 1 lakh or above
    if amount >= 100000:
        print("STOP: Transaction limit reached!")
        break

    # Rule 2: Skip invalid transactions
    if amount <= 0:
        print("INVALID: Skipping transaction")
        invalid_transactions += 1
        continue

    # Rule 3: Count successful transactions
    successful_transactions += 1
    print("SUCCESS: Transaction processed")

    # Rule 4: Identify high-value transactions
    if amount > 50000:
        high_value_transactions.append(amount)
        print("HIGH VALUE TRANSACTION DETECTED!")

# Step 4: Generate summary
print("\n" + "=" * 45)
print("          TRANSACTION SUMMARY")
print("=" * 45)

print("Successful transactions:", successful_transactions)
print("Invalid transactions:", invalid_transactions)
print("High-value transactions:", high_value_transactions)
print("Total high-value transactions:", len(high_value_transactions))

print("=" * 45)
