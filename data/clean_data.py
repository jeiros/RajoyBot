#!/usr/bin/env python3

from glob import glob
import sys


#files = sorted(glob('./20*txt'))


file1 = sys.argv[1]

dias = ('lunes,', 'martes,', 'miércoles,', 'jueves,', 'viernes,', 'sabado,', 'sábado', 'domingo,')

with open(file1) as f:
    for line in f:
        if ('Pagina' not in line and not line.startswith(dias)) and (not line.startswith('Mensajes en twitter de Mariano Rajoy Brey') and not line.startswith('RT ')):
            print(line.strip())
