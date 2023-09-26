"""3- Escreva um algoritmo que leia um conjunto de 20 números inteiros e mostre qual foi o
maior e o menor valor fornecido.
"""

maior = float('-inf')
menor = float('inf')

for _ in range(20):
    numero = int(input("Digite um número inteiro: "))

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

print("O menor valor fornecido é: ",menor)
print("O maior valor fornecido é: ",maior)