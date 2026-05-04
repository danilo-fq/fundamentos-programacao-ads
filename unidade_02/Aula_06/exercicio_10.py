"""
Defina um número fixo no código. Peça ao usuário para adivinhar até acertar. Informe se o palpite é maior ou menor que o número correto.
"""

numero_correto = 22

numero = int(input("Digite um numero: "))

while (numero != numero_correto):

    if (numero > numero_correto):

        print("O seu palpite é maior do que o número correto")

    else:

        print("O seu palpite é menor do que o número correto")

    numero = int(input("Digite outro numero: "))

print("Você acertou, o número correto é o: ", numero_correto)
