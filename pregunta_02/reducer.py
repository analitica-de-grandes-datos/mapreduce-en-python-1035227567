
import sys

current_purpose = None
max_amount = 0

for line in sys.stdin:
    purpose, amount = line.strip().split('\t')

    amount = int(amount)

    if current_purpose and current_purpose != purpose:
        print(f"{current_purpose}\t{max_amount}")
        max_amount = 0

    if amount > max_amount:
        max_amount = amount

    current_purpose = purpose

if current_purpose:
    print(f"{current_purpose}\t{max_amount}")
