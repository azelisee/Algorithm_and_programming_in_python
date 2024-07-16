import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-3,4)
y2 = 2*x**2 - 4*x - 6
y3 = (x + 2)*(-x + 3)
plt.plot(x,y2,"ro-")
plt.plot(x,y3,"y--")
plt.grid()
plt.show()
