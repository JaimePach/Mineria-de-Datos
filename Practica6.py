import pandas as pd
from Practica2 import obtener_tablaprincipal
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt


def regresion_lineal(df: pd.DataFrame, columna_x: str, columna_y: str):
   
    x = df[columna_x].values.reshape(-1, 1)
    y = df[columna_y].values

    modelo = LinearRegression()
    modelo.fit(x, y)

    y_pred = modelo.predict(x)
    coef_correlacion = r2_score(y, y_pred)
    # Crear la figura y el eje
    fig, ax = plt.subplots()
    ax.scatter(x, y, color='blue', label='Datos reales')
    ax.plot(x, y_pred, color='red', linewidth=2, label='Regresión lineal')
    texto_coef = f'Coef. de Correlación (R^2): {coef_correlacion:.2f}'
    ax.text(0.05, 0.95, texto_coef, transform=ax.transAxes, fontsize=10, verticalalignment='top')

    # Configurar etiquetas y leyenda
    ax.set_xlabel(columna_x)
    ax.set_ylabel(columna_y)
    ax.legend()

    # Mostrar la gráfica
    plt.show()
    return modelo, coef_correlacion


def crear_dataframe_detiempo(df: pd.DataFrame, columna: str, var_y: str, valorFila: str) -> pd.DataFrame: # funcion para series de tiempo
   df_nuevo = df[[columna,'release_date',var_y ]].copy()
   df_nuevo = df_nuevo[df_nuevo[columna] == valorFila]
   df_nuevo = df_nuevo.groupby('release_date')[[var_y]].sum().reset_index()
   return df_nuevo

def crear_dataframe_lineal(df: pd.DataFrame, columna_x: str, columna_y: str):
   df_nuevo = df[[columna_x, columna_y]].copy()
   df_nuevo = df_nuevo.groupby(columna_x)[[columna_y]].mean().reset_index()
   return df_nuevo

if __name__=="__main__":

  archivo_csv = 'archive/metacritic_games.csv'
  df,columnas = obtener_tablaprincipal(archivo_csv)

  columna = "metascore"
  #valorfila = "PC"
  var_y = "user_score"
  

  #df = crear_dataframe_detiempo(df, columna, var_y, valorfila )
  df = crear_dataframe_lineal(df, columna, var_y)
  regresion_lineal(df, columna,var_y)