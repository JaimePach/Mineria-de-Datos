import os
import zipfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Obtener el directorio actual del programa
current_directory = os.getcwd()

# Nombre de la carpeta de descarga
carpeta_descarga = "Mineria de datos"

# Ruta completa a la carpeta de descarga
ruta_descarga = os.path.join(current_directory, carpeta_descarga)

# Verificar si la carpeta de descarga ya existe; si no, crearla
if not os.path.exists(ruta_descarga):
    os.makedirs(ruta_descarga)

# Configurar las opciones de Chrome para descargar archivos en la carpeta especificada
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": ruta_descarga,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

# Inicializar el navegador Chrome con las opciones de configuración
driver = webdriver.Chrome(options=chrome_options)

# Navegar a la página web
driver.get('https://www.kaggle.com/datasets/skateddu/metacritic-games-stats-20112019')

try:
    # Encontrar el elemento de descarga por selector CSS y hacer clic en él
    descarga = driver.find_element(By.CSS_SELECTOR, '.sc-bXWOdt.sc-hjsqBZ.eFcryG.WvDJN')
    descarga.click()

    # Esperar hasta que el archivo zip se descargue (ajusta el tiempo según corresponda)
    wait = WebDriverWait(driver, 100)  # Espera un máximo de 60 segundos
    archivo_descargado = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'archive.zip')))
    
    if archivo_descargado:
        print("La descarga del archivo ZIP se ha completado.")

    # Ruta al archivo ZIP descargado
    zip_file_path = os.path.join(ruta_descarga, 'archive.zip')

    # Extraer el contenido del archivo ZIP
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(ruta_descarga)

    # Verificar si el archivo CSV se ha extraido correctamente
    archivo_csv = os.path.join(ruta_descarga, 'nombre_del_archivo.csv')

    if os.path.isfile(archivo_csv):
        print("La extraccion del archivo CSV se ha completado.")

except Exception as e:
    print(f"Error: {e}")


