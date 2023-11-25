import pandas as pd
import matplotlib.pyplot as plt
from Practica2 import obtener_tablaprincipal

def graficar_dataframe(dataframe, columna_x, columna_y, ):

    # Verificar si las columnas existen en el DataFrame
    if columna_x not in dataframe.columns or columna_y not in dataframe.columns:
        print("Las columnas especificadas no existen en el DataFrame.")
        return

    # Ordenar el DataFrame por la columna de fechas
    dataframe = dataframe.sort_values(columna_x)

    # Crear el gráfico 
    plt.figure(figsize=(15, 8))  # Ajustar el tamaño del gráfico 
    plt.scatter(dataframe[columna_x], dataframe[columna_y], marker='o', linestyle='-', color='b')

    # Personalizar el gráfico
    plt.title(f'Gráfico de {columna_y} a lo largo del tiempo')
    plt.xlabel(columna_x)
    plt.ylabel(columna_y)
    plt.grid(True)

  

    # Mostrar el gráfico
    plt.tight_layout()  # Ajustar el diseño para evitar recortar etiquetas
    plt.show()
    

if __name__=="__main__":
   
  # Llamar a la función para obtener el DataFrame
   archivo_csv = 'archive/metacritic_games.csv'
   df ,columnas= obtener_tablaprincipal(archivo_csv)
   graficar_dataframe(df, 'release_date', 'positive_critics')
