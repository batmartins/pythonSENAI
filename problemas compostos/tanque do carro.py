#1- quanto custa encher o tanque do carro
#2- capacidade de combustível do carro em litros, quantos litros o carro já tem e o valor do litro do comcustível em reais
#3- passo 1-subtrair a capacidade total pelo tanque atual. passo 2- multiplicar o resultado pelo preço do combustível. passo 3-exibir o custo em reais
print('tanque do carro')
capacidade = int(input("insira a capacidade total do tanque"))
jatem = int(input("digite quanto de combustível já tem no tanque"))
subtrair = capacidade-jatem
valor = float(input("digite o valor em reais do litro do combustível"))
multiplicar = subtrair*valor
print('o custo total é de', multiplicar,'reais')