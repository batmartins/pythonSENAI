print(f"É positivo ou negativo?")
print("")
print(f"digite 1 para continuar")
print(f"digite 0 para sair")
print("")

#_função
def verificar(num):
    
    if num < 0:
        print(f"O número:{num} é negativo")
        return False
        
    else:
        print(f"O número:{num} é positivo")
        return True
        
#_código
while True:
    print("")
    print(f"digite 1 para continuar")
    print(f"digite 0 para sair")
    print("")
    
    escolha = int(input("digite sua escolha"))
    
    if escolha == 1:
        num = int(input("digite o número"))
        verificar(num)
    elif escolha == 0:
        print("você saiu")
        break
    else:
        print("escolha não identificada")