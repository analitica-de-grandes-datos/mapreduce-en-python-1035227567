
import sys

for line in sys.stdin:
    columns = line.strip().split(',')
    
    if len(columns) >= 2:
        key = columns[1]
        value = line.strip()
        print(f'{key}\t{value}')
