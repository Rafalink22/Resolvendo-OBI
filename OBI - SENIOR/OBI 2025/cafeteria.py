#A = mínimo de leite desejado
#B = máximo de leite desejado
#C = capacidade total da xícara
#D = volume de café por dose

A = int(input())
B = int(input())
C = int(input())
D = int(input())

doses_maxima = C // D  #Máximo de doses de café que cabem na xícara

#Vamos testar de 0 até doses_maxima
for doses in range(doses_maxima + 1):
    volume_cafe = doses * D
    volume_leite = C - volume_cafe
    
    if A <= volume_leite <= B:
        print("S")
        break
else:
    #Se o laço terminar sem dar break, então nenhuma opção serviu
    print("N")
