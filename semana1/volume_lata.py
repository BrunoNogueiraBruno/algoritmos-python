# ENUNCIADO:
# Calcular e apresentar o valor do volume de uma lata de óleo,
# utilizando a fórmula VOLUME ← 3.14159 * R ↑ 2 * ALTURA.

import math
PI = math.pi

raio_input = float(input("Insira o raio da lata de óleo: "))
altura_input = float(input("Insira a altura da lata de óleo: "))


def volume_lata(raio, altura):
    volume = PI * (raio**2) * altura
    return round(volume, 2)


volume_output = volume_lata(raio_input, altura_input)


print(f'O volume da lata de óleo é de {volume_output} unidades cúbicas')
