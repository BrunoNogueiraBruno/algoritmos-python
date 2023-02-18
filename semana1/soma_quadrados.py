# ENUNCIADO:
# Construir um programa que leia três valores numéricos inteiros
# (representados pelas variáveis A, B e C) e apresentar como resultado final,
# armazenado em memória, o valor da soma dos quadrados dos três valores lidos

# para ficar mais interessante tirei o limite de três valores

valores_input = input('Insira alguns valores: ').split(',')


def soma_quadrados(valores):
    soma = 0
    
    for valor in map(float, valores):
        soma += valor**2

    return soma


output = soma_quadrados(valores_input)

print(f'O resultado da soma dos valores é {output}')
