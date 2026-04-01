"""
Leia um número e: Se for par e positivo → “Par positivo”;
Se for par e negativo → “Par negativo”;
Caso contrário → “Ímpar”.
"""

num = int(input("Digite um número: "))

if num > 0 and num % 2 == 0:
    print("Par positivo")
elif num < 0 and num % 2 == 0:
    print("Par negativo")
elif num == 0:
    print("Par e neutro")
else:
    print("Ímpar")
