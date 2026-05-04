"""
Peça números ao usuário continuamente e informe se cada número é par ou ímpar. O programa só deve parar quando o usuário digitar 0.
"""

numero = float(input("Digite um número: "))

while (numero != 0):

    if (numero % 2 == 0):

        print("O número", numero, "é par!")

    else:
        print("O número", numero, "é ímpar!")
        
    numero = float(input("Digite outro número: "))
