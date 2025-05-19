print("o que voce é?")
ano_nascimento = int(input("digite seu no de nascimento"))
ano_atual = int(input("em que ano estamos?"))

if ano_atual <=2025 and ano_atual >=1908 and ano_nascimento>=1908 and ano_nascimento<=2025:

    idd = ano_atual-ano_nascimento

    if idd <=10:
        print(idd, "voce é kid")
    elif idd >=11 and idd <=17:
        print(idd, "você é adolescente")
    elif idd >=18 and idd <=59:
        print(idd, "você é adulto")
    elif idd >=60:
        print(idd," você é idoso")
else:
    print("ano inválido")