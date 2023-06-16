
import sys

for line in sys.stdin:
    fields = line.strip().split()
    if len(fields) >= 2:
        date = fields[1]
        month = date.split('-')[1]
        print(f"{month}	1")
