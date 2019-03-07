import numpy as np
import matplotlib.pyplot as plt

# Parametric plot

t = np.linspace(0, np.pi * 2, 200)

x = np.sin(3 * t)
y = np.cos(5 * t)

plt.plot(x, y)

plt.show();

