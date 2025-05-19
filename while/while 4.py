print("fatorial, ao quadrado, ao cubo ou tabuada")
while True:
    print("que conta você quer fazer?")
    print("0 para sair")
    print("1 para fatorar")
    print("2 para ao quadrado")
    print("3 para ao cubo")
    print("4 para a tabuada")
    menu = int(input("digite sua opção:"))
    if menu != 0:
        n = int(input("digite o número que você quer operar"))
    if menu == 0:
        print("você saiu")
        break
    elif menu == 1:
        contador = 1
        fator = contador
        while n > contador:
            fator = fator * (contador+1)
            contador = contador + 1
        print(contador)
        print(fator)
    elif menu == 2:
        print(n**2)
    elif menu == 3:
        print(n**3)
    elif menu == 4:
        print(n*1)
        print(n*2)
        print(n*3)
        print(n*4)
        print(n*5)
        print(n*6)
        print(n*7)
        print(n*8)
        print(n*9)
        print(n*10)
    else:
        print("ERRO, opção inválida")