
import sys

current_month = None
current_count = 0

for line in sys.stdin:
    month, value = line.strip().split('	')

    if current_month is None:
        current_month = month
        current_count += 1
    elif current_month == month:
        current_count += 1
    else:
        print(f"{current_month}	{current_count}")

        current_month = month
        current_count = 1

if current_month is not None:
    print(f"{current_month}	{current_count}")
