#input da string
def input_str(recado):
    while True:
        nome = input(recado)
        
        if not nome.isalpha():
            print("ERRO, não digite números")
            
        else:
            return nome

#input do int
def input_int(recado):
    while True:
        try:
            numero = int(input(recado))
            return numero
        except ValueError:
            print("ERRO, digite apenas númros inteiros")
            
#input do float
def input_float(recado, casas):
    while True:
        try:
            numero = float(input(recado, casas))
            return numero
        except ValueError:
            print("ERRO, digite apenas números")