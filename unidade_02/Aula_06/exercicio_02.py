"""
Peça ao usuário para digitar uma senha. Continue solicitando até que ele acerte a senha correta (defina uma senha fixa no código).
"""
senha_secreta = "programacao"

senha = input("Digite uma senha: ")

while (senha != senha_secreta):

    print("senha incorreta!")

    senha = input("Digite outra senha: ")
    
print("Parabéns a senha secreta é: ", senha_secreta)
