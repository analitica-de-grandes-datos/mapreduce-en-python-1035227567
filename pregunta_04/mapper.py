

import sys

for line in sys.stdin:
    fields = line.strip().split()
    if len(fields) >= 1:
        key = fields[0]
        print(f"{key},1")
