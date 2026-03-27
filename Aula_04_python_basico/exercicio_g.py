"""
Construa um algoritmo que receba a quantidade de horas trabalhadas por um
funcionário e o valor da hora trabalhada, calculando o salário total.
"""

qtd_horas_trabalhadas = float(
    input("Digite a quantidade de horas trabalhadas: ")
)

valor_hora_trabalhada = float(
    input("Digite o valor da hora trabalhada em reais: ")
)

salario_total = qtd_horas_trabalhadas * valor_hora_trabalhada

print("O valor do salário total será: R$", salario_total, sep="")
