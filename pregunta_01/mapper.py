

import sys

for linea in sys.stdin:
    atributos = linea.strip().split(',')

    if len(atributos) == 21:
        credit_history = atributos[2]

        print(f'{credit_history}\t1')
