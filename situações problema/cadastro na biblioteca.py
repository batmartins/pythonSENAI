def cadastro(livros):
    isbn = int(input("digite o código do livro"))
    titulo =input("digite o título do livro")
    autor =input("digite o autor do livro")
    categoria =input("digite a categoria do livro")
    ano_de_publico =int(input("digite o ano de publicação do livro"))
    livro = {
        "isbn" : isbn,
        "titulo" :titulo,
        "autor" :autor,
        "categoria" :categoria,
        "ano de publicação" :ano_de_publico,
        }
    livros.append(livro)

    
livros = []
print("menu de funções")
print('')
print("digite 0 para sair")
print("digite 1 para cadastrar um livro")
print("digite 2 para visualizar a lista de livros cadastrados")
print("digite 3 para saber a quantidade total de livros cadastrados")
print("digite 4 para a lista de títulos")
print('')
while True:
    escolha = int(input("digite sua escolha"))
    if escolha == 0:
        print("você saiu")
        break
    elif escolha == 1:
        cadastro(livros)
        print("livro cadastrado com sucesso")
    elif escolha == 2:
        for livro in livros:
            for chave, valor in livro.items():
                print(f"{chave}-{valor}")
    elif escolha == 3:
        print(len(livros))
    elif escolha == 4:
        for livro in livros:
            print(livro["titulo"])