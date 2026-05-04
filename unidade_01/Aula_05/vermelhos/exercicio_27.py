"""
Leia dois números informados pelo usuário.
Se ambos forem positivos:
    - calcule e exiba a soma entre eles
Caso contrário, calcule e exiba o produto entre eles.
"""

num_1 = int(input("Digite um número: "))
num_2 = int(input("Digite um segundo número: "))

if num_1 > 0 and num_2 > 0:
    soma = num_1 + num_2
    print("A soma dos dois números é:", soma)
else:
    produto = num_1 * num_2
    print("O produto entre os dois números é:", produto)
