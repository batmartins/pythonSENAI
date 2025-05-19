print("operação matematica")
n1=int(input("digite um número"))
n2=int(input("digite um segundo número"))
operacao=input("digite uma operação matemática(adição, subtração, multiplicação ou divisão):")
result = True 


while result:
    if operacao=="adição":
        print(n1+n2)
        result = False
    elif operacao=="subtração":
        print(n1-n2)
        result = False
    elif operacao== "multiplicação":
        print(n1*n2)
        result = False 
    elif operacao=="divisão":
        print(n1/n2)
        result = False 
    else:
        print("operação não identificada, por favor, tente novamente mais tarde")
        result = True 
        print("operação matematica")
        n1=int(input("digite um número"))
        n2=int(input("digite um segundo número"))
        operacao=input("digite uma operação matemática(adição, subtração, multiplicação ou divisão):")