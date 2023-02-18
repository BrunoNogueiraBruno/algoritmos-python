# ENUNCIADO:
# Elaborar um programa que apresente o valor da conversão em dólar (US$)
# de um valor lido em real (R$). O programa deve solicitar o valor da
# cotação do dólar e também a quantidade de reais disponível com o
# usuário e armazenar em memória o valor da con-versão antes da apresentação

cotacao_input = input("Insira a cotação do dolar: ")
real_input = input("Insire a quantidade de reais: ")

def real_para_dolar(cotacao, real):
    return float(real) / float(cotacao)

output = real_para_dolar(cotacao_input, real_input)

print(f'{real_input} reais equivalem a {output} dolares')
