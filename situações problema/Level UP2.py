import random

def oculto():
    print("Certo! Já escolhi um número")
    n = random.randint(0, 100)
    return n


print("Level Up - jogo de adivinhação")
print("")
print("Para jogar, irei escolher um número aleatório de 0 a 100 e você tentará adivinhar.")
print("A cada chute eu direi se o número inserido é maior ou menor que o número que eu escolhi.")
print("")

num = oculto()
while True:
    print("")
    n2 = int(input("agora chute um número: "))
    if n2 == num:
        print("Parabéns! Você acertou")
        mais_uma = int(input("Você quer ir mais uma? Digite 1 para sim e 2 para sair"))
        if mais_uma == 2:
            print("você saiu")
            break
        elif mais_uma == 1:
            num = oculto()
    
    elif n2 > num:
        print("O número digitado é maior que o meu")
    elif n2 < num:
        print("o número digitado é menor que o meu")
    else:
        print("algo de errado não está certo")