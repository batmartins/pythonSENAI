print("númeors pares antes do seu")
inicio = int(input("digite um número"))
quant = 0
n = 0

while n < inicio:
    n = n + 1
    if n % 2 == 0:
        print(n)
        quant += 1
print("a quantidade de numeros pares é",quant)
    