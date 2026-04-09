#3. Altere o algoritmo anterior para, além da média, contar os alunos que tiraram entre 0 e 5,0
#(0 ≤ nota < 5,0) e acima de 5,0 (nota ≥ 5,0).

n = int(input("Digite o número de alunos: "))

contador = 1
soma = 0
qntAbaixo = 0
qntMedia = 0

while contador <= n:
    nota = float(input(f"Digite a nota do aluno {contador}: "))
    if nota <= 0 or nota < 5:
        qntAbaixo += 1
    elif nota >= 5:
        qntMedia += 1
    soma += nota
    contador += 1



media = soma / n

print(f"\nMédia da turma: {media:.2f}")
print(f"Alunos na média: {qntMedia}")
print(f"Alunos abaixo da média: {qntAbaixo}")