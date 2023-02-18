# ENUNCIADO:
# Ler dois valores numéricos inteiros (representados pelas variáveis A e B) e
# apresentar o resultado armazenado em memória do quadrado da diferença do
# primeiro valor (variável A) em relação ao segundo valor (variável B).

numeros_input = input("Insira dois valores: ").split(',')

def quadrado_diferenca(numero):
    a, b = map(float, numero)
    print(a, b)
    return (a - b)**2

output = quadrado_diferenca(numeros_input)

print(f'O quadrado da diferença de {numeros_input[0]} em relação a {numeros_input[1]} é {output}')
