#1- achar a área do hexagono
#2- solicitar a medida do lado do triângulo
#3- 1 multiplicar o lado do triângulo por ele mesmo, descobrir raiz de três, multiplicar a raiz pela multiplicação anterior e dividir por quatro.
#3- 2 Multiplicar tudo por seis.
print('área do hexagono')
lado = int(input('digite o lado do hexagono em centímetros'))
lado2 = lado*lado
raiz = round(3**0.5, 2)
mult = raiz*lado2
divisao = mult/4
mult2 = round(divisao*6, 2)
print('a área do hexagono é', mult2)