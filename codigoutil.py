#Acá voy a poner las anotaciones importantes de los videos codigo andando
import wget as w
import pandas as pd
import math as m
from math import sin, cos
from os import path as pth
import random as n

import requests

def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)

wget("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Clase_3_datos/Datos.xlsx")

archivo = pd.read_excel("Datos.xlsx", index_col= "Nombre") #aca leemos el archivo excel del link de arriba↑↑
# La variable archivo es de un tipo de dato especial de pandas llamado 'DataFrame'

#print (d ["Quimica"]) #[10, 4, 2, 9, 8, 1]

#print (d)
#alumno = df.loc [0]
#print (alumno["Quimica"])
#print(archivo)
alumnito = archivo.loc ["Sol"]
print (alumnito)

df = pd.read_excel ("Datos.xlsx")
d = df.to_dict("records") #puede ser "record" tambien o "list"

for alumno in d:
    if alumno["Nombre"] == "Sol":
        print ("Te encontré! ", alumno)



datin = {
    "usuario": ["pato", "nato", "gato"],
    "pass": ["abc123", "contra", "casdcas"],
    "random": []
}

for i in range(3):
    datin["random"].append (n.randint (1,30))

print (datin)
df = pd.DataFrame(datin)
print (df)

#----------------------------------------------

archivo = pd.read_excel("Datos.xlsx") 
data = archivo.to_dict("list") 
# "list" significa que vamos a almacenar a cada columna como una lista con su contenido

print(data)
print(data['Nombre'])     # Accedemos a los datos de una columna
print(data['Nombre'][2])  # Accedemos al índice 2 de la columna 'Nombres'

#---------------similar pero con record -----------
archivo = pd.read_excel("Datos.xlsx") 

data = archivo.to_dict("records") 
# "records" significa que vamos a obtener el contenido separado por cada fila

print(data)
print(data[2])            # Accedemos a los datos de una fila
print(data[2]['Nombre'])  # Accedemos a la columna 'Nombres' de la fila con índice 2