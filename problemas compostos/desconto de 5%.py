#passo a passo
#1 solicite um produto e seu preço
#2 aplique 5% de desconto
#3
#passo1- dividir 5 por 100
#passo2- mulplicar pelo valor do produto
#passo3- exibir o valor final e quanto diminuiu
print("desconto de 5%")
nome = input("digite o produto")
preço = int(input("digite o preço do produto em reais"))
resultado = preço/5
resultado2 = preço-resultado
print("o novo valor do produto", nome, "é de", resultado2, "reais")
print(" e o desconto foi de:", resultado, "reais")