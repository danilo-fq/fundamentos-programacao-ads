"""
Peça vários números ao usuário (encerra com 0) e informe qual foi o maior número digitado.
"""

numero = float(input("Digite um número: "))

maior_numero = 0

while (numero != 0):

    if (numero > maior_numero):

        maior_numero = numero

    numero = float(input("Digite outro número: "))
    
print("Maior número digitado: ", maior_numero)
