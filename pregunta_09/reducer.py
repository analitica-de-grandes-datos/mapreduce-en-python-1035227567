
import sys

records = []

for line in sys.stdin:
    fields = line.strip().split()

    value = int(fields[0])
    record = fields[1:]

    records.append((value, record))

    if len(records) > 6:
        records.remove(max(records))

records.sort()

for record in records:
    output = "   ".join(record[1]) + "\t"
    print(output)
