
import sys

current_key = None

for line in sys.stdin:
    key, value = line.strip().split('\t', 1)
    
    if current_key and current_key != key:
        print(current_value)
    
    current_key = key
    current_value = value

if current_key:
    print(current_value)
