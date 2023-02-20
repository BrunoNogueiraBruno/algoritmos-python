# ENUNCIADO:
# Elaborar um programa que calcule e apresente o valor do resultado da
# área de uma circunferência (variável A). O programa deve solicitar
# a entrada do valor do raio da circunferência (variável R). Para a
# execução deste problema, utilize a fórmula A ← 3.14159265* R ↑ 2

import math
PI = math.pi

raio_input = input('Insira o valor do raio da circunferência: ')


def calcular_area(raio):
    return PI * float(raio)**2


area_output = calcular_area(raio_input)
print(f'O valor da área da circunferência é de {area_output}')
