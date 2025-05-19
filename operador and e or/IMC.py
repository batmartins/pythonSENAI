print("Qual é seu IMC?")
peso = float(input("digite seu peso em kg"))
altura = float(input("digite sua altura em metros"))

imc = peso/altura**2

if imc <=19:
    print(f'{imc:.2f}, você está abaixo do peso')
elif imc >19 and imc <=27:
    print(f'{imc:.2f}, você está com o peso ideal')
elif imc >27 and imc <=32:
    print(f'{imc:.2f}, você está acima do peso')
elif imc >32:
    print(f'{imc:.2f}, você está obeso')