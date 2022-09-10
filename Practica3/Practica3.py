from sympy.interactive.printing import init_printing
init_printing(use_unicode=False, wrap_line=False)
from sympy.abc import s
from sympy.integrals.transforms import inverse_laplace_transform
from sympy.matrices import Matrix, eye
from sympy import pprint, integrate, symbols, simplify, init_printing
from sympy.plotting import plot
from sympy.interactive import printing
from control import tf2ss, tf, ssdata
from os import system
# from sympy.abc import s, t

# Funcion para imprimir la entrada
def imprimir_entradas(size_num, size_den, num, den):
    print(f"numerador: [", end='')
    for i in range(size_num):
        try:
            print(num[i],end='')
        except:
            print("",end='')
        if i < (size_num + 1):
            print("\t", end='')
    print(f"], denominador: [", end='')
    for i in range(size_den + 1):
        try:
            print(den[i],end='')
        except:
            print("",end='')
        if i < (size_den):
            print("\t", end='')
    print(f"]")

printing.init_printing(use_latex='True')

s, t, tao = symbols('s t tao')
# Ejemplo 1
A = Matrix([[0,1],[-4,-5]])
B = Matrix([[0],[1]])
C = Matrix([1,0])
X0 = Matrix([[-1],[2]])

# n = 2
# den = [1, 3, 2]
# num = [5]
den = []
num = []

# Ingresar datos del usuario

# Obtener num
system("clear")
imprimir_entradas(0,0, [], [])
size_denominador = int(input("\n\nDigita el valor de n para las constantes de Y: "))
for i in range(size_denominador + 1):
    system("clear")
    imprimir_entradas(0, size_denominador, num, den)
    den.append(int(input(f"\n\nDigita el valor de la constante de a*d^{i}y(t)/dt: ")))
    
# Obtener den
system("clear")
imprimir_entradas(0, size_denominador, num, den)
size_numerador = int(input("Digita el valor de n para las constantes de U: "))
for i in range(size_numerador + 1):
    system("clear")
    imprimir_entradas(size_numerador, size_denominador, num, den)
    num.append(int(input(f"Digita el valor de a*d^{i}u(t)/dt: ")))

# print(num)
# print(den)
sistema = tf2ss(num,den)
print(sistema)
A, B, C, D = ssdata(sistema)

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

print("\n---- y(t) = :\n")
y = C * x
# y = C.transpose() * x
# pprint(C.transpose())
pprint(y)

p1 = plot(x[0], show=False)
p2 = plot(x[1], show=False)
p3 = plot(y[0], show=False)
p1.extend(p2)
p1.extend(p3)
p1.show()