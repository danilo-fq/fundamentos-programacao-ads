"""
Leia um valor e: verifique se eles está entre 0 e 100, caso o
número esteja fora do intervalo, mostre na tela o valor.
"""

num = int(input("Digite um número: "))

if not (num >= 0 and num <= 100):
    print("O valor do número é:", num)
