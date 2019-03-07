import numpy as np
import matplotlib.pyplot as plt

# Getting data from file

# with open("temperatures.txt", 'r') as file:
#     # lines = [[float(j) for j in i.split(' ')] for i in file]
#     low_temps = []
#     high_temps = []
#     for i in file:
#         a = i.split(' ')
#         low = float(a[0])
#         high = float(a[1])
#         low_temps.append(low)
#         high_temps.append(high)

A = np.loadtxt("temperatures.txt", delimiter=' ', usecols=(0,))
B = np.loadtxt("temperatures.txt", delimiter=' ', usecols=(1,))

print(A)

x = [i for i in range(len(A))]

# x = [i for i in range(len(lines))]
# y1 = [i[0] for i in lines]
# y2 = [i[1] for i in lines]


plt.plot(x, A)
plt.plot(x, B)

plt.show()
