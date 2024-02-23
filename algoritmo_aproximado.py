#!/usr/bin/env python3



def hitting_set_greedy(A, B):
    # Se crea un dict con la frecuencia de apariciones de cada jugador en los subconjuntos
    # Se ordena el set de subconjuntos de acuerdo a la suma de las frecuencias de los jugadores, dividido por la cantidad de jugadores en el subconjunto
    # Se ordenan los jugadores de cada subconjunto de acuerdo a su frecuencia
    
    a = list(A)
    x = list(B)
    hitting_set = []
    while len(x) > 0:
        sort_dict = {}

        for s in x: 
            for jugador in s:
                sort_dict[jugador] = sort_dict.get(jugador, 0) + 1
        
        a.sort(key=lambda jugador: sort_dict.get(jugador, 0), reverse=True)

        hitting_set.append(a[0])
        x = [s for s in x if a[0] not in s]        
        a = []
        for _set in x:
            for jugador in _set:
                if jugador not in a:
                    a.append(jugador)
    return hitting_set





