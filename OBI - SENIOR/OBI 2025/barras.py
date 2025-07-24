N = int(input())  #Número de colunas
lista_pop = []  #Lista com os valores da popularidade

for _ in range(N):
    lista_pop.append(int(input()))

H = max(lista_pop)  #Altura máxima

matriz = []

for i in range(H):  #Linha
    linha = []
    for j in range(N):  #Coluna
        if H - i <= lista_pop[j]:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)

#Imprimir o gráfico
for linha in matriz:
    print(" ".join(map(str, linha)))
