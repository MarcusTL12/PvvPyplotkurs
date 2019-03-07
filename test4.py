import numpy as np
import scipy.special as sp

print(sp.binom(10, 2))

A = np.matrix("[1 2 3; 1 2 4; 3 2 5]")

B = np.matrix("""[1 2 3;
                  1 2 4;
                  3 2 5]""")
#

C = np.matrix([[1, 2, 3],
               [1, 2, 4],
               [3, 2, 5]])
#

print(A, '\n')
print(B, '\n')
print(C, '\n')


print(A[0, 1])
print(A[1, :], '\n')
print(A[:, 2], '\n')

print((2 * A)**2, '\n')

print(A.T, '\n')

print(np.linalg.inv(A))

print(np.linalg.det(A), '\n')


b = np.matrix([1, 2, 3]).T

print(b)

print(A * b, '\n')

x = np.linalg.inv(A) * b

print(x, '\n')

print(A * x, '\n')

x2 = np.linalg.solve(A, b)

print(x2, '\n')

