import pandas as pd
import matplotlib.pyplot as plt
from typing import Tuple, Dict, List
import numpy as np
from Practica2 import obtener_tablaprincipal

def k_means(puntos: list[np.array], k: int):
    DIM = len(puntos[0]) # determinar la dimension de los puntos
    N = len(puntos) #determinar la cantidad de puntos
    num_cluster = k  
    iterations = 15

    x = np.array(puntos)
    etiquetaspuntos = np.random.randint(0, num_cluster, N)
    
    mean = np.zeros((num_cluster, DIM)) #crear centroides [0,0] de dimension 2

    for t in range(iterations): # iteraciones a realizar
        for n in range(num_cluster): #Para cada centroide
            mean[n] = np.mean(x[etiquetaspuntos == n], axis=0) # calcula un centroide usando la media de los puntos con etiquetas definidas
        for i in range(N): #Para cada punto existente
            dist = np.sum((mean - x[i]) ** 2, axis=1) # saca las distancias al cuadrado del punto x[i] a cada centroide
            pred = np.argmin(dist) # devuelve el indice del valor minimo de dist
            etiquetaspuntos[i] = pred #devuelve el indice de la distancia mas corta(centroide mas cerca) 

    for kl in range(num_cluster): # se grafica los puntos
        xp = x[etiquetaspuntos == kl, 0]
        yp = x[etiquetaspuntos == kl, 1]
        plt.scatter(xp, yp)
    plt.savefig("archive/kmeans.png")
    plt.close()
    return mean

if __name__=="__main__":

  archivo_csv = 'archive/metacritic_games.csv'
  df,columnas = obtener_tablaprincipal(archivo_csv)

  columna_x = df['positive_critics']
  columna_y = df['neutral_critics']
  puntos = list(zip(columna_x, columna_y))
  k_means(puntos,3 )
