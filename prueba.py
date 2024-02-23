import numpy as np
import random
from tqdm import tqdm  # Importa tqdm

def verificar(A, B, k, sol):
    if len(sol) > k:
        return False
    
    for subconjunto in B:
        hit = False
        for elem in subconjunto:
            if elem in sol:
                hit = True
                break
        if not hit:
            return False
    
    return True

from algoritmo_aproximado import hitting_set_greedy
from algoritmo_backtracking import obtener_hitting_set
from utils.utils import obtener_conjunto_y_subconjuntos
from time import time
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

def correr_benchmark_optimo(A, B):
    
    empieza = time()
    obtener_hitting_set(A, B)
    termina = time()
    
    return termina - empieza

def correr_benchmark_aproximado(A, B):
    
    empieza = time()
    hitting_set_greedy(A,B)
    termina = time()
    
    return termina - empieza



random.seed(7)

def n_log_n(n):
    return n * np.log(n)
MAX_SUBCONJUNTOS = 1000
def plottear_tiempos_de_aproximado_en_funcion_de_cantidad_de_peticiones():
    # archivos = ["./archivos_prueba/5.txt", "./archivos_prueba/10_varios.txt", "./archivos_prueba/15.txt", "./archivos_prueba/20.txt", "./archivos_prueba/50.txt", "./archivos_prueba/75.txt", "./archivos_prueba/100.txt", "./archivos_prueba/150_not_for_testing.txt", "./archivos_prueba/175_not_for_testing.txt", "./archivos_prueba/200.txt"]
    cantidades = []
    tiempos = []
    for i in tqdm(range(1, MAX_SUBCONJUNTOS + 1, 10), desc="Corriendo benchmark"):
        cant_a = random.randint(1, i)
        cant_b = random.randint(1, i)
        A = [j for j in range(cant_a)]
        B = []
        for i in range(cant_b):
            cant = random.randint(1, cant_a)
            B.append(random.sample(A, cant))
        cantidades.append(i)
        tiempos.append(correr_benchmark_aproximado(A, B))


    df = pd.DataFrame(data={"cantidades": cantidades, "tiempos": tiempos})

    # Calcula los valores de n(log(n))
    # df['n_log_n'] = df['cantidades'].apply(n_log_n)

    # Traza la gráfica
    df = pd.DataFrame(data={"cantidades": cantidades, "tiempos": tiempos})
    sns.lmplot(x='cantidades', y='tiempos', data=df, order=2)
    # plt.title("Tiempo en funcion de la cantidad de peticiones")
    # plt.xlabel("Cantidad de peticiones (n)")
    # plt.ylabel("Tiempo de ejecucion (s)")
    plt.show()

plottear_tiempos_de_aproximado_en_funcion_de_cantidad_de_peticiones()
