"""
Construa um algoritmo que receba a altura e o peso de
uma pessoa e calcule o Índice de Massa Corporal (IMC).
"""

altura = float(input("Digite a altura em metros (m): "))
peso = float(input("Digite o peso em quilogramas (kg): "))

imc = peso / (altura ** 2)

print("O resultado do IMC é:", imc)
