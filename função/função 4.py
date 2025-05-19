def forma():
    print("digite 1 para o círculo")
    print("digite 2 para o quadrado")
    print("digite 3 para o retângulo")
    forma_geometrica = int(input("qual forma geométrica você quer descobrir a área?"))
    if forma_geometrica == 1:
        circulo()
    elif forma_geometrica == 2:
        quadrado()
    elif forma_geometrica == 3:
        retangulo()
    else:
        print("Erro")

def circulo():
    raio = int(input("digite o raio do círculo"))
    area = 3,14*raio**2
    print("a área do círculo é", area)

def quadrado():
    lado = int(input("qual é o valor do lado do quadrado?"))
    area = lado*lado
    print("A área do quadrado é", area)
    
def retangulo():
    base = int(input("qual é a base do retângulo?"))
    altura = int(input("qual é a altura do retângulo?"))
    area = base*altura 
    print("A área do retâgulo é", area)
    
print("Áreas de circulos, quadrados e retângulos")
forma()
