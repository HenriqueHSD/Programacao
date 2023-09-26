"""7- Escreva um algoritmo que leia dois números e apresente um menu de opções como o mostrado abaixo: a. Leia a opção do usuário e execute a operação com os dois números lidos anteriormente.

"""

def soma(a, b):
    return a + b

def diferenca(a, b):
    return abs(a - b)

def produto(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não é permitida"

print("Digite dois números:")
num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))

print("Escolha a opção:")
print("1 - Soma de 2 números.")
print("2 - Diferença entre 2 números (maior pelo menor).")
print("3 - Produto entre 2 números.")
print("4 - Divisão entre 2 números (o denominador não pode ser zero).")

opcao = int(input("Opção: "))

if opcao == 1:
    resultado = soma(num1, num2)
elif opcao == 2:
    resultado = diferenca(max(num1, num2), min(num1, num2))
elif opcao == 3:
    resultado = produto(num1, num2)
elif opcao == 4:
    resultado = divisao(num1, num2)
else:
    resultado = "Opção inválida"

print("Resultado:", resultado)