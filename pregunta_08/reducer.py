
import sys

current_letter = None
sum_value = 0
count = 0

for line in sys.stdin:
    line = line.strip()
    letter, value, cnt = line.split('\t')

    if current_letter is None:
        current_letter = letter

    if letter == current_letter:
        sum_value += float(value)
        count += float(cnt)
    else:
        if current_letter:
            average = sum_value / count
            print(f'{current_letter}\t{sum_value}\t{average}')
        current_letter = letter
        sum_value = float(value)
        count = float(cnt)

if current_letter is not None:
    average = sum_value / count
    print(f'{current_letter}\t{sum_value}\t{average}')
