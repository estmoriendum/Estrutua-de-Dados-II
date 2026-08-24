atividade 1 

numeros = []

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

print("\nNúmeros digitados:")
print(numeros)

soma = sum(numeros)

media = soma / 10

#encontra o maior e o menor valor
maior = max(numeros)
menor = min(numeros)

quantidade_pares = 0

for numero in numeros:
    if numero % 2 == 0:
        quantidade_pares += 1

print("\nResultados:")
print("Soma:", soma)
print("Média:", media)
print("Maior valor:", maior)
print("Menor valor:", menor)
print("Quantidade de números pares:", quantidade_pares)

-----------------------------------------------------------------------------------------------------------------------

atividade 2 

matriz = []

for i in range(3):
    linha = []

    for j in range(3):
        numero = int(input("Digite um número: "))
        linha.append(numero)

    matriz.append(linha)

print("\nMatriz:")

for i in range(3):
    print(matriz[i])

soma = 0

for i in range(3):
    for j in range(3):
        soma = soma + matriz[i][j]

soma_diagonal = 0

for i in range(3):
    soma_diagonal = soma_diagonal + matriz[i][i]

# Encontrando o maior elemento
maior = matriz[0][0]

for i in range(3):
    for j in range(3):
        if matriz[i][j] > maior:
            maior = matriz[i][j]

print("\nSoma de todos os elementos:", soma)
print("Soma da diagonal principal:", soma_diagonal)
print("Maior elemento:", maior)

-----------------------------------------------------------------------------------------------------------------------

atividade 3

livro = {}

livro["titulo"] = input("Digite o título do livro: ")
livro["autor"] = input("Digite o autor do livro: ")
livro["ano"] = int(input("Digite o ano do livro: "))
livro["preco"] = float(input("Digite o preço do livro: "))

print("\nDados do livro:")
print("Título:", livro["titulo"])
print("Autor:", livro["autor"])
print("Ano:", livro["ano"])
print("Preço:", livro["preco"])

#altera preço
novo_preco = float(input("\nDigite o novo preço: "))
livro["preco"] = novo_preco

livro["categoria"] = input("Digite a categoria do livro: ")

print("\nDados atualizados:")
print("Título:", livro["titulo"])
print("Autor:", livro["autor"])
print("Ano:", livro["ano"])
print("Preço:", livro["preco"])
print("Categoria:", livro["categoria"])

atividade 4

-----------------------------------------------------------------------------------------------------------------------

from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    matricula: int
    nota1: float
    nota2: float

    def media(self):
        return (self.nota1 + self.nota2) / 2


nome = input("Digite o nome: ")
matricula = int(input("Digite a matrícula: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

aluno = Aluno(nome, matricula, nota1, nota2)

print("\nNome:", aluno.nome)
print("Matrícula:", aluno.matricula)
print("Nota 1:", aluno.nota1)
print("Nota 2:", aluno.nota2)
print("Média:", aluno.media())


-----------------------------------------------------------------------------------------------------------------------

atividade 5

from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    matricula: int
    nota1: float
    nota2: float

    def media(self):
        return (self.nota1 + self.nota2) / 2

alunos = []

#cadastrar 
for i in range(5):
    print("\nCadastro do aluno", i + 1)

    nome = input("Digite o nome: ")
    matricula = int(input("Digite a matrícula: "))
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    aluno = Aluno(nome, matricula, nota1, nota2)

    alunos.append(aluno)

#media
print("\nMédia dos alunos:")

for aluno in alunos:
    print(aluno.nome, "- Média:", aluno.media())

#aprovados
print("\nAlunos aprovados:")

for aluno in alunos:
    if aluno.media() >= 7:
        print(aluno.nome, "- Média:", aluno.media())

#maior
maior_media = alunos[0]

for aluno in alunos:
    if aluno.media() > maior_media.media():
        maior_media = aluno


print("\nAluno com maior média:")
print("Nome:", maior_media.nome)
print("Média:", maior_media.media())


-----------------------------------------------------------------------------------------------------------------------

atividade 6

from dataclasses import dataclass

@dataclass
class Produto:
    codigo: int
    nome: str
    preco: float
    quantidade: int


# Lista de produtos
produtos = []

while True:

    print("\n===== SISTEMA DE ESTOQUE =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Valor total do estoque")
    print("5 - Produto mais caro")
    print("0 - Sair")

    escolha = input("Escolha: ")

    
    if escolha == "1":

        codigo = int(input("Digite o código: "))
        nome = input("Digite o nome: ")
        preco = float(input("Digite o preço: "))
        quantidade = int(input("Digite a quantidade: "))

        produto = Produto(codigo, nome, preco, quantidade)

        produtos.append(produto)

        print("Produto cadastrado com sucesso!")


    elif escolha == "2":

        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")

        else:
            print("\n===== PRODUTOS =====")

            for produto in produtos:
                print("Código:", produto.codigo)
                print("Nome:", produto.nome)
                print("Preço:", produto.preco)
                print("Quantidade:", produto.quantidade)
                print("--------------------")

    #busca
    elif escolha == "3":

        codigo_busca = int(input("Digite o código do produto: "))

        encontrado = False

        for produto in produtos:

            if produto.codigo == codigo_busca:
                print("\nProduto encontrado!")
                print("Código:", produto.codigo)
                print("Nome:", produto.nome)
                print("Preço:", produto.preco)
                print("Quantidade:", produto.quantidade)

                encontrado = True

        if encontrado == False:
            print("Produto não encontrado.")

    #total
    elif escolha == "4":

        total = 0

        for produto in produtos:
            total = total + (produto.preco * produto.quantidade)

        print("\nValor total do estoque:", total)

    #+ caro
    elif escolha == "5":

        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")

        else:
            mais_caro = produtos[0]

            for produto in produtos:

                if produto.preco > mais_caro.preco:
                    mais_caro = produto

            print("\n===== PRODUTO MAIS CARO =====")
            print("Código:", mais_caro.codigo)
            print("Nome:", mais_caro.nome)
            print("Preço:", mais_caro.preco)
            print("Quantidade:", mais_caro.quantidade)

    #sair
    elif escolha == "0":

        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")
