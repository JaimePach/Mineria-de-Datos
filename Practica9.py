from typing import List, Tuple
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import datetime
from matplotlib.dates import date2num, DateFormatter
from Practica2 import obtener_tablaprincipal
from scipy.stats import pearsonr

def graficar_regresion_lineal(datos: List[Tuple[str, float]], nombrecolum_y: str,var1: str, var2: str):
    # Desempaqueta las listas de fechas y valores
    fechas, valores = zip(*datos)

    # Convierte las fechas a objetos datetime
    fechas_dt = [datetime.strptime(fecha, '%Y-%m-%d') for fecha in fechas]

    # Convierte las fechas a números de días
    fechas_num = date2num(fechas_dt)

    # Convertir las listas a arreglos
    fechas_np = np.array(fechas_num).reshape(-1, 1)
    valores_np = np.array(valores)

    # Crea el modelo de regresión lineal
    modelo = LinearRegression()
    modelo.fit(fechas_np, valores_np)

    # Hace predicciones
    predicciones = modelo.predict(fechas_np)

    coeficiente_correlacion, _ = pearsonr(fechas_num.flatten(), valores_np)


    # Configura el formato de las fechas en el eje x
    date_format = DateFormatter("%Y-%m-%d")
    plt.gca().xaxis.set_major_formatter(date_format)

    # Rotar las etiquetas de las fechas para que no se superpongan
    plt.xticks(rotation=90, ha='right')

    # Grafica los datos y la regresión lineal
    plt.scatter(fechas_dt, valores, label='Datos')
    plt.plot(fechas_dt, predicciones, color='red', label='Regresión lineal')
    plt.xlabel('Fechas')
    plt.ylabel(nombrecolum_y)
    plt.title(f'Gráfica de {var1} {var2} (Correlación: {coeficiente_correlacion:.2f})')    
    plt.legend()
    plt.show()

if __name__=="__main__":
  archivo_csv = 'archive/metacritic_games.csv'
  df,columnas = obtener_tablaprincipal(archivo_csv)

  columna_y = 'positive_users'
  columnaigualdad1 = 'genre'
  valoresperado1 = 'Strategy'
  columnaigualdad2 = 'platform'
  valoresperado2= 'PC'

  df_nuevo = df[(df[columnaigualdad1]== valoresperado1) & (df[columnaigualdad2]== valoresperado2 )]
  df_final = df_nuevo.groupby('release_date')[[columna_y ]].mean().reset_index()

  datos = list(zip(df_final['release_date'].dt.strftime('%Y-%m-%d'), df_final[columna_y]))

  graficar_regresion_lineal(datos, columna_y,valoresperado1,valoresperado2)
