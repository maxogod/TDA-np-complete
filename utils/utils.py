#!/usr/bin/env python3

def obtener_conjunto_y_subconjuntos(filename):
    conjunto = set()
    subconjuntos = set()

    with open(filename, 'r') as file:
        for line in file:
            subconjunto_actual = set()
            requeridos = line.split(',')
            for requerido in requeridos:
                conjunto.add(requerido.strip('\n'))
                subconjunto_actual.add(requerido.strip('\n'))
            subconjuntos.add(frozenset(subconjunto_actual))

    return conjunto, subconjuntos
