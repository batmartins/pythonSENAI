def imc(peso, altura):
    imc1 = peso/(altura*altura)
    return imc1

def intensidade(imc_):
    if imc_ < 18.5:
        print(imc, " seu estado é de magreza")
    elif imc_ >= 18.5 and imc_ <=24.9:
        print(imc_, "seu estado é normal")
    elif imc_ >=25 and imc_ <=29.9:
        print(imc_, "o seu estado é sobrepeso")
    elif imc_ >=30 and imc_ <=34.9:
        print(imc_, "o seu estado é de obesidade grau 1")
    elif imc_ >=35 and imc_ <=39.9:
        print(imc_, "o seu estado é de obesidade grau 2")
    elif imc_ >= 40:
        print(imc_, "seu estado é de obesidade grau 3")
    else:
        print(imc_, "ERRO. IMC inválido")


altura = float(input("digite a sua altura em metros"))
peso = float(input("digite seu peso em kg"))
imc_ = imc(peso, altura)

intensidade(imc_)