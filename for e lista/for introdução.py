#1-crio uma lista com os nomes de 5 objetos
objetos = ["mesa", "ventilador", "caneta", "cadeira", "garrafa"]
print("lista criada")
print("")


#2-adiciono mais um objeto ao final da lista
objetos.append("ar-condicionado")
print('item "ar-condicionado" adicionado')
print("")


#3-acesso o objeto que está na 2° posição e exibo-o
print(objetos[1])
print("2° objeto exibido")
print("")


#4-removo um objeto da lista e exibo-o
remover = objetos.pop(2)
print(remover)
print("item removido e exibido")
print("")


#5-exibo o tamanho da lista
print(len(objetos))
print("tamanho da lista exibido")
print("")


#6-mostro todos os itens com o 'for'
for item in objetos:
    print(item)
print("itens exibidos")
print("")


#7-verifico se 'cadeira' está na lista. Se sim, removo-a, se não, adiciono
if "cadeira" in objetos:
    objetos.remove("cadeira")
    print('item "cadeira" removido')
else:
    objetos.append("cadeira")
    print('item "cadeira" adicionado')
print("")


#8-ordeno a lista em ordem alfabética, exiba o antes e o depois
for item in objetos:
    print(item)
print("lista exibida")
print("")
objetos.sort()
for item in objetos:
    print(item)
print("lista organizada em ordem alfabética e exibida")
print("")


#9-acesso o primeiro e o último objeto e exibo eles
print(objetos[0])
print("primeiro item exibido")
ultimo = objetos.pop()
print(ultimo)
objetos.append(ultimo)
print("último item exibido")
print("")


#10-limpo toda a lista
objetos.clear()
print("lista limpa")
print("")