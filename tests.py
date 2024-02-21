#!/usr/bin/env python3

import unittest
from utils.utils import obtener_conjunto_y_subconjuntos
from algoritmo_backtracking import obtener_hitting_set


class UnitTests(unittest.TestCase):
    def test_5_subconjuntos(self):
        file = './archivos_prueba/5.txt'
        res = 2

        conjunto, subconjuntos = obtener_conjunto_y_subconjuntos(file)
        ejecucion = obtener_hitting_set(conjunto, subconjuntos)
        print(f"Ejecucion devuelve: {ejecucion}")
        self.assertEqual(res, len(ejecucion))

    def test_7_subconjuntos(self):
        file = './archivos_prueba/7.txt'
        res = 2

        conjunto, subconjuntos = obtener_conjunto_y_subconjuntos(file)
        ejecucion = obtener_hitting_set(conjunto, subconjuntos)
        self.assertEqual(res, len(ejecucion))

    def test_10_pocos_subconjuntos(self):
        file = './archivos_prueba/10_pocos.txt'
        res = 3

        conjunto, subconjuntos = obtener_conjunto_y_subconjuntos(file)
        ejecucion = obtener_hitting_set(conjunto, subconjuntos)
        self.assertEqual(res, len(ejecucion))

    # def test_10_todos_subconjuntos(self):
    #     file = './archivos_prueba/10_todos.txt'
    #     res = 10

    #     conjunto, subconjuntos = obtener_conjunto_y_subconjuntos(file)
    #     ejecucion = obtener_hitting_set(conjunto, subconjuntos)
    #     print(ejecucion)
    #     self.assertEqual(res, len(ejecucion))

    # def test_10_varios_subconjuntos(self):
    #     file = './archivos_prueba/10_varios.txt'
    #     res = 6

    #     conjunto, subconjuntos = obtener_conjunto_y_subconjuntos(file)
    #     ejecucion = obtener_hitting_set(conjunto, subconjuntos)

    #     self.assertEqual(res, len(ejecucion))

    def test_15_subconjuntos(self):
        file = './archivos_prueba/15.txt'
        res = 4

        conjunto, subconjuntos = obtener_conjunto_y_subconjuntos(file)
        ejecucion = obtener_hitting_set(conjunto, subconjuntos)

        self.assertEqual(res, len(ejecucion))

    # def test_20_subconjuntos(self):
    #     file = './archivos_prueba/20.txt'
    #     res = 5

    #     conjunto, subconjuntos = obtener_conjunto_y_subconjuntos(file)
    #     ejecucion = obtener_hitting_set(conjunto, subconjuntos)

    #     self.assertEqual(res, len(ejecucion))

    # def test_50_subconjuntos(self):
    #     file = './archivos_prueba/50.txt'
    #     res = 6

    #     conjunto, subconjuntos = obtener_conjunto_y_subconjuntos(file)
    #     ejecucion = obtener_hitting_set(conjunto, subconjuntos)

    #     self.assertEqual(res, len(ejecucion))

    # def test_75_subconjuntos(self):
    #     file = './archivos_prueba/75.txt'
    #     res = 8

    #     conjunto, subconjuntos = obtener_conjunto_y_subconjuntos(file)
    #     ejecucion = obtener_hitting_set(conjunto, subconjuntos)

    #     self.assertEqual(res, len(ejecucion))

    # def test_100_subconjuntos(self):
    #     file = './archivos_prueba/100.txt'
    #     res = 9

    #     conjunto, subconjuntos = obtener_conjunto_y_subconjuntos(file)
    #     ejecucion = obtener_hitting_set(conjunto, subconjuntos)

    #     self.assertEqual(res, len(ejecucion))

    # def test_200_subconjuntos(self):
    #     file = './archivos_prueba/200.txt'
    #     res = 9

    #     conjunto, subconjuntos = obtener_conjunto_y_subconjuntos(file)
    #     ejecucion = obtener_hitting_set(conjunto, subconjuntos)

    #     self.assertEqual(res, len(ejecucion))


if __name__ == '__main__':
    unittest.main()
