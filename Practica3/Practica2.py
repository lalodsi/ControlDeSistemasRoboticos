from sympy.interactive.printing import init_printing
init_printing(use_unicode=False, wrap_line=False)
from sympy.abc import s
from sympy.integrals.transforms import inverse_laplace_transform
from sympy.matrices import Matrix, eye
from sympy import pprint, integrate, symbols, simplify
from sympy.plotting import plot
# from sympy.abc import s, t

s, t, tao = symbols('s t tao')
# Ejemplo
A = Matrix([[0,1],[-4,-5]])
B = Matrix([[0],[1]])
C = Matrix([1,0])
X0 = Matrix([[-1],[2]])

print("\nMatriz A----\n")
pprint(A)


# Obteniendo la matriz exponencial
I = eye(2)
sI = s * I

print("\nPolinomio---- sI - A:\n")
polinomio = sI - A; 
pprint(polinomio)

print("\n\nInversa---- (sI - A)^-1:\n")
inversa_polinomio = polinomio.inv()
pprint(inversa_polinomio)

print("\nInversa de laplace---- L{(sI - A)^-1}:\n")
matriz_exponencial = inverse_laplace_transform(inversa_polinomio, s, t)
pprint(matriz_exponencial)

# Realizando la multiplicacion
print("\n---- e^(at) * x0:\n")
e_por_x0 = matriz_exponencial * X0
pprint(e_por_x0)

# Realizando la integral
print("\n---- integral:\n")

matriz_exponencial_menosTao = inverse_laplace_transform(inversa_polinomio, s, t-tao)
integral = integrate(matriz_exponencial_menosTao, (tao, 0, t))
pprint(integral)

print("\n---- x(t) = :\n")
x_no_simplificado = e_por_x0 + integral * B
x = simplify(x_no_simplificado)
pprint(x)

p1 = plot(x[0], show=False)
p2 = plot(x[1], show=False)
p1.extend(p2)
p1.show()