import numpy as np
import matplotlib.pyplot as plt

x = 3*1000
f = 5*1000
g = np.sin(np.arange(0, 10, 0.01) * 2) * 1000

plt.plot(x, f, '-')
plt.plot(x, g, '-')

idx = np.argwhere(np.diff(np.sign(f - g)) != 0).reshape(-2) 
plt.plot(x[idx], f[idx], 'bo-')
plt.show()