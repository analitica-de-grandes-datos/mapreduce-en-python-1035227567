
import sys

current_letter = None
current_values = []

def emit_values(values):
    values.sort(key=lambda x: int(x.split()[2]))  # Ordenar por el valor (3ra columna)
    for value in values:
        print(value)

for line in sys.stdin:
    line = line.strip()
    letter, value, data = line.split('\t')

    if current_letter is None:
        current_letter = letter

    if letter == current_letter:
        current_values.append(data)
    else:
        emit_values(current_values)
        current_values = [data]
        current_letter = letter

if current_letter is not None:
    emit_values(current_values)
