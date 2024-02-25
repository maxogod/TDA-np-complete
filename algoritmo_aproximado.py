#!/usr/bin/env python3


# Esto es lo que se tiene que buscar minimizar en cada paso segun el K&T, 11.3
def calcular_pesos(subconjuntos):
    pesos = {}
    for subconjunto in subconjuntos:
        for jugador in subconjunto:
            pesos[jugador] = pesos.get(jugador, 0) + 1 / len(subconjunto)
    return pesos

def hitting_set_greedy(A, B):
    a = list(A)
    pesos = calcular_pesos(B)
    a.sort(key=lambda jugador: pesos.get(jugador, 0))
    hitting_set = []
    while len(B) > 0:
        hitting_set.append(a[0])
        B = [s for s in B if a[0] not in s]        
        a = []
        for _set in B:
            for jugador in _set:
                if jugador not in a:
                    a.append(jugador)
    return hitting_set





