"""
Peça várias notas ao usuário (encerra quando digitar -1) e calcule a média das notas válidas.
"""

nota = float(input("Digite uma nota: "))

quantidade_notas = 0

soma_notas = 0

while (nota != -1):

    quantidade_notas += 1

    soma_notas += nota

    nota = float(input("Digite outra nota: "))

if (quantidade_notas == 0):
    print("A nota precisa ser um valor positivo")
else:
    media = soma_notas / quantidade_notas
    print("A média das notas é: ", media)
