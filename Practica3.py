import pandas as pd
from Practica2 import obtener_tablaprincipal,imprimir_dataframe_en_ventana



def imprimir_genero_promedio(df: pd.DataFrame ,columna:str ,columnapromedio:str): 
    tablaspromedio = df.groupby(columna)[[columnapromedio]].mean().reset_index()
    columnas = [columna, columnapromedio]
    nombre = f"Promedio de {columnapromedio}"
    imprimir_dataframe_en_ventana(tablaspromedio,columnas,nombre)

def imprimir_genero_minimo(df: pd.DataFrame, columna:str, columnaminimo: str):
    tablasminimo = df.groupby(columna)[[columnaminimo]].min().reset_index()
    columnas = [columna, columnaminimo]
    nombre = f"Minimo de {columnaminimo}"
    imprimir_dataframe_en_ventana(tablasminimo, columnas, nombre)

def imprimir_genero_maximo(df: pd.DataFrame, columna: str, columnamaximo: str):
    tablasmaximo = df.groupby(columna)[[columnamaximo]].max().reset_index()
    columnas = [columna, columnamaximo]
    nombre = f"Maximo de {columnamaximo}"
    imprimir_dataframe_en_ventana(tablasmaximo, columnas, nombre)        





if __name__=="__main__":
    # Llamar a la función para obtener el DataFrame
   archivo_csv = 'archive/metacritic_games.csv'
   df,columnas= obtener_tablaprincipal(archivo_csv)
   imprimir_genero_promedio(df,'genre','positive_critics' )
   imprimir_genero_maximo(df, 'genre','positive_critics' )
   imprimir_genero_minimo(df, 'genre','positive_critics' )