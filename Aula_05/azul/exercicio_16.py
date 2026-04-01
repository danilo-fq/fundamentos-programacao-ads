"""
Leia um valor e: Mostre o tipo;
Se for numérico (após conversão) → mostre o quadrado.
"""


try:
    entrada = input("Digite um valor: ")

    print("O tipo da variavel entrada é:", type(entrada))

    valor = float(entrada)

    print("O quadrado do número de entrada é:", valor ** 2)
except ValueError:
    print("A entrada informada não é numérica!")
