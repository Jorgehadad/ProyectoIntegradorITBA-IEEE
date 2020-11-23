import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np

def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)

wget ("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Clase_4_datos/AMZN.csv")
wget ("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Clase_4_datos/GOOGLE.csv")
wget ("https://github.com/scikit-learn/examples-data/blob/master/financial-data/WFC.csv")
wget ("https://github.com/scikit-learn/examples-data/blob/master/financial-data/WMT.csv")
wget ("https://github.com/scikit-learn/examples-data/blob/master/financial-data/MSFT.csv")

amazon= pd.read_csv("AMZN.csv") 
google = pd.read_csv("GOOGLE.csv") 
#fargo = pd.read_csv("WFC.csv")
#wallmart = pd.read_csv("WMT.csv")
#microsoft = pd.read_csv("MSFT.csv")


valores = amazon [["Open", "High", "Low", "Close", "Date"]]
valores2 = google [["Open", "High", "Low", "Close", "Date"]]

#def generarGrafico (empresa1, empresa2):
    
        #ax= valores.plot(x = "Date" , y= "Open")
    #plt.plot (valores["Date"] ,valores["Close"])
    #plt.plot (valores2["Date"] ,valores2["Close"])
    #plt.title("Gráfico Amazón y Google")
    #plt.xlabel('Tiempo')
    #plt.ylabel('Precio')
    #plt.savefig ("graficoamazonygoogle.jpg")
    #return (plt.show ())
    



intersec = (valores[ (valores["Open"]>1000) & (valores2["Open"]>1000) ])

print (intersec ["Open"])


