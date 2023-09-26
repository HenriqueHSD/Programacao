"""8- Crie um algoritmo que, dada uma temperatura em graus célsius, exiba uma mensagem informando o tipo do clima, de acordo com as seguintes condições: se a temperatura estiver até 18 graus, o clima é frio; se a temperatura estiver entre 19 e 23 graus, o clima é agradável; se a temperatura estiver entre 24 e 35 graus, o clima é quente; se a temperatura estiver acima de 35 graus, o clima é muito quente."""

temperatura = float(input("Digite a temperatura em graus Celsius: "))

if temperatura <= 18:
    clima = "frio"
elif temperatura <= 23:
    clima = "agradável"
elif temperatura <= 35:
    clima = "quente"
else:
    clima = "muito quente"

print("O clima é", clima)