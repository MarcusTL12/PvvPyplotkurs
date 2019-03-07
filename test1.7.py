import numpy as np
import matplotlib.pyplot as plt

m = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6
}

with open("tfy4115.txt", 'r') as file:
    grades = [m[i.strip().split(' ')[-1]] for i in file]



plt.xkcd(True)

plt.hist(grades, bins=12)
plt.xticks([1, 2, 3, 4, 5, 6], ["A", "B", "C", "D", "E", "F"])


plt.show()
