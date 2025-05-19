import inputs
def mostrar():
    print("Calculadora Básica")
    print("para adição digite 1")
    print("para subtrção digite 2")
    print("para multiplicação digite 3")
    print("para divisão digite 4")
    print("para todas as anteriores digite 5")
    
def soma(n1, n2):
    return n1+n2

def subtracao(n1, n2):
    return n1-n2

def multiplicacao(n1, n2):
    return n1*n2

def divisao(n1, n2):
    return n1/n2

def tudo(n1, n2):
    print("o resultado da soma é", soma(n1, n2))
    print("o resultado da subtração é", subtracao(n1, n2))
    print("o resultado da multiplicação é", multiplicacao(n1, n2))
    print("o resultado da divisão é", divisao(n1, n2))
def calculo(n1, n2, operacao):
    if operacao == 1:
        print("o resultado da soma é",soma(n1, n2))
    elif operacao == 2:
        print("o resultado da subtração é", subtracao(n1, n2))
    elif operacao == 3:
        print("o resultado da multiplicação é", multiplicacao(n1, n2))
    elif operacao == 4:
        print("o resultado da divisão é", divisao(n1, n2))
    elif operacao == 5:
        tudo(n1, n2)
    else:
        print("Erro, Operação não identificada")

mostrar()

while True:
    try:
        operacao = inputs.input_int("digite a operação:")
        
        n1 = inputs.input_int("digite o primeiro número")
        n2 = inputs.input_int("digite o segundo número")

        calculo(n1, n2, operacao)
        break
    except:
        print("ops, ocorreu um erro de digitação, tente de novo")