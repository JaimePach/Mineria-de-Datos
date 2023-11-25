from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Descargar el conjunto de stop words en español (si no lo has hecho antes)
import nltk
nltk.download('stopwords')
nltk.download('punkt')

def generar_nube_palabras(archivo_texto):
    # Leer el archivo de texto
    with open(archivo_texto, 'r', encoding='utf-8') as file:
        texto = file.read()

    # Tokenizar el texto y quitar stop words
    stop_words = set(stopwords.words('spanish'))
    palabras = word_tokenize(texto)
    palabras_filtradas = [palabra.lower() for palabra in palabras if palabra.isalpha() and palabra.lower() not in stop_words]

    # Crear la nube de palabras
    texto_filtrado = ' '.join(palabras_filtradas)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(texto_filtrado)

    # Mostrar la nube de palabras usando matplotlib
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# Ejemplo de uso
archivo_texto = 'archive/texto.txt'  # Reemplaza con el nombre de tu archivo de texto
generar_nube_palabras(archivo_texto)
