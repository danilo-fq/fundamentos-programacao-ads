"""
Leia idade e: Mostre: Menor de idade (<18);
Adulto (18 a 59); Idoso (60+).
"""

idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Menor de idade")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")
