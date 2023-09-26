"""6- Leia a velocidade máxima permitida em uma avenida e a velocidade com que o
motorista estava dirigindo nela. Calcule e mostre a multa que uma pessoa vai receber,sabendo que são pagos:  R$ 50 reais se o motorista ultrapassar em até 10km/h a velocidade permitida; R$ 100 reais, se o motorista ultrapassar de 11 a 30 km/h a velocidade permitida; e R$ 200 reais, se estiver acima de 31km/h da velocidade permitida.
"""

def calcular_multa(velocidade_maxima, velocidade_motorista):
    limite_10 = velocidade_maxima + 10
    limite_30 = velocidade_maxima + 30

    if velocidade_motorista <= limite_10:
        multa = 50
    elif velocidade_motorista <= limite_30:
        multa = 100
    else:
        multa = 200

    return multa

velocidade_maxima = int(input("Digite a velocidade máxima permitida (em km/h): "))
velocidade_motorista = int(input("Digite a velocidade do motorista (em km/h): "))

multa = calcular_multa(velocidade_maxima, velocidade_motorista)
print("A multa a ser paga é de R$", multa)