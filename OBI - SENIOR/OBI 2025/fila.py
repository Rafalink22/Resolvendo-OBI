N = int(input())  #Número de alunos
alturas = [] #Lista de altura dos alunos

for _ in range(N):
    alturas.append(int(input()))  #Lê as alturas

alunos_nao_vistos = 0 #Contador de alunos não vistos
maior_altura = 0  #Começa do menor possível

#Percorrer de trás pra frente
for i in range(N -1, -1, -1):
    if alturas[i] <= maior_altura:
        alunos_nao_vistos += 1  #Está escondido
    else:
        maior_altura = alturas[i]  #Atualiza o maior visto até agora

print(alunos_nao_vistos)
