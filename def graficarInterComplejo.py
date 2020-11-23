import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np

print ("Ahora se mostraran la comparativa entre las empresas de Amazon y Google")
#wget ("https://raw.githubusercontent.com/LedesmaFran/python/master/GOOGLE.csv") 
#wget  ("https://raw.githubusercontent.com/LedesmaFran/python/master/AMZN.csv")

googlefile = pd.read_csv("GOOGLE.csv")
amazonfile = pd.read_csv("AMZN.csv")
google2= pd.DataFrame(googlefile)
google = googlefile.to_dict("list")
amazon = amazonfile.to_dict("list")


#print(google['Open'])
#print(amazon['Open'])


maxG = len(google['Date'])-1
maxA = len(amazon['Date'])-1
plt.figure(figsize=(14, 6))
crucex = []
crucey = []
gx = [google["Date"][0]]
gy = [google["Open"][0]]
ax = [amazon["Date"][0]]
ay = [amazon["Open"][0]]

# Empiezan con el valor del primer dia
opc = input('Desea establecer fechas limite? s/n')

if opc == 's':
    if google["Date"][0] > amazon["Date"][0]:
        print('La fecha inicial minima posible es: ', google["Date"][0])
    else:
        print('La fecha inicial minima posible es: ', amazon["Date"][0])
    fechai = str(input('Ingrese la fecha inicial (AAAA-MM-DD)'))


    if google["Date"][maxG] > amazon["Date"][maxA]:
        print('La fecha final maxima posible es: ', amazon["Date"][len(amazon["Date"])-1])
    else:
        print('La fecha final maxima posible es: ', google["Date"][len(google["Date"])-1])

    fechaf = str(input('Ingrese la fecha final (AAAA-MM-DD)'))
    we = int(0)
    x = int(0)
    while google["Date"][we] != fechai:
        we += 1
    while google["Date"][x] != fechaf:
        x += 1

    for y in range(we, x):
        gx.append(google["Date"][y])
        gy.append(google["Open"][y])
        ax.append(amazon["Date"][y])
        ay.append(amazon["Open"][y])

        if (ay[y] == gy[y]) or (ay[y] > gy[y] and ay[y - 1] < gy[y - 1]) or (ay[y] < gy[y] and ay[y - 1] > gy[y - 1]):
            crucex.append(gx[y])
            crucey.append(gy[y])



else:

    for i in range(1, len(google["Date"])):  # range empieza desde 1 en vez de 0
        gx.append(google["Date"][i])
        gy.append(google["Open"][i])
        ax.append(amazon["Date"][i])
        ay.append(amazon["Open"][i])

    # Condicional de cruce (son iguales o invirtieron su orden)
        if (ay[i] == gy[i]) or (ay[i] > gy[i] and ay[i - 1] < gy[i - 1]) or (ay[i] < gy[i] and ay[i - 1] > gy[i - 1]):
            crucex.append(gx[i])
            crucey.append(gy[i])

plt.plot(gx,gy, "b", label= "Google" )
plt.plot(ax,ay,  "r", label= "Amazon")
plt.plot(crucex,crucey, 'o')
plt.xlabel('Fecha')
plt.ylabel('Precio')
plt.xticks(gx[::100], rotation=45)
plt.title("Gráfico Google y Amazon con INTERSECCIONES marcadas")
plt.legend()
plt.savefig ("Grafico Complejo Amazon-Google2.jpg")
plt.show()






    

