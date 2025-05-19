print("qual o tipo do triangulo?")
l1 = int(input("digite um lado do triangulo"))
l2 = int(input("digite o outro lado do triangulo"))
l3 = int(input("digite o último lado do triangulo"))

if l1==l2 and l2==l3 and l1==l3:
    print(" o triangulo é equilátero")
elif l1==l2 and l2==l3 and l1!=l3 or l1==l2 and l2!=l3 and l1==l3 or l1!=l2 and l2==l3 and l1==l3 or l1!=l2 and l2!=l3 and l1==l3 or l1==l2 and l2!=l3 and l1!=l3 or l1!=l2 and l2==l3 and l1!=l3:
    print(" o triangulo é isósceles")
else:
    print("o triangulo é escaleno")
