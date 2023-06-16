
import sys

for line in sys.stdin:
    line = line.strip()
    columns = line.split()
    if len(columns) >= 3:
        letter = columns[0]
        value = int(columns[2])
        print(f'{letter}\t{value}\t1')  # Emitir la letra, el valor y un contador para el reducer
