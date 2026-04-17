seq = int(input("Quantos números você irá digitar?: "))

contador = 1
segmentoMax = 0
numanterior = 0
num = 0

while contador <= seq:
    numanterior = num
    num = int(input(f"Digite o número {contador} da sequencia: "))
    

    if num > numanterior:
        segmentoMax += 1
    contador += 1

print(f"Segmento máximo: {segmentoMax - 1}")