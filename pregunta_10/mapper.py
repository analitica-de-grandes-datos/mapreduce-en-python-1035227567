
import sys

for line in sys.stdin:
    number, letters = line.strip().split('\t')
    
    letters = letters.split(',')
    
    for letter in letters:
        print(f'{letter}\t{number}')
