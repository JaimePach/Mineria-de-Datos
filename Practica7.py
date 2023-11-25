import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, List, Dict
import random
from Practica2 import obtener_tablaprincipal


def convertir_dataframe_list(df: pd.DataFrame , colum_x: str, colum_y: str)-> List: # convierte un dataframe en lista de tuplas
    if colum_x not in df.columns or colum_y not in df.columns:
        raise ValueError("Al menos una de las columnas especificadas no se encuentra en el DataFrame.")
    tuple_list = list(zip(df[colum_x], df[colum_y]))
    # Excluir la primera tupla que contiene los nombres de las columnas
    tuple_list = tuple_list[1:]
    return tuple_list

def distancia_euclidiana(punto1: np.array, punto2: np.array)-> float:  #Calcula la distancia euclidiana
    return np.sqr(np.sum((punto2-punto1) ** 2))



                            
def k_nearest_neighbors(datos: List[np.array],datosprueba: List[np.array],etiquetas: List[str] ,k: int):
    



if __name__=="__main__":
    
  archivo_csv = 'archive/metacritic_games.csv'
  df,columnas = obtener_tablaprincipal(archivo_csv)

  columna_x = df['positive_critics']
  columna_y = df['neutral_critics']

  grupos = ["Grupo1","Grupo2","Grupo3"]
  puntos = list(zip(columna_x, columna_y)) #asigna los puntos
  longitud = len(puntos) #la longitud de los puntos
  etiquetas = [str(i) for i in range(0, longitud)] # aqui se pondra la etiqueta a cada uno de los puntos
  

