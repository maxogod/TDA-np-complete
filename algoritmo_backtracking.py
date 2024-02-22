#!/usr/bin/env python3

import sys
from utils.utils import obtener_conjunto_y_subconjuntos


def obtener_hitting_set(A,B):
    sol_total = []
    _hitting_set_recursivo(B, [], sol_total, 0)
    return sol_total


def _hitting_set_recursivo(B, solucion_parcial, solucion_total, subset_actual):
    
    if len(solucion_parcial) >= len(solucion_total) and len(solucion_total) > 0:
        return False # Por este camino no se puede llegar a una solución mejor (o de menor largo)
    
    if subset_actual == len(B) and verificar(B, solucion_parcial):
        solucion_total[:] = solucion_parcial
        return True # Se llego a una solución válida

    for elem in solucion_parcial:
        if elem in B[subset_actual]: # Salteamos el subset si ya esta hiteado
            return _hitting_set_recursivo(B, solucion_parcial, solucion_total, subset_actual + 1)
    
    for elem in B[subset_actual]:
        
        solucion_parcial.append(elem)
        
        if not _hitting_set_recursivo(B, solucion_parcial, solucion_total, subset_actual + 1):
                solucion_parcial.pop()
                return True # Este camino no minimiza el largo del hitting set, se vuelve uno atras en la recursión
        
        solucion_parcial.pop()
    
    return True


def verificar(B, sol):

    for subconjunto in B:
        hit = False
        for elem in subconjunto:
            if elem in sol:
                hit = True
                break
        if not hit:
            return False
    
    return True


if __name__ == "__main__":
    args = sys.argv
    A, B = obtener_conjunto_y_subconjuntos(args[1])
    ejecucion = obtener_hitting_set(A, B)
    print(f"Jugadores Totales: {len(ejecucion)}\nLista de Jugadores: {ejecucion}")