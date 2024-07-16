import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2,3); y = -x**3 + x**2 - 2*x
plt.plot(x, y, "ro--")
plt.grid(); plt.show()
