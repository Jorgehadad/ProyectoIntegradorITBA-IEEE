import pandas as pd

# La clave es el titulo de la columna y el contenido son listas con los items de cada columna
data = {
    "Personas" : ["Analía Ferreyra" , "Martin Hugo", "Fernando Lorenzo"],
    "Edad" : [25, 35, 87] 
}

# Con pd.DataFrame podemos generar una variable tipo DataFrame
# Recordemos que DataFrame es el tipo de dato que usa pandas
dataFrame = pd.DataFrame(data) 

print(dataFrame)

# Exportamos la información a un archivo llamado "personas.xlsx"
dataFrame.to_excel("personas.xlsx") 


