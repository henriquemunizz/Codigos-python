#2. Dados o número n de alunos de uma turma de Algoritmos e suas notas da primeira prova,
#determinar a média das notas dessa turma. Considere que o usuário digite as informações
#corretamente.

n = int(input("Digite o número de alunos: "))

contador = 1
soma = 0

while contador <= n:
    nota = float(input(f"Digite a nota do aluno {contador}: "))
    soma += nota
    contador += 1

media = soma / n

print(f"\nMédia da turma: {media:.2f}")