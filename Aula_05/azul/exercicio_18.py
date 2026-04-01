"""
Leia um número e: Mostre se ele é par positivo,
par negativo, impar positivo, impar negativo ou
neutro.
"""

num = int(input("Digite um número: "))

if num > 0:
    if num % 2 == 0:
        print("par positivo")
    else:
        print("ímpar positivo")
elif num < 0:
    if num % 2 == 0:
        print("par negativo")
    else:
        print("ímpar negativo")
else:
    print("neutro")
