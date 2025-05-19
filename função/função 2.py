print("De Celcius para Fahrenheit e Kelvin")

def kelvin(celcius):
    k = celcius+237
    return k

def fahrenheit(celcius):
    f = celcius*1.8 + 32
    return round(f, 2)

celcius = int(input("digite a temperatura em grau celcius"))

print("a temperatura atual em Fahrenheit e em Kelvin é respectivamente:",fahrenheit(celcius) , 'e', kelvin(celcius))
