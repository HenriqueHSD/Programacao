"""2- A série de Fibonacci é formada pela seguinte seqüência: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
etc. Escreva um algoritmo que gere a série de Fibonacci até o vigésimo termo.
"""

termo_anterior = 1
termo_atual = 1

print(termo_anterior)
print(termo_atual)

for _ in range(18):
    proximo_termo = termo_anterior + termo_atual
    print(proximo_termo)

    termo_anterior = termo_atual
    termo_atual = proximo_termo