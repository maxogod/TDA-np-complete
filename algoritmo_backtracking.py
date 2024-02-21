#!/usr/bin/env python3


def _hitting_set(sol_parcial, sol_total, restantes):

    if len(sol_parcial) >= len(sol_total) and len(sol_total) > 0:
        return

    if not restantes:
        sol_total[:] = sol_parcial[:]
        return
    
    for subset in restantes:
        for jugador in subset:
            sol_parcial.append(jugador)
            nuevos_restantes = [s for s in restantes if jugador not in s]
            _hitting_set(sol_parcial, sol_total, nuevos_restantes)
            sol_parcial.remove(jugador) 


def obtener_hitting_set(A,B):
    sol_total = []
    _hitting_set([], sol_total, B)
    return sol_total
