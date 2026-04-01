"""
Leia um valor informado pelo usuário. Verifique o tipo da variável;
Caso seja possível interpretá-lo como um valor numérico:
    - Se for um número inteiro, exiba o dobro;
    - Caso seja um número real, exiba a metade;
Caso não seja possível interpretar como número, exiba: “Tipo inválido”.
"""

try:
    entrada = input("Digite um valor de entrada: ")
    print("o tipo de dado da entrada é:", type(entrada))
    if "." in entrada:
        value = float(entrada)
        print("A metade do número real é:", value / 2)
    else:
        value = int(entrada)
        print("O dobro do número inteiro é:", value * 2)
except ValueError:
    print("Tipo inválido")
