import matplotlib.pyplot as plt
import numpy as np

x = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
# x = np.linspace(0, 3, 4)

y1= [1, 4, 1, 6, 8]
y2= [2, 3, 3, 2, 5]

plt.plot(x, y1, "orange")
plt.plot(x, y2, "k")

plt.plot([0.5],[2.5], "r+")
plt.xticks(x)
plt.grid()
plt.show()

