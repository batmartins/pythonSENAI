print("despesas")
valor_atual = 0
num_de_despesas = 0

while True:
    print("o que você quer fazer?")
    print("digite 0 para sair")
    print("digite 1 para adicionar valor da despesas ")
    print("digite 2 para mostrar a qauntidade e o valor total das despesas")
    menu = int(input("qual é a sua opção?"))
    
    if menu == 0:
        print("você saiu")
        break
    elif menu == 1:
        adicionar = int(input("qual o valor que você quer adicionar?"))
        print("você adicionou", adicionar, "reais nas suas despesas")
        num_de_despesas += 1
        valor_atual = adicionar + valor_atual
    elif menu == 2:
        print("você tem um total de", num_de_despesas,"despesas, que somam", valor_atual,"reais de despesas")
    else:
        print("ERRO, opção inválida")