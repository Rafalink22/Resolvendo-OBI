A = int(input())  # Tamanho da lista1 (SA)
B = int(input())  # Tamanho da lista2 (SB)

lista1 = []
lista2 = []

# Lendo a lista SA
for _ in range(A):
    lista1.append(int(input()))

# Lendo a lista SB
for _ in range(B):
    lista2.append(int(input()))

j = 0  # Índice da lista2 (SB)

# Percorrer lista1 (SA)
for item in lista1:
    if j < B and item == lista2[j]:
        j += 1  # Avança na SB se achar o próximo valor da subsequência

# Verifica se percorremos toda a SB
if j == B:
    print('S')
else:
    print('N')
