"""
Leia um número e: Se for maior que 100 → mostre metade;
Senão → mostre o dobro.
"""

num = int(input("Digite um número: "))

if num > 100:
    print("A metade do número é:", num / 2)
else:
    print("O dobro do número é:", num * 2)
