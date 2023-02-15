# ENUNCIADO:
# Efetuar o cálculo e apresentar o valor de uma prestação de um bem em atraso,
# utili-zando a fórmula PRESTAÇÃO ← VALOR + (VALOR * (TAXA / 100) * TEMPO).


KM_POR_LITRO = 12

valor_input = float(input("Insira o valor em R$ do bem em atraso: "))
taxa_input = float(input("Insira a taxa da prestação: "))
tempo_input = float(input("Insira o tempo de atraso: "))


def prestacao_atrasada(valor, taxa, tempo):
    prestacao = valor + (valor*(taxa/100) * tempo)
    return round(prestacao, 2)


prestacao_output = prestacao_atrasada(valor_input, taxa_input, tempo_input)


print(f'O valor da prestação do bem atrasado é de R$ {prestacao_output}')
