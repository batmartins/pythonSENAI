nota1 = int(input('digite sua primeira nota'))
nota2 = int(input('digite sua segunda nota para saber se foi aprovado'))

notas1 = nota1+nota2
notas = notas1/2

a_ou_r = ''

if notas >= 70:
    a_ou_r = notas
    print('sua nota foi', notas, 'e você foi aprovado!')
else:
    a_ou_r = notas
    print('sua nota foi', notas, 'e você foi reprovado')
    