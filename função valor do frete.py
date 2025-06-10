print("valor do frete")
print("")

#_função
def calcular_frete(peso, distancia, taxa_fixa):
    valor = (peso*0.5) + (distancia*0.1) + taxa_fixa
    print(f"o valor do frete é de {valor} reais")

#_código
peso = int(input("digite o peso em kg"))
distancia = int(input("digite a distancia em km"))
taxa_fixa = 100
calcular_frete(peso, distancia, taxa_fixa)