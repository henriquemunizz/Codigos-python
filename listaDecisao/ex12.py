#12. Faça um algoritmo que leia as médias semestrais obtidas por um aluno na disciplina de
#Computational Thinking, o número de aulas ministradas e o número de aulas assistidas por
#este aluno nesta disciplina. Calcule e mostre a média final deste aluno e diga se ele foi
#aprovado ou reprovado ou está de exame. Lembrando que a média do primeiro semestre tem
#peso 4 e a do segundo peso 6, além disso, o aluno tem que ter frequentado mais de 70% das
#aulas

cp1 = float(input("Nota CP1: "))
cp2 = float(input("Nota CP2: "))
cp3 = float(input("Nota CP3: "))
cp4 = float(input("Nota CP4: "))
gs1 = float(input("Nota GS1: "))
gs2 = float(input("Nota GS2: "))
cllg1 = float(input("Nota Challenge1: "))
cllg2 = float(input("Nota Challenge2: "))
cllg3 = float(input("Nota Challenge3: "))
cllg4 = float(input("Nota Challenge4: "))
aulasMin = int(input("Aulas Ministradas: "))
aulasAss = int(input("Aulas Assistidas: "))

mediaCp1 = (cp1 + cp2) / 2
mediaCll1 = (cllg1 + cllg2) / 2
mediaFinal1 = mediaCp1 * 0.2 + mediaCll1 * 0.2 + gs1 * 0.6

mediaCp2 = (cp3 + cp4) / 2
mediaCll2 = (cllg3 + cllg4) / 2
mediaFinal2 = mediaCp2 * 0.2 + mediaCll2 * 0.2 + gs2 * 0.6

mediaTotal = mediaFinal1 * 0.4 + mediaFinal2 * 0.6

frequencia = aulasAss / aulasMin * 100

if frequencia < 70:
    print("Reprovado por frequência.")
else:
    if mediaTotal >= 6:
        print("Aprovado!")
    elif mediaTotal >= 4:
        print("Exame.")
    else:
        print("Reprovado por nota.")