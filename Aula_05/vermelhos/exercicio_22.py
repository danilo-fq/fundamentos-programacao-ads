"""
Leia um valor informado pelo usuário. Tente convertê-lo para número inteiro.
    - Caso não seja possível realizar a conversão, exiba: “Entrada inválida”.
    - Caso a conversão seja bem-sucedida:
        - Se o número for maior que 10, exiba: “Alto”.
        - Caso contrário, exiba: “Baixo”.
"""

try:
    entrada = int(input("Digite um valor de entrada: "))
    if entrada > 10:
        print("Alto")
    else:
        print("Baixo")
except ValueError:
    print("Entrada inválida")
