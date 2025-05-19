print("média do aluno")
nota1 = int(input("digite sua primeira nota"))
nota2 = int(input("digite sua segunda nota"))

if nota1>0 and nota1<=100 and nota2>0 and nota2<=100:
    ad = nota1+nota2
    nota = ad/2

    if nota >=70:
        print(nota, "você foi aprovado!")
    elif nota >=50 and nota <70:
        print(nota, "você ficou de recuperação")
    elif  nota <50:
        print(nota, "você foi reprovado")
else:
    print("sua nota é inválida")