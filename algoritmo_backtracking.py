#!/usr/bin/env python3

SOLUCION = []
def _hitting_set(sol, restantes):
    global SOLUCION
    print(f'Considerando {sol}')
    if len(SOLUCION) > 0 and len(sol) >= len(SOLUCION):
        return
    if len(restantes) == 0 and len(SOLUCION) == 0:
        SOLUCION = sol.copy()
        return
    if len(restantes) == 0 and len(sol) < len(SOLUCION):
        SOLUCION = sol.copy()
        return
    if len(restantes) == 0:
        return
    for subset in restantes:
        for jugador in subset:
            sol.append(jugador)
            nuevos_restantes = [s for s in restantes if jugador not in s]
            # if len(nuevos_restantes) == len(restantes) - 1:
                # _hitting_set(sol, nuevos_restantes)
                # break 
            _hitting_set(sol, nuevos_restantes)
            sol.remove(jugador) 






def obtener_hitting_set(A,B):
    global SOLUCION
    SOLUCION.clear()
    print(f'B:{B}')
    print('-'*50)
    sort_dict = {}
    for s in B:
        for jugador in s:
            if jugador in sort_dict:
                sort_dict[jugador] += 1
            else:
                sort_dict[jugador] = 1
    print(f'Sort_dict:{sort_dict}')
    print('-'*50)

    x = sorted(B, key=lambda subset: sum(sort_dict[jugador] for jugador in subset)/len(subset), reverse=True)
    print(f'X:{x}')
    print('-'*50)
    _hitting_set([], x)
    return SOLUCION

