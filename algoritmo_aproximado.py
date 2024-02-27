#!/usr/bin/env python3

import sys
from utils.utils import obtener_conjunto_y_subconjuntos

# Esto es lo que se tiene que buscar minimizar en cada paso segun el K&T, 11.3
def calcular_coeficiente(subconjuntos):
    pesos = {}
    suma_largos_subconjuntos = 0
    for subconjunto in subconjuntos:
        for jugador in subconjunto:
            pesos[jugador] = pesos.get(jugador, 0) + 1
        suma_largos_subconjuntos += len(subconjunto)
        
        
    for jugador in pesos.keys():
        pesos[jugador] = 1 / (pesos[jugador] * suma_largos_subconjuntos)
   
    return pesos

def hitting_set_greedy(A, B):
    hitting_set = []
    while B:
        pesos = calcular_coeficiente(B)

        a = [jugador for jugador in pesos.keys()]
        a.sort(key=lambda jugador: pesos.get(jugador, 0))

        hitting_set.append(a[0])

        B = [s for s in B if a[0] not in s]        

        pesos.pop(a[0], None)
        
    return hitting_set


if __name__ == "__main__":
    args = sys.argv
    A, B = obtener_conjunto_y_subconjuntos(args[1])
    ejecucion = hitting_set_greedy(A, B)
    print(f"Jugadores Totales: {len(ejecucion)}\nLista de Jugadores: {ejecucion}")
