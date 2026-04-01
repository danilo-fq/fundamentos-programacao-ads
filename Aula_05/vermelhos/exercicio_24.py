"""
Leia um número inteiro. Verifique se ele está no
intervalo de 1 a 100 (inclusive). Se estiver:
    - Verifique se o número é par ou ímpar;
        Exiba: “Par no intervalo” ou “Ímpar no intervalo”.
    - Caso não esteja no intervalo,
        Exiba: “Fora do intervalo”.
"""

num = int(input("Digite um número: "))

if num >= 1 and num <= 100:
    if num % 2 == 0:
        print("Par no intervalo")
    else:
        print("Ímpar no intervalo")
else:
    print("Fora do intervalo")
