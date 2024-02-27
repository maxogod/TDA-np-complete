#!/usr/bin/env python3

import unittest
from utils.utils import obtener_conjunto_y_subconjuntos
from algoritmo_backtracking import obtener_hitting_set
from algoritmo_aproximado import hitting_set_greedy
import math

def calcular_pesos(subconjuntos):
    pesos = {}
    for subconjunto in subconjuntos:
        for jugador in subconjunto:
            pesos[jugador] = pesos.get(jugador, 0) + 1
    return pesos

class UnitTests(unittest.TestCase):
    def guardar_resultados(self, resultado):
        # Nombre del archivo para guardar los resultados
        archivo_resultados = "resultados.txt"
        # Se abre el archivo en modo append (añadir al final)
        with open(archivo_resultados, "w") as archivo:
            # Se escribe el nombre del test y su resultado
            archivo.write(f"Test: {self._testMethodName}\n")
            archivo.write(f"{resultado}\n\n")

    def test_5_subconjuntos(self):
        file = './archivos_prueba/5.txt'
        res = 2

        conjunto, subconjuntos = obtener_conjunto_y_subconjuntos(file)
        ejecucion = obtener_hitting_set(conjunto, subconjuntos)
        ejecucion_greedy = hitting_set_greedy(conjunto, subconjuntos)

        pesos = calcular_pesos(subconjuntos)
        peso_optimo = sum([pesos[jugador] for jugador in ejecucion])
        peso_greedy = sum([pesos[jugador] for jugador in ejecucion_greedy])

        self.guardar_resultados((len(ejecucion),len(ejecucion_greedy)))
        self.assertGreaterEqual(len(ejecucion_greedy), res)
        self.assertGreaterEqual(math.log(len(conjunto)) * peso_optimo, peso_greedy)
        self.assertEqual(res, len(ejecucion))

    def test_7_subconjuntos(self):
        file = './archivos_prueba/7.txt'
        res = 2

        conjunto, subconjuntos = obtener_conjunto_y_subconjuntos(file)
        ejecucion = obtener_hitting_set(conjunto, subconjuntos)
        ejecucion_greedy = hitting_set_greedy(conjunto, subconjuntos)

        pesos = calcular_pesos(subconjuntos)
        peso_optimo = sum([pesos[jugador] for jugador in ejecucion])
        peso_greedy = sum([pesos[jugador] for jugador in ejecucion_greedy])

        self.guardar_resultados((len(ejecucion),len(ejecucion_greedy)))
        self.assertGreaterEqual(math.log(len(conjunto)) * peso_optimo, peso_greedy)
        self.assertEqual(res, len(ejecucion))

    def test_10_pocos_subconjuntos(self):
        file = './archivos_prueba/10_pocos.txt'
        res = 3

        conjunto, subconjuntos = obtener_conjunto_y_subconjuntos(file)
        ejecucion = obtener_hitting_set(conjunto, subconjuntos)
        ejecucion_greedy = hitting_set_greedy(conjunto, subconjuntos)

        pesos = calcular_pesos(subconjuntos)
        peso_optimo = sum([pesos[jugador] for jugador in ejecucion])
        peso_greedy = sum([pesos[jugador] for jugador in ejecucion_greedy])
        
        self.guardar_resultados((len(ejecucion),len(ejecucion_greedy)))
        
        self.assertGreaterEqual(math.log(len(conjunto)) * peso_optimo, peso_greedy)

        self.assertEqual(res, len(ejecucion))

    def test_10_todos_subconjuntos(self):
        file = './archivos_prueba/10_todos.txt'
        res = 10

        conjunto, subconjuntos = obtener_conjunto_y_subconjuntos(file)
        ejecucion = obtener_hitting_set(conjunto, subconjuntos)
        ejecucion_greedy = hitting_set_greedy(conjunto, subconjuntos)

        pesos = calcular_pesos(subconjuntos)
        peso_optimo = sum([pesos[jugador] for jugador in ejecucion])
        peso_greedy = sum([pesos[jugador] for jugador in ejecucion_greedy])
        
        self.guardar_resultados((len(ejecucion),len(ejecucion_greedy)))
        
        self.assertGreaterEqual(math.log(len(conjunto)) * peso_optimo, peso_greedy)
        self.assertEqual(res, len(ejecucion))



    def test_10_varios_subconjuntos(self):
        file = './archivos_prueba/10_varios.txt'
        res = 6

        conjunto, subconjuntos = obtener_conjunto_y_subconjuntos(file)
        ejecucion = obtener_hitting_set(conjunto, subconjuntos)
        ejecucion_greedy = hitting_set_greedy(conjunto, subconjuntos)

        pesos = calcular_pesos(subconjuntos)
        peso_optimo = sum([pesos[jugador] for jugador in ejecucion])
        peso_greedy = sum([pesos[jugador] for jugador in ejecucion_greedy])
        
        self.guardar_resultados((len(ejecucion),len(ejecucion_greedy)))
        
        self.assertGreaterEqual(math.log(len(conjunto)) * peso_optimo, peso_greedy)
        self.assertEqual(res, len(ejecucion))

    def test_15_subconjuntos(self):
        file = './archivos_prueba/15.txt'
        res = 4

        conjunto, subconjuntos = obtener_conjunto_y_subconjuntos(file)
        ejecucion = obtener_hitting_set(conjunto, subconjuntos)
        ejecucion_greedy = hitting_set_greedy(conjunto, subconjuntos)

        pesos = calcular_pesos(subconjuntos)
        peso_optimo = sum([pesos[jugador] for jugador in ejecucion])
        peso_greedy = sum([pesos[jugador] for jugador in ejecucion_greedy])
        self.guardar_resultados((len(ejecucion),len(ejecucion_greedy)))
        
        self.assertGreaterEqual(math.log(len(conjunto)) * peso_optimo, peso_greedy)
        self.assertEqual(res, len(ejecucion))


    def test_20_subconjuntos(self):
        file = './archivos_prueba/20.txt'
        res = 5

        conjunto, subconjuntos = obtener_conjunto_y_subconjuntos(file)
        ejecucion = obtener_hitting_set(conjunto, subconjuntos)
        ejecucion_greedy = hitting_set_greedy(conjunto, subconjuntos)

        pesos = calcular_pesos(subconjuntos)
        peso_optimo = sum([pesos[jugador] for jugador in ejecucion])
        peso_greedy = sum([pesos[jugador] for jugador in ejecucion_greedy])
        self.guardar_resultados((len(ejecucion),len(ejecucion_greedy)))
        
        self.assertGreaterEqual(math.log(len(conjunto)) * peso_optimo, peso_greedy)
        self.assertEqual(res, len(ejecucion))


    def test_50_subconjuntos(self):
        file = './archivos_prueba/50.txt'
        res = 6

        conjunto, subconjuntos = obtener_conjunto_y_subconjuntos(file)
        ejecucion = obtener_hitting_set(conjunto, subconjuntos)
        ejecucion_greedy = hitting_set_greedy(conjunto, subconjuntos)

        pesos = calcular_pesos(subconjuntos)
        peso_optimo = sum([pesos[jugador] for jugador in ejecucion])
        peso_greedy = sum([pesos[jugador] for jugador in ejecucion_greedy])
        self.guardar_resultados((len(ejecucion),len(ejecucion_greedy)))
        
        self.assertGreaterEqual(math.log(len(conjunto)) * peso_optimo, peso_greedy)
        self.assertEqual(res, len(ejecucion))

    def test_75_subconjuntos(self):
        file = './archivos_prueba/75.txt'
        res = 8

        conjunto, subconjuntos = obtener_conjunto_y_subconjuntos(file)
        ejecucion = obtener_hitting_set(conjunto, subconjuntos)
        ejecucion_greedy = hitting_set_greedy(conjunto, subconjuntos)

        pesos = calcular_pesos(subconjuntos)
        peso_optimo = sum([pesos[jugador] for jugador in ejecucion])
        peso_greedy = sum([pesos[jugador] for jugador in ejecucion_greedy])
        self.guardar_resultados((len(ejecucion),len(ejecucion_greedy)))
        
        self.assertGreaterEqual(math.log(len(conjunto)) * peso_optimo, peso_greedy)
        self.assertEqual(res, len(ejecucion))

    def test_100_subconjuntos(self):
        file = './archivos_prueba/100.txt'
        res = 9

        conjunto, subconjuntos = obtener_conjunto_y_subconjuntos(file)
        ejecucion = obtener_hitting_set(conjunto, subconjuntos)
        ejecucion_greedy = hitting_set_greedy(conjunto, subconjuntos)

        pesos = calcular_pesos(subconjuntos)
        peso_optimo = sum([pesos[jugador] for jugador in ejecucion])
        peso_greedy = sum([pesos[jugador] for jugador in ejecucion_greedy])
        self.guardar_resultados((len(ejecucion),len(ejecucion_greedy)))
        
        self.assertGreaterEqual(math.log(len(conjunto)) * peso_optimo, peso_greedy)
        self.assertEqual(res, len(ejecucion))

    def test_200_subconjuntos(self):
        file = './archivos_prueba/200.txt'
        res = 9

        conjunto, subconjuntos = obtener_conjunto_y_subconjuntos(file)
        ejecucion = obtener_hitting_set(conjunto, subconjuntos)
        ejecucion_greedy = hitting_set_greedy(conjunto, subconjuntos)

        pesos = calcular_pesos(subconjuntos)
        peso_optimo = sum([pesos[jugador] for jugador in ejecucion])
        peso_greedy = sum([pesos[jugador] for jugador in ejecucion_greedy])
        self.guardar_resultados((len(ejecucion),len(ejecucion_greedy)))
        
        self.assertGreaterEqual(math.log(len(conjunto)) * peso_optimo, peso_greedy)
        self.assertEqual(res, len(ejecucion))


if __name__ == '__main__':
    unittest.main()
