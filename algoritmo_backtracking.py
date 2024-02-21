#!/usr/bin/env python3

SOLUCION = []
def _hitting_set(sol, restantes):
    global SOLUCION
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
            _hitting_set(sol, nuevos_restantes)
            sol.remove(jugador)

def obtener_hitting_set(A,B):
    global SOLUCION
    SOLUCION.clear()
    _hitting_set([], B)
    return SOLUCION

