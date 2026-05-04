"""
Peça números ao usuário até que ele digite 0. Ao final, informe quantos números positivos e quantos negativos foram digitados.
"""

numero = float(input("Digite um número: "))

quantidade_positivos = 0

quantidade_negativos = 0

while (numero != 0):

    if (numero > 0):

        quantidade_positivos += 1

    else:

        quantidade_negativos += 1

    numero = float(input("Digite outro número: "))

print("Quantidade números positivos:", quantidade_positivos)

print("Quantidade números negativos:", quantidade_negativos)
