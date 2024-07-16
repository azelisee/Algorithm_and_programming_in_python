import matplotlib.pyplot as plt
import numpy as np
plt.clf()
x = np.linspace(-2,6)
y4 = 3 - np.exp(-x + 1)
y5 = 0 * x + 3
plt.plot(x,y4,"g-")
plt.plot(x,y5,"r--")
plt.grid()
plt.show()
