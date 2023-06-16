
import sys

for line in sys.stdin:
    fields = line.strip().split()

    value = int(fields[2])

    print(f"{value}   {line.strip()}")
