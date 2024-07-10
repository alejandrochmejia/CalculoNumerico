import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
x = np.array([6,9,3])
y = x**3
poly = lagrange(x,y)
plt.plot(poly)
plt.show()

