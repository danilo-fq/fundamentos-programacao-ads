"""
Leia um valor informado pelo usuário. Exiba o tipo da variável lida.
Verifique se é possível converter o valor para número real (float).
    - Se for possível, exiba o resultado da divisão desse
número por 2.
    - Caso contrário, exiba: “Não numérico”.
"""

try:
    entrada = input("Digite um valor de entrada: ")

    print("O tipo da entrada é:", type(entrada))

    valor_real = float(entrada)

    print("O resultado da divisão desse número por 2 é:", valor_real / 2)

except ValueError:
    print("Não numérico")
