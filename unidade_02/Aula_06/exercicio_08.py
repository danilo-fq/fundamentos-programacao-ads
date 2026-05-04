"""
Peça um número e mostre a tabuada dele de 1 a 10.
"""

numero = int(input("Digite um número: "))

indice = 1

while indice <= 10:

    print(numero, " x ", indice, " = ", indice * numero)

    indice += 1
