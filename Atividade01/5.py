"""5- Crie um algoritmo que receba do usuário um número qualquer e verifique se esse é múltiplo de 5."""

numero = int(input("Digite um número: "))

if numero % 5 == 0:
    print(f"{numero} é um múltiplo de 5.")
else:
    print(numero, "não é um múltiplo de 5.")