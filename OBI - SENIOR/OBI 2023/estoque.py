# Lê o número de tipos de roupas (linhas da matriz)
M = int(input())

# Lê o número de tamanhos de roupas (colunas da matriz)
N = int(input())

# Cria a matriz de estoque (inicialmente vazia)
matriz = []

# Preenche a matriz com os valores de estoque
for i in range(M):
    linhas = []  # Lista para armazenar os valores da linha i
    for j in range(N):
        valor = int(input())  # Lê o valor de estoque para o tipo i+1 e tamanho j+1
        linhas.append(valor)  # Adiciona o valor à linha
    matriz.append(linhas)  # Adiciona a linha completa à matriz

# Lê o número de pedidos realizados
P = int(input())

# Inicializa a variável que vai contar as vendas feitas com sucesso
pecas = 0

# Processa cada pedido
for _ in range(P):
    linha = int(input())    # Lê o tipo da roupa (1 até M)
    coluna = int(input())   # Lê o tamanho da roupa (1 até N)

    # Verifica se há estoque disponível para o tipo e tamanho pedidos
    if matriz[linha - 1][coluna - 1] > 0:
        matriz[linha - 1][coluna - 1] -= 1  # Reduz o estoque em 1
        pecas += 1  # Incrementa a contagem de peças vendidas

# Exibe o total de peças efetivamente vendidas
print(pecas)
