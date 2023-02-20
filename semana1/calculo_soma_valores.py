# ENUNCIADO:
# Elaborar um programa que leia quatro valores numéricos inteiros (variáveis A, B, C e D).
# Ao final, o programa deve apresentar o resultado, armazenado em memória, do
# produto (variável P) do primeiro com o terceiro valor, e o resultado da soma (variável S)
# do segundo com o quarto valor

# para ficar mais interessante tirei o limite de quatro valores

valores_input = input('Insira um número par de valores: ').split(',')


def calculo_soma_valores(valores):
    index = 0

    valores_para_multiplicar = []
    valores_para_somar = []

    for valor in map(float, valores):
        
        if (index % 2 == 0):
            valores_para_multiplicar.append(valor)
        else:
            valores_para_somar.append(valor)

        index += 1

    multiplicacao = [a*b for a, b in zip(valores_para_multiplicar[:-1], valores_para_multiplicar[1:])][0]
    soma = [a+b for a, b in zip(valores_para_somar[:-1], valores_para_somar[1:])][0]

    return multiplicacao, soma


if (len(valores_input) % 2 != 0):
    print(f'Você deve inserir um número par de valores')
else:
    multiplicacao, soma = calculo_soma_valores(valores_input)
    print(f'O produto dos valores de index ímpar é de {multiplicacao}, já a soma dos valores de index par é de {soma}')
