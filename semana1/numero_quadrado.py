# ENUNCIADO:
# Efetuar a leitura de um valor numérico inteiro e apresentar o
#resultado do valor lido ele-vado ao quadrado, sem efetuar o armazenamento do resultado em memória.

numero_input = input("Insira um número: ")


def numero_quadrado(numero):
    return float(numero) **2

output = numero_quadrado(numero_input)

print(f'O número {numero_input} ao quadrado é {output}')
