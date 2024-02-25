#!/usr/bin/env python3


# Esto es lo que se tiene que buscar minimizar en cada paso segun el K&T, 11.3
def calcular_pesos(subconjuntos):
    pesos = {}
    for subconjunto in subconjuntos:
        for jugador in subconjunto:
            pesos[jugador] = pesos.get(jugador, 0) + 1

    for jugador in pesos.keys():
        for subconjunto in subconjuntos:
            if jugador in subconjunto:
                pesos[jugador] = 1 / pesos[jugador] * len(subconjunto)        
    return pesos

def hitting_set_greedy(A, B):
    a = list(A)
    x = list(B)
    pesos = calcular_pesos(x)
    a.sort(key=lambda jugador: pesos.get(jugador, 0))
    hitting_set = []
    while len(x) > 0:
        hitting_set.append(a[0])
        subsets = [s for s in subsets if a[0] not in s]        
        a = []
        for subset in subsets:
            for jugador in subset:
                if jugador not in a:
                    a.append(jugador)
                    
    return hitting_set
