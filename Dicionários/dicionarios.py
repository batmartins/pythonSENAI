#---------------------------------------------------------------Dicionário-----------------------------------------------------------------------------
#-------------------------------------------------Criar
aluno = {
    "nome": "Lucas",
    "idade": 28,
    "altura": 1.75,
    "matriculado": True 
}
filme_martins = {
    "nome":"the Batman",
    "protagonista":"Batman",
    "ator":"Robert Pattinson",
    "diretor":"Matt Reeves",
    "lancado": True
}
filme_veto = {
    "nome":"Moana, um mar de aventuras",
    "protagonista":"Moana",
    "ator":"Auli'i Cravalho",
    "diretor":"John Musker",
    "lancado": True
}
filme_fer = {
    "nome":"Lilo & Stitck live action",
    "protagonista":"Stitck",
    "ator":"Chris Sanders",
    "diretor":"Todd Cherniawsky",
    "lancado": False
    }
#------------------------------------------------Adicionar campo
aluno["peso"] = 65

#------------------------------------------------Alterar campo
aluno["idade"] = 29

#------------------------------------------------Deletar campo
del aluno["altura"]

#------------------------------------------------Verificar
if "altura" in aluno:
    print("altura existente")
else:
    print("altura inexistente")

#-------------------------------------------------Exibir
for chaves, valor in aluno.items():
    print(f"{chaves}:{valor}")
print("")
for chaves, valor in filme_martins.items():
    print(f"{chaves}:{valor}")
print("")
for chaves, valor in filme_veto.items():
    print(f"{chaves}:{valor}")
print("")
for chaves, valor in filme_fer.items():
    print(f"{chaves}:{valor}")
print("")
#-------------------------------------------------Exibir uma lista de dicionários
lista_filmes = [filme_martins,filme_veto,filme_fer]


     #Escolhendo os campos
for filme in lista_filmes:
    print(f"{filme['diretor']}")
    print("")
    
    #Exibindo todos
for filme in lista_filmes:
    for chaves, valor in filme.items():
        print(f"{chaves} - {valor}")
    print("")