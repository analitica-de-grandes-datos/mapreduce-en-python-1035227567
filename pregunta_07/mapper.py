
import sys

for line in sys.stdin:
    line = line.strip()
    columns = line.split()
    if len(columns) >= 3:
        letter = columns[0]
        value = columns[2]
        print(f'{letter}\t{value}\t{line}')
