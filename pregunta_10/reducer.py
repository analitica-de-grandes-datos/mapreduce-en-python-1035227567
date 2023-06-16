
import sys

current_letter = None
numbers = []

for line in sys.stdin:
    letter, number = line.strip().split('\t')
    
    if current_letter is None:
        current_letter = letter
        numbers = [number]
    elif letter == current_letter:
        numbers.append(number)
    else:
        numbers.sort(key=int)
        
        numbers_str = ','.join(numbers)
        print(f'{current_letter}\t{numbers_str}')
        
        current_letter = letter
        numbers = [number]

if current_letter is not None:
    numbers.sort(key=int)
    numbers_str = ','.join(numbers)
    print(f'{current_letter}\t{numbers_str}')
