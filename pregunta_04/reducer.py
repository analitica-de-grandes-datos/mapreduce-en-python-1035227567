
import sys

current_key = None
current_count = 0

for line in sys.stdin:
    key, value = line.strip().split(',')

    if current_key is None:
        current_key = key
        current_count += 1
    elif current_key == key:
        current_count += 1
    else:
        print(f"{current_key},{current_count}")
        
        current_key = key
        current_count = 1

if current_key is not None:
    print(f"{current_key},{current_count}")
