V = int(input()) #Valor disponível
A = int(input()) #Conta do Açougue
F = int(input()) #Conta da Farmácia
P = int(input()) #Conta da Padaria

contas = [A, F, P] #Lista das contas

contas.sort() #Ordena as contas

#Verifica quantas contas podem ser pagas
if contas[0] + contas[1] + contas[2] <= V:
    print(3) #Todas as 3 contas
elif contas[0] + contas[1] <= V:
    print(2) #Duas menores contas
elif contas[0] <= V:
    print(1) #A menor conta
else:
    print(0) #Nenhuma conta
