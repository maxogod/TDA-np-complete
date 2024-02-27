#!/usr/bin/env python3

import sys
from utils.utils import obtener_conjunto_y_subconjuntos

# Esto es lo que se tiene que buscar minimizar en cada paso segun el K&T, 11.3
def calcular_coeficiente(subconjuntos):
    pesos = {}
    for subconjunto in subconjuntos:
        for jugador in subconjunto:
            if jugador not in pesos:
                pesos[jugador] = {'frecuencia': 0, 'largo_total': 0}
            pesos[jugador]['frecuencia'] += 1
            pesos[jugador]['largo_total'] += len(subconjunto)
        
    for jugador in pesos.keys():
        pesos[jugador] = 1 / (pesos[jugador]['frecuencia'] * pesos[jugador]['largo_total'])
   
    return pesos

def hitting_set_greedy(A, B):
    a = list(A)
    hitting_set = []
    pesos = calcular_coeficiente(B)
    a.sort(key=lambda jugador: pesos.get(jugador, 0))
    while len(B) > 0:
        hitting_set.append(a[0])
        
        B = [s for s in B if a[0] not in s]        
        pesos.pop(a[0], None)
        pesos = calcular_coeficiente(B) # Esto ya itera sobre los subsets, por lo que si algo no existe en B, no se agrega a a
        a = [jugador for jugador in pesos.keys()]
        a.sort(key=lambda jugador: pesos.get(jugador, 0))
        
    return hitting_set


if __name__ == "__main__":
    args = sys.argv
    A, B = obtener_conjunto_y_subconjuntos(args[1])
    ejecucion = hitting_set_greedy(A, B)
    print(f"Jugadores Totales: {len(ejecucion)}\nLista de Jugadores: {ejecucion}")

