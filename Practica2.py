import tkinter as tk
from tkinter import ttk
import pandas as pd

def obtener_tablaprincipal(archivo_csv):
    
    with open(archivo_csv, 'r') as file: #Leer solo la primera fila del CSV para obtener los nombres de las columnas
        column_names = next(file).strip().split(',')
    column_names.remove('number_players')
    # Crear un DataFrame del CSV
    df = pd.read_csv(archivo_csv, na_values=[''])
    df = df.fillna("N/A")

    df = df.drop(df.columns[4], axis=1)
    
    return df ,column_names

def imprimir_dataframe_en_ventana(df,column):
    ventana = tk.Tk()  # Crear la ventana principal
    ventana.title("Tablas")
    ventana.config(width=1000, height=500)

    frame_tabla = ttk.Frame(ventana)  # Crear un Frame para la tabla y la barra de desplazamiento
    frame_tabla.pack(expand=True, fill='both')

    # Crear un Treeview (tabla) en el Frame
    tabla = ttk.Treeview(frame_tabla, columns=column, show='headings')

    # Crear una barra de desplazamiento vertical
    scrollbar_y = ttk.Scrollbar(frame_tabla, orient='vertical', command=tabla.yview)
    tabla.configure(yscrollcommand=scrollbar_y.set)

    for col in column:  # Aquí se definen las columnas
        tabla.heading(col, text=col)
        tabla.column(col, width=100)

    for fila in df.itertuples(index=False):  # Agregar los datos a la tabla iterando las filas
        tabla.insert("", "end", values=fila)
    
    # Empaqueta la tabla y la barra de desplazamiento en el Frame
    tabla.pack(side='left', fill='both', expand=True)
    scrollbar_y.pack(side='right', fill='y')

    # Inicia el bucle principal de la aplicación
    ventana.mainloop()

# Llamar a la función para obtener el DataFrame
archivo_csv = 'archive/metacritic_games.csv'
df ,columnas= obtener_tablaprincipal(archivo_csv)

# Llamar a la función para imprimir el DataFrame en la ventana
imprimir_dataframe_en_ventana(df, columnas)
