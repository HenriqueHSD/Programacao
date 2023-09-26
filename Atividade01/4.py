"""4- Imprima uma tabela de conversão de polegadas para centímetros, de 1 a 20. Considere
que Polegada = Centímetro * 2,54.
"""

def polegada_para_cm(polegadas):
    return polegadas * 2.54

print("Polegadas\Centímetros")

for polegadas in range(1, 21):
    centimetros = polegada_para_cm(polegadas)
    print(f"{polegadas}\t\t{centimetros:.2f}")