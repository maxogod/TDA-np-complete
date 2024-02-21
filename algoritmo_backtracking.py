#!/usr/bin/env python3


def _hitting_set(sol_parcial, sol_total, restantes):

    if len(sol_parcial) >= len(sol_total) and len(sol_total) > 0: # Lee bien esta linea XD
        return

    if len(restantes) == 0:
        sol_total.clear()
        sol_total.extend(sol_parcial)
        return
    for subset in restantes:
        for jugador in subset:
            sol_parcial.append(jugador)
            nuevos_restantes = [s for s in restantes if jugador not in s]
            # if len(nuevos_restantes) == len(restantes) - 1:
                # _hitting_set(sol, nuevos_restantes)
                # break 
            _hitting_set(sol_parcial, sol_total, nuevos_restantes)
            sol_parcial.remove(jugador) 






def obtener_hitting_set(A,B):
    sol_total = []
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
    _hitting_set([], sol_total, x)
    return sol_total
