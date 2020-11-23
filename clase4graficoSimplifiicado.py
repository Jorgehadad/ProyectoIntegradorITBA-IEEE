#una forma más facil par asimplificar el tema de los valores de X e Y
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2*3.14, 0.3)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.title("Gráfico azul")
plt.plot(x, y1, 'bo') # graficamos función y1
plt.xlabel('Tiempo')
plt.ylabel('Corriente')

plt.subplot(1, 2, 2)
plt.title("Gráfico rojo")
plt.plot(x, y2, 'r-.') # graficamos función y2
plt.xlabel('Tiempo')
plt.axis([0, 3, -1, 1])
plt.grid()

plt.show()