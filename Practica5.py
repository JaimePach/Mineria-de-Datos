
from Practica2 import obtener_tablaprincipal
from scipy.stats import f_oneway


if __name__=="__main__":

  archivo_csv = 'archive/metacritic_games.csv'
  df,columnas = obtener_tablaprincipal(archivo_csv)
  
  resultado_anova = f_oneway(df['positive_critics'], df['neutral_critics'], df['negative_critics'])
  print("\n\n Resultados del ANOVA: \n")
  print("\n Estadística F:", resultado_anova.statistic)
  print("\n Valor p:", resultado_anova.pvalue)

  
  # Interpretar los resultados
  alpha = 0.05
  if resultado_anova.pvalue < alpha:
    print("\n Hay diferencias significativas entre al menos dos grupos.")
  else:
    print("\n No hay evidencia suficiente para concluir diferencias significativas entre los grupos.")