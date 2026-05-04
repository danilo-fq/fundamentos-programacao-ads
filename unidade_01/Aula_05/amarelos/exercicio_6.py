"""
Leia dois números e exiba qual é o maior.
"""

num_1 = int(input("Digite um número: "))
num_2 = int(input("Digite um segundo número: "))

if num_1 > num_2:
    print("O maior número é o:", num_1)
elif num_2 > num_1:
    print("O maior número é o:", num_2)
else:
    print("Os números são idênticos!")
