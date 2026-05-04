"""
Leia dois números e: Mostre a soma;
Mostre qual é maior ou se são iguais.
"""

num_1 = float(input("Digite um número: "))
num_2 = float(input("Digite um segundo número: "))
soma = num_1 + num_2

if num_1 > num_2:
    print("Soma:", soma, ", o maior número é o:", num_1)
elif num_2 > num_1:
    print("Soma:", soma, ", o maior número é o:", num_2)
else:
    print("Soma:", soma, ", os números são iguais!")
