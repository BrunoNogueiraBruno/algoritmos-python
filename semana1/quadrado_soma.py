# ENUNCIADO:
# Construir um programa que leia três valores numéricos inteiros
# (representados pelas variáveis A, B e C) e apresentar como resultado
# final, armazenado em memória, o valor do quadrado da soma dos três valores lidos.

# para ficar mais interessante tirei o limite de três valores

valores_input = input('Insira alguns valores: ').split(',')


def quadrado_soma(valores):
    soma = 0
    
    for valor in map(float, valores):
        soma += valor

    return soma ** 2


output = quadrado_soma(valores_input)

print(f'O resultado do quadrado da soma dos valores é {output}')
