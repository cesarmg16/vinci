import requests
import zipfile
import pandas as pd
import mysql.connector
import os
import time
from kaggle.api.kaggle_api_extended import KaggleApi

# Espera 30 segundos
time.sleep(30)

# Ruta del archivo descargado
zip_path = '/app/formula-1-world-championship-1950-2020.zip'

# Ruta donde se guardan los csv
data_path = '/app/'

# Crea una instancia de la API de Kaggle
api = KaggleApi()
api.authenticate()

# Atributos del dataset
dataset_owner = 'rohanrao'
dataset_name = 'formula-1-world-championship-1950-2020'

# Descarga el dataset
api.dataset_download_files(dataset_owner + '/' + dataset_name, path=data_path)

# Conexión a la base de datos
connection = mysql.connector.connect(user='root', password='root', host='db', database='f1_data')

# Descomprimir el archivo
with zipfile.ZipFile(zip_path, 'r') as zip_file:
    zip_file.extractall(data_path)

# Borramos el archivo zip
os.remove(zip_path)


# Función de inserción en la base de datos
def insert_csv(name):
    # Lee el archivo csv y lo combierte en DataFrame
    df = pd.read_csv(data_path + name + '.csv')

    # Crea el cursor para ejecutar las consultas en la base de datos
    cursor = connection.cursor()
    
    # Obtiene el número de filas de la tabla
    cursor.execute(f"SELECT count(*) FROM {name}")
    table_count = cursor.fetchone()[0]
        
    # Obtiene el número de filas del archivo sin contar los headers
    file_count = len(df)

    # Compara los valores
    if table_count >= file_count:
        print(f"La tabla {name} está completa")
        return
    
    count = 1
    
    # Recorre cada fila del DataFrame e inserta los datos en la tabla
    for index, row in df.iterrows():
        values = list(row)
        formatted_values = []

        # Itera sobre los valores y los formatea según su tipo
        for value in values:
            if pd.isna(value):
                value = "\\N"

            if isinstance(value, str):                
                value = value.replace("'", "''")
                formatted_value = f"'{value}'"  # Agrega comillas simples al valor de texto
            else:
                formatted_value = str(value)
            formatted_values.append(formatted_value)

        values_str = ', '.join(formatted_values)
        query = f"INSERT IGNORE INTO {name} VALUES ({values_str})"
        cursor.execute(query)
        
        print(f"({count}) Insert en la tabla {name}")
        count += 1
        
        # Guarda los cambios en la base de datos
        connection.commit()

    # Cierra el cursor
    cursor.close()


# Lista de los nombres de las tablas y los archivos csv (coinciden)
names = ['circuits', 'drivers', 'constructors', 'seasons', 'status', 'races', 'constructor_results', 'constructor_standings', 'driver_standings', 'lap_times', 'pit_stops', 'qualifying', 'results', 'sprint_results']

# Recorremos la lista de nombres
for i in range(len(names)):
    # Llamamos a la función de inserción
    insert_csv(names[i])

    # Borramos el archivo
    os.remove(data_path + names[i] + '.csv')

# Cerramos la conexión a la base de datos
connection.close()
