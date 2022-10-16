from sympy.matrices import Matrix
from sympy import pprint

A = Matrix([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
])

B = Matrix([[1, 1, 1]])

C = Matrix([[1], [1], [1]])

CI = Matrix([0, 0, 0])

pprint(A)
pprint(B)
pprint(C)