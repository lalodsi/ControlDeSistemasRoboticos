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
from time import sleep

# Funcion para imprimir la entrada
def imprimir_entradas(size_num, size_den, num, den):
    print(f"numerador: [", end='')
    for i in range(size_num):
        try:
            print(num[i],end='')
        except:
            print("_",end='')
        if i < (size_num - 1):
            print("  ", end='')
    print(f"], denominador: [", end='')
    for i in range(size_den):
        try:
            print(den[i],end='')
        except:
            print("_",end='')
        if i < (size_den - 1):
            print("   ", end='')
    print(f"]")

printing.init_printing(use_latex='True')

s, t, tao = symbols('s t tao')
# # Ejemplo 1
# A = Matrix([[0,1],[-4,-5]])
# B = Matrix([[0],[1]])
# C = Matrix([1,0])
X0 = Matrix([[-1],[2]])

# n = 2
# den = [1, 3, 2]
# num = [5]
datos_correctos = False
while(not datos_correctos):
    # Ingresar datos del usuario
    den = []
    num = []
    # Obtener num
    system("clear")
    imprimir_entradas(0,0, [], [])
    size_denominador = int(input("\n\nDigita el valor de n para las constantes de Y: ")) + 1
    for i in range(size_denominador):
        system("clear")
        imprimir_entradas(0, size_denominador, num, den)
        den.append(int(input(f"\n\nDigita el valor de la constante de a*d^{i}y/dt: ")))
        
    # Obtener den
    system("clear")
    imprimir_entradas(0, size_denominador, num, den)
    size_numerador = int(input("\n\nDigita el valor de n para las constantes de U: ")) + 1
    for i in range(size_numerador):
        system("clear")
        imprimir_entradas(size_numerador, size_denominador, num, den)
        num.append(int(input(f"\n\nDigita el valor de a*d^{i}u/dt: ")))

    system("clear")
    imprimir_entradas(size_numerador, size_denominador, num, den)
    respuesta = input("\n\nSon correctos estos valores?(y/n): ")

    while (respuesta != 'y' and respuesta != 'n'):
        respuesta = input("Sólo puedes elegir entre 'y' y 'n'. Son correctos estos valores?(y/n): ")
    if respuesta == 'y':
        datos_correctos = True
    elif respuesta == 'n':
        datos_correctos = False
        
# Comienzo del programa

# Espacio de estados
system("clear")
print("\nGenerando espacio de estados...")
sleep(1)
sistema = tf2ss(num,den)
A, B, C, D = ssdata(sistema)
print("Espacio de estados generado correctamente!")
print(sistema)
sleep(1)

# Obteniendo la matriz exponencial
print("\nCalculando la matriz Exponencial")
print("\n\tCalculando matrices...")
I = eye(2)
inversa_polinomio = (s * I - A).inv()

print("\n\tCalculando transformada inversa de laplace...")
matriz_exponencial = inverse_laplace_transform(inversa_polinomio, s, t)
matriz_exponencial_menosTao = inverse_laplace_transform(inversa_polinomio, s, t-tao)
print("\nMatriz exponencial calculada correctamente!\n")

print("\nCalculando integrales...\n")
integral = integrate(matriz_exponencial_menosTao, (tao, 0, t))
print("\nCalculando x(t)...\n")
x_no_simplificado = matriz_exponencial * X0 + integral * B
x = simplify(x_no_simplificado)

print("\nCalculando y(t)...\n")
y = C * x
# pprint(C.transpose())
pprint(y)

p1 = plot(x[0], show=False)
p2 = plot(x[1], show=False)
p3 = plot(y[0], show=False)
p1.extend(p2)
p1.extend(p3)
p1.show()