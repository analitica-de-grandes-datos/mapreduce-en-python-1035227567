
import sys

current_letter = None
min_value = float('inf')
max_value = float('-inf')

for line in sys.stdin:
    letter, date, value = line.strip().split('\t')

    if current_letter is None:
        current_letter = letter
        min_value = float(value)
        max_value = float(value)
    elif current_letter == letter:
        min_value = min(min_value, float(value))
        max_value = max(max_value, float(value))
    else:
        print(f"{current_letter}\t{max_value}\t{min_value}")

        current_letter = letter
        min_value = float(value)
        max_value = float(value)

if current_letter is not None:
    print(f"{current_letter}\t{max_value}\t{min_value}")
