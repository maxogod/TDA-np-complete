#!/usr/bin/env python3

import sys
from utils.utils import obtener_conjunto_y_subconjuntos

# Esto es lo que se tiene que buscar minimizar en cada paso segun el K&T, 11.3
def calcular_coeficiente(subconjuntos):
    pesos = {}
    for subconjunto in subconjuntos:
        for jugador in subconjunto:
            if jugador not in pesos:
                pesos[jugador] = (0, 0)
            pesos[jugador] = (pesos[jugador][0] + 1, pesos[jugador][1] + len(subconjunto))
        
    for jugador in pesos.keys():
        pesos[jugador] = 1 / (pesos[jugador][0] * pesos[jugador][1])
   
    return pesos

def hitting_set_greedy(B):
    hitting_set = []
    while B:
        pesos = calcular_coeficiente(B)
        print(pesos)
        a = [jugador for jugador in pesos.keys()]
        a.sort(key=lambda jugador: pesos.get(jugador, 0))

        hitting_set.append(a[0])

        B = [s for s in B if a[0] not in s]        

        pesos.pop(a[0], None)
        
    return hitting_set


if __name__ == "__main__":
    args = sys.argv
    A, B = obtener_conjunto_y_subconjuntos(args[1])
    ejecucion = hitting_set_greedy(B)
    print(f"Jugadores Totales: {len(ejecucion)}\nLista de Jugadores: {ejecucion}")
