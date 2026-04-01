"""
Leia três números inteiros informados pelo usuário.
Exiba em ordem decrescente o resto da divisão por 3.
"""

num_1 = int(input("Digite um número: "))
num_2 = int(input("Digite um segundo número: "))
num_3 = int(input("Digite um terceiro número: "))

mod_por_3_num_1 = num_1 % 3
mod_por_3_num_2 = num_2 % 3
mod_por_3_num_3 = num_3 % 3

if (mod_por_3_num_1 > mod_por_3_num_2 and mod_por_3_num_1 > mod_por_3_num_3):
    if mod_por_3_num_2 > mod_por_3_num_3:
        print(
            mod_por_3_num_1,
            mod_por_3_num_2,
            mod_por_3_num_3
        )
    else:
        print(
            mod_por_3_num_1,
            mod_por_3_num_3,
            mod_por_3_num_2
        )
elif mod_por_3_num_2 > mod_por_3_num_3:
    if mod_por_3_num_1 > mod_por_3_num_3:
        print(
            mod_por_3_num_2,
            mod_por_3_num_1,
            mod_por_3_num_3
        )
    else:
        print(
            mod_por_3_num_2,
            mod_por_3_num_3,
            mod_por_3_num_1
        )
else:
    if mod_por_3_num_1 > mod_por_3_num_2:
        print(
            mod_por_3_num_3,
            mod_por_3_num_1,
            mod_por_3_num_2
        )
    else:
        print(
            mod_por_3_num_3,
            mod_por_3_num_2,
            mod_por_3_num_1
        )
