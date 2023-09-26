#1 Receba uma string informada pelo usuário e exiba cada caractere informado em uma linha diferente.
palavra = input("Digite alguma palavra:")
print(palavra.replace("", "\n"))

#2 E-mail: vamos validar um padrão de e-mail informado pelo usuário
#A. Deve conter um caractere @
#B. O @ não pode ser o primeiro caractere
#C. O @ Não pode ser o último caractere (Dica função len retorna o tamanho de uma string)
#D. Deve terminar com .com
#C. Conter no mínimo 10 caracteres.

import re

def validar_email(email):

    if '@' not in email:
        return False

    if email.index('@') == 0:
        return False

    if email.index('@') == len(email) - 1:
        return False

    if not email.endswith('.com'):
        return False

    if len(email) < 10:
        return False

    return True

email = input("Digite um endereço de e-mail: ")

if validar_email(email):
    print("O e-mail é válido.")
else:
    print("O e-mail é inválido.")