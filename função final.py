#• O usuário possa informar o nome do aluno.
#• O sistema receba três notas e calcule a média automaticamente.
#• Com base na média, o sistema deve indicar se o aluno está "Aprovado" (média ≥ 7), "Recuperação" (entre 5 e 6.9) ou "Reprovado" (média < 5).
#• O sistema deve permitir o cadastro de vários alunos e exibir um resumo final com o nome de cada aluno e sua situação.
print("Sistema de notas de alunos")
print("")
def exibir_menu():
    print("digite 1 para calcular a média")
    print("digite 2 para cadastrar o nome do aluno")
    print("digite 3 para exibir o resumo final")
    print("digite 0 para sair")
def calcular_media(n1, n2, n3):

    media_ = (n1 + n2 + n3)/3
    return media_
def verificar_situacao(media):
    if calcular_media(n1, n2, n3) >= 7:
        return f"aprovado"
    elif calcular_media(n1, n2, n3) <7 and calcular_media(n1, n2, n3) >=5:
        return  f"recuperação"
    else:
        return f"reprovado"
def cadastrar_aluno(alunos):
    nome = input("Digite o nome ")
    aluno = {
        "nome" : nome,
        }
    m = calcular_media(n1 ,n2 ,n3)
    s = verificar_situacao(m)
    aluno["media"] = m
    aluno["situação"] = s
#adicionar o dicionário à lista
    alunos.append(aluno)
def mostrar_relatorio(alunos):
    for aluno in alunos:
        for chave, valor in aluno.items():
            print(f"{chave}-{valor}")

#criar a lista vazia
alunos = []

#CÓDIGO
while True:
    #exibir o menu 
    exibir_menu()
    escolha = int(input("digite sua escolha"))
    if escolha == 0:
        print("você saiu")
        break
    elif escolha == 2:
        cadastrar_aluno(alunos)
        print("cadastro concluído")
    elif escolha == 1:
        n1 = float(input("digite a primeira nota"))
        n2 = float(input("digite a segunda nota"))
        n3 = float(input("digite a terceira nota"))
        verificar_situacao(calcular_media(n1, n2, n3))
        print("cadastrado")
    elif escolha == 3:
        mostrar_relatorio(alunos)
    else:
        print("escolha inválida")