# ENUNCIADO:
# Elaborar um programa que calcule e apresente o valor do volume de uma caixa retangular,
# utilizando a fórmula VOLUME ← COMPRIMENTO * LARGURA * ALTURA

valores_input = input("Respectivamente, insira Comprimento, Largura e Altura de uma caixa retangular: ").split(',')


def calcular_volume(valores):
    comprimento, largura, altura = valores
    return float(comprimento) * float(comprimento) * float(altura)


if len(valores_input) == 3:
    output = calcular_volume(valores_input)
    print(f'O volume da caixa é de {output}')

else:
    print('Você precisa inserir 3 valores')
