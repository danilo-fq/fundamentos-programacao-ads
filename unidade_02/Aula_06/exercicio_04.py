"""
Peça números ao usuário e some-os. O programa deve parar quando o usuário digitar um número negativo. Ao final, mostre a soma total.
"""

numero = float(input("Digite um número: "))

soma = 0

while numero >= 0:

    soma += numero

    numero = float(input("Digite outro número: "))
    
print("O total da soma é: ", soma)
