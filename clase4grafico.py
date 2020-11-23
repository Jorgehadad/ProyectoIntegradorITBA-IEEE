import matplotlib.pyplot as plt
import numpy as np


#cantidad de puntos
cant = 10

t1= np.arange (0, 1.1, 0.1) #1er valor dominio, 2do valor del dominio, sepacion
t2= np.linspace(0, 1, 11) #diferencia es q el 11 en linspace representa la cantidad de numeros
#que quiero tener en el arreglo
#ADEMÁS LIMSPACE SI INCLUYE EL VALOR INICIAL MIENTRAS QUE ARRANGE NO

x= np.linspace(0, 1, cant)
print (x)

y = [ np.sin (2*np.pi* x[i ]) for i in range (cant)]
print (y)

plt.plot (x, y)
plt.show()




