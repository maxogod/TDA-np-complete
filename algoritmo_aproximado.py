#!/usr/bin/env python3


def hitting_set_greedy(B):
    # Se crea un dict con la frecuencia de apariciones de cada jugador en los subconjuntos
    sort_dict = {}
    for s in B: 
        for jugador in s:
            sort_dict[jugador] = sort_dict.get(jugador, 0) + 1
            
    # Se ordena el set de subconjuntos de acuerdo a la suma de las frecuencias de los jugadores, dividido por la cantidad de jugadores en el subconjunto
    x = sorted(B, key=lambda subset: sum(sort_dict[jugador] for jugador in subset)/len(subset), reverse=True) 
    
    # Se ordenan los jugadores de cada subconjunto de acuerdo a su frecuencia
    for i, subs in enumerate(x): 
        x[i] = sorted(subs, key=lambda jugador: sort_dict[jugador], reverse=True)

    hitting_set = []
    while len(x) > 0:
        hitting_set.append(x[0][0])
        x = [s for s in x if x[0][0] not in s]        

    return hitting_set