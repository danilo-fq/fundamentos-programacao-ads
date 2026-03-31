"""
Construa um algoritmo que receba o valor de um produto
e calcule o preço final considerando um acréscimo de 8% de imposto.
"""

valor_prod = float(input("Digite o primeiro número: "))

preco_final = valor_prod * (1 + 0.08)

print("O preço final com 8% de imposto será:", preco_final)
