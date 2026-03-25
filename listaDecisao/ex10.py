#Uma equação de 2º grau é da forma: ax2 + bx + c = 0, onde a ̸= 0. Escreva um algoritmo
#que recebe os três coeficientes da equação, calcula e imprime as raízes reais se for possível.
#Use a seguinte fórmula para resolver a equação:

import math

a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente c: "))

if a == 0:
    print("Não é equação do segundo grau")
else:
    delta = b**2 - 4*a*c
    
    if delta < 0:
        print("Não possui raízes reais")
    else:
        raiz_delta = math.sqrt(delta)
        x1 = (-b + raiz_delta) / (2*a)
        x2 = (-b - raiz_delta) / (2*a)
        
        print("x1 =", x1)
        print("x2 =", x2)