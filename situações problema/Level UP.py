import random

print("Level UP - Par ou ímpar")
print("")
while True:
    print("escolha o que quer fazer")
    print("digite 0 para o tutorial")
    print("digite 1 para jogar")
    print("digite 2 para sair")
    escolha = int(input("digite sua escolha: "))
    
    if escolha == 0:
        print("")
        print("1°- Escolha se quer par ou ímpar.")
        print("2°- Digite um número de 0 a 10.")
        print("3°- descubra quem ganhou.")
        print("O jogo funciona da seguinte maneira:")
        print("Você e eu escolhemos se queremos par ou ímpar, depois, escolhemos um número de 0 a 10 cada um.")
        print("Após isso, a soma dos números é efetuada e o resultado ser par ou ímpar é o que vai definir quem venceu")
        print("")
        
    elif escolha == 1:
        i_p = int(input("digite 1 para escolher ímpar, ou 2 para escolher par: "))
        n = int(input("digite um número de 0 a 10: "))
        n2 = random.randint(1, 10)
        soma = n + n2
        print("")
        print("eu escolhi o número:", n2)
        print("você escolheu o número:", n)
        print("")
        if i_p == 2 and soma % 2 == 0:
            print("a soma deu", soma, ", que é par, você venceu!")
        elif i_p == 2 and soma % 2 == 1:
            print("a soma deu", soma, ", que é impar, você perdeu")
        elif i_p == 1 and soma % 2 == 0:
            print("a soma deu", soma, ", que é par, você perdeu")
        else:
            print("a soma deu", soma,", que é ímpar, você venceu!")
            
    elif escolha == 2:
        print("")
        print("você saiu")
        break
              
    else:
        print("opção ínvalida")