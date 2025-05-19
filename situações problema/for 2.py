import inputs
print("reunião")
print("")
print("menu de opções")
print("1 - cadastrar um nome")
print("2 - exibir o total de inscritos")
print("3 - exibir a lista de nomes em ordem alfabética")
print("4 - realizar a confirmação de presença dos pais")
print("5 - exibir o relatório da chamada")
print("6 - sair")
print("")
nomes = []
presentes = []
ausentes = []
while True:
    opcao = inputs.input_int("digite sua escolha")
    print("")

    if opcao == 1:
        nome = inputs.input_str("digite o nome que quer cadastrar")
        if nome in nomes:
            print("nome já cadastrado")
        else:
            nomes.append(nome)
            print("nome cadastrado com sucesso")
    elif opcao == 2:
        print("o total de pais é", len(nomes))
    
    elif opcao == 3:
        nomes.sort()
        for nome in nomes:
            print(nome)
    elif opcao == 4:
        nome = inputs.input_str("digite um nome para verificar se está presente")
        if nome in nomes:
            presente = inputs.input_str("está presente? sim/não")
            if presente == "sim":
                presentes.append(nome)
                print("nome adicionado à lista de presentes")
            else:
                ausentes.append(nome)
                print("nome adicionado à lista de ausentes")
        else:
            print("nome nao encontrado")
    elif opcao == 5:
        print("lista de presentes:")
        for item in presentes:
            print(item)
        print("")
        print("lista de ausentes:")
        for item1 in ausentes:
            print(item1)
    elif opcao == 6:
        print("você saiu")
        break
    else:
        print("opção inesistente")