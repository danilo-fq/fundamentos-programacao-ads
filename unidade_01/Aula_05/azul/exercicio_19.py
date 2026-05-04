"""
Leia dois números e: Verifique se são iguais ou diferentes.
Sendo diferentes mostre a diferença entre eles.
"""

num_1 = int(input("Digite um número: "))
num_2 = int(input("Digite um segundo número: "))

if not (num_1 == num_2):
    dif = num_1 - num_2
    print("A diferença entre os números é:", dif)
