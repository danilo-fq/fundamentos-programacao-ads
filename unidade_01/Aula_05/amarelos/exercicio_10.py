"""
Leia um número e informe:
“Dentro do intervalo” se estiver entre 0 e 10;
“Fora do intervalo” caso contrário.
"""

num = float(input("Digite um número: "))

if num >= 0 and num <= 10:
    print("Dentro do intervalo")
else:
    print("Fora do intervalo")
