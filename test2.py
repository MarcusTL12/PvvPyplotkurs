import numpy as np
import matplotlib.pyplot as plt

# Plotte matematisk funksjon


def func(x):
	if x < -1:
		return -(x + 1)**2 + 1
	elif x < 1:
		return np.sin(3 / 2 * np.pi * x)
	else:
		return (x - 1)**2 - 1

f = np.vectorize(func)

# x = np.linspace(0, 2 * np.pi, 100)
x = np.linspace(-2, 2, 1000)
# x = np.arange(0, 2 * np.pi, 0.1)

# y = np.sin(x)
y = f(x)

# print(max(y))

plt.plot(x, y)

plt.show()
