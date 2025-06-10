print("tempo de percurso")
print("")

#_função
def calcular(distancia, velocidade):
    result = distancia/velocidade
    print(f"levará {result} hora(s) para realizar esse percurso")
    
#_código
distancia = int(input("digite a ditância da viagem em km"))
velocidade = int(input("digite a velocidade do carro em km/h"))

calcular(distancia, velocidade)