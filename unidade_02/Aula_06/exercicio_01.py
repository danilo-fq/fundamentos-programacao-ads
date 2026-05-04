"""
Solicite uma nota entre 0 e 10. Continue pedindo até que o usuário informe um valor válido.
"""

nota = int(input("Digite uma nota entre 0 e 10: "))

while (nota < 0 or nota > 10):

    print("valor invalido!")

    nota = int(input("Digite uma nota entre 0 e 10: "))

print("sua nota é: ", nota)
