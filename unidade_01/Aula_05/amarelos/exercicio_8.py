"""
Leia um número e: Se for positivo,
mostre a raiz aproximada (use **0.5); Caso contrário,
informe “Número inválido”
"""

num = float(input("Digite um número: "))


if num > 0:
    print(num ** 0.5)
else:
    print("Número inválido")
