

import sys

counts = {}

for linea in sys.stdin:
    key, value = linea.strip().split('\t')

    if key in counts:
        counts[key] += int(value)
    else:
        counts[key] = int(value)

sorted_counts = sorted(counts.items())

for key, count in sorted_counts:
    print(f'{key}\t{count}')