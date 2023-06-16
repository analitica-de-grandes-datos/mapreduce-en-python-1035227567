
import sys

for line in sys.stdin:
    fields = line.strip().split()
    if len(fields) >= 3:
        letter = fields[0]
        date = fields[1]
        value = float(fields[2])  
        print(f"{letter}\t{date}\t{value}")
