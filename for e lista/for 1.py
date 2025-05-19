import inputs
print("inscrições para o evento escolar")
print("")
print("menu de opções")
print("1 - cadastrar um nome")
print("2 - exibir o total de inscritos")
print("3 - exibir a lista de nomes em ordem alfabética")
print("4 - permitir a consulta de um nome")
print("5 - sair")
print("")
nomes = []
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
        print("o total de inscritos é", len(nomes))
    
    elif opcao == 3:
        nomes.sort()
        for nome in nomes:
            print(nome)
    elif opcao == 4:
        nome = inputs.input_str("digite o nome que quer consultar")
        if nome in nomes:
            vari = inputs.input_str("nome encontrado, você deseja remove-lo da lista? s/n")
            if vari == "s":
                nomes.remove(nome)
                print("nome removido")
            elif vari == "n":
                print("o nome permanece na lista")
            else:
                print("opção inesistente")
        else:
            vari1 = inputs.input_str("nome não encontrado, deseja adiciona-lo? s/n")
            if vari1 == "s":
                nomes.append(nome)
                print("o nome foi adicionado à lista")
            elif vari1 == "n":
                print("ok")
            else:
                print("opção inesistente")
    elif opcao == 5:
        print("você saiu")
        break
    else:
        print("opção inesistente")