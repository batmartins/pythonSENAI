print("qualidade do ar")
print("")

#_função
def verificar_ar(estacao, temp, umid):
    if estacao == "inverno":
        if temp>=20 and temp<=22 and umid>=40 and umid<=55:
            print("a qualidade do ar está ideal")
        else:
            print("a qualidade do ar não está ideal")
    elif estacao == "verão":
        if temp>=23 and temp<=26 and umid>=40 and umid<=65:
            print("a qualidade do ar está ideal")
        else:
            print("a qualidade do ar não está ideal")
#_código
estacao = input("em que estação etamos? (inverno ou verão)")
temp = int(input("qual a temperarura atual?"))
umid = int(input("qual a umidade do ar atual?"))

verificar_ar(estacao, temp, umid)