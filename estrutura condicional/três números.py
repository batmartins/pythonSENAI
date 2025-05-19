print('qual dos três números é o maior?')
n1 = int(input('digite o primeiro número'))
n2 = int(input('digite o segundo número'))
n3 = int(input('digite o terceiro número'))
if n1>n2:
    if n1>n3:
        print(n1, 'é o maior número')
    elif n3>n2:
        print(n3, 'é o maior número')
elif n2>n3:
    print(n2, 'é o maior número')
else:
    print(n3, 'é o maior número')