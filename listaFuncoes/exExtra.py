
import random

def validador():
    d1 = random.randint(1, 9)
    d2 = random.randint(1, 9)
    d3 = random.randint(1, 9)
    d4 = random.randint(1, 9)
    d5 = random.randint(1, 9)
    d6 = random.randint(1, 9)
    d7 = random.randint(1, 9)
    d8 = random.randint(1, 9)
    d9 = random.randint(1, 9)

    soma1 = d1 * 10 + d2 * 9 + d3 * 8 + d4 * 7 + d5 * 6 + d6 * 5 + d7 * 4 + d8 * 3 + d9 * 2
    resto1 = soma1 % 11

    if resto1 < 2:
        d10 = 0
    else:
        d10 = 11 - resto1

    soma2 = d1 * 11 + d2 * 10 + d3 * 9 + d4 * 8 + d5 * 7 + d6 * 6 + d7 * 5 + d8 * 4 + d9 * 3 + d10 * 2
    resto2 = soma2 % 11

    if resto2 < 2:
        d11 = 0

    else:
        d11 = 11 - resto2

    return f"{d1}{d2}{d3}.{d4}{d5}{d6}.{d7}{d8}{d9}-{d10}{d11}"

j = 1

while j <= 100000:
    print(validador())
    j = j + 1