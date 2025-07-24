V = int(input())
A = int(input())
F = int(input())
P = int(input())

contas = [A, F, P]

contas.sort()

if contas[0] + contas[1] + contas[2] <= V:
    print(3)
elif contas[0] + contas[1] <= V:
    print(2)
elif contas[0] <= V:
    print(1)
else:
    print(0)