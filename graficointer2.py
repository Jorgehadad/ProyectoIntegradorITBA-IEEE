import numpy as np
import matplotlib.pyplot as plt
x = [0, 1, 2, 4, 6]  # in my primary problem i dont have just 5 points and i have approximately 200 points !
y = [0, 0, 3, -1, 2]
x = np.array(x)
y = np.array(y)
a = [np.polyfit(x[i:(i+2)], y[i:(i+2)], 1) for i in range(len(x)-1)]
plt.plot(x, y, "o")
plt.show()