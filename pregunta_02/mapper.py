
import sys

for line in sys.stdin:
    fields = line.strip().split(',')

    amount = int(fields[4])  
    purpose = fields[3]  

    print(f"{purpose}\t{amount}")
