atividade 1

# Criando uma lista vazia
numeros = []

# Pedindo 10 números ao usuário
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

# Exibindo todos os números
print("\nNúmeros digitados:")
print(numeros)

# Calculando a soma
soma = sum(numeros)

# Calculando a média
media = soma / 10

# Encontrando o maior e o menor valor
maior = max(numeros)
menor = min(numeros)

# Contando os números pares
quantidade_pares = 0

for numero in numeros:
    if numero % 2 == 0:
        quantidade_pares += 1

# Exibindo os resultados
print("\nResultados:")
print("Soma:", soma)
print("Média:", media)
print("Maior valor:", maior)
print("Menor valor:", menor)
print("Quantidade de números pares:", quantidade_pares)

atividade 2 

Dito pelo ChatGPT:
Claro! Para fazer no Google Colab de uma forma simples, como iniciante, você pode usar uma matriz (lista de listas) e dois for.

Código
# Criando uma matriz 3x3
matriz = []

# Pedindo os valores para o usuário
for i in range(3):
    linha = []

    for j in range(3):
        numero = int(input("Digite um número: "))
        linha.append(numero)

    matriz.append(linha)

# Exibindo a matriz
print("\nMatriz:")

for i in range(3):
    print(matriz[i])

# Calculando a soma de todos os elementos
soma = 0

for i in range(3):
    for j in range(3):
        soma = soma + matriz[i][j]

# Calculando a soma da diagonal principal
soma_diagonal = 0

for i in range(3):
    soma_diagonal = soma_diagonal + matriz[i][i]

# Encontrando o maior elemento
maior = matriz[0][0]

for i in range(3):
    for j in range(3):
        if matriz[i][j] > maior:
            maior = matriz[i][j]

# Exibindo os resultados
print("\nSoma de todos os elementos:", soma)
print("Soma da diagonal principal:", soma_diagonal)
print("Maior elemento:", maior)
