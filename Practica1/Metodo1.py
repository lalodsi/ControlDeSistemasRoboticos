from sympy.interactive.printing import init_printing
init_printing(use_unicode=False, wrap_line=False)
from sympy.abc import s
from sympy.integrals.transforms import inverse_laplace_transform
from sympy.matrices import Matrix, eye
from sympy import pprint
from sympy.abc import s, t

# Ejemplo
A = Matrix([[0,1],[2,1]])

print("\nMatriz A----\n")
pprint(A)

I = eye(2)
sI = s * I

print("\nPolinomio---- sI - A:\n")
polinomio = sI - A; 
pprint(polinomio)

print("\n\nInversa---- (sI - A)^-1:\n")
inversa_polinomio = polinomio.inv()
pprint(inversa_polinomio)

print("\nInversa de laplace---- L{(sI - A)^-1}:\n")
inversa_laplace = inverse_laplace_transform(inversa_polinomio, s, t)
pprint(inversa_laplace)


# print("\n\Determinante---- (sI - A)^-1:\n")
# determinante = syms.det(inversa_polinomio)
# pprint(determinante)

