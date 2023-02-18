# ENUNCIADO:
# Elaborar um programa que apresente o valor da conversão em real (R$)
# de um valor lido em dólar (US$). O programa deve solicitar o valor da
# cotação do dólar e também a quan-tidade de dólares disponível com o
# usuário e armazenar em memória o valor da conver-são antes da apresentação.

cotacao_input = input("Insira a cotação do dolar: ")
dolar_input = input("Insire a quantidade de dólares: ")

def dolar_para_real(cotacao, dolar):
    return float(cotacao) * float(dolar)

output = dolar_para_real(cotacao_input, dolar_input)

print(f'{dolar_input} dólares equivalem a {output} reais')
