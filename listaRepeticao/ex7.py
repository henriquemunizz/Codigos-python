#7. A conversão de graus Fahrenheit para centígrados é obtida pela fórmula C = 5/9(F − 32).
#Escreva um algoritmo que calcule e escreva uma tabela de graus centígrados em função de
#graus Fahrenheit que variem de 50 a 150 Fahrenheit de 1 em 1.

print("  Fahrenheit | Celsius")
print("    ----------------------")

f = 50

while f <= 150:
    c = (5/9) * (f - 32)
    print(f"{f:10}   | {c:7.2f}")
    f += 1