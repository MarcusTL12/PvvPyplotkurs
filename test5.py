import numpy as np
import sympy

a, b, c, d = sympy.symbols('a b c d')

A = np.matrix([[a, b],
               [c, d]])
#

print(A)

print(A**2)
