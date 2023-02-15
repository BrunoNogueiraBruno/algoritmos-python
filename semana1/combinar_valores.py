# ENUNCIADO:
# Ler quatro valores numéricos inteiros e apresentar os resultados
# armazenados em memória das adições e multiplicações utilizando o
# mesmo raciocínio aplicado quando do uso de propriedades distributivas
# para a máxima combinação possível entre as quatro variáveis.
# Não é para calcular a propriedade distributiva, deve-se apenas
# usar a sua forma de combinação. Considerando a leitura de valores para
# as variáveis A, B, C e D, devem ser feitas seis adições e seis
# multiplicações, ou seja, deve ser combinada a variável A com a
# variável B, a variável A com a variável C, a variável A com a variável D.
# Depois, é necessário combinar a variável B com a variável C e a
# variável B com a variável D e, por fim, a variável C será combinada com a variável D.

valores_input = input("Insira os 4 valores inteiros separados por vírgula: ").split(',')


def printar_valores(termo_um, termo_dois):
    termo_um_nome, termo_um_valor = termo_um
    termo_dois_nome, termo_dois_valor = termo_dois

    adicao = termo_um_valor + termo_dois_valor
    multiplicacao = termo_um_valor * termo_dois_valor
    
    print(f'{termo_um_nome}({termo_um_valor}) + {termo_dois_nome}({termo_dois_valor}) = {adicao}')
    print(f'{termo_um_nome}({termo_um_valor}) * {termo_dois_nome}({termo_dois_valor}) = {multiplicacao}')


def checar_nome_variavel(index):
    variaveis = ['A','B','C','D']
    return variaveis[index]


def obter_tupla_valores(valores):
    index = 0
    
    lista_tuplas = []

    for valor in valores:
        nome = checar_nome_variavel(index)
        tupla = (nome, int(valor))

        lista_tuplas.append(tupla)

        index += 1
    
    return lista_tuplas


def combinar_valores(valores):
    tuplas = obter_tupla_valores(valores) # os valores no tipo tupla são necessários para armazenarmos também o nome da variável, o que vai ser útil na exibição das combinações
    valores_para_combinar = tuplas[:] # é muito importante usar o [:], assim a variável é copiada ao invés de ser dependente da original, assim uma mudança em valores_para_combinar não afeta valores_inteiros

    index = 0
    for nome_termo_um, valor_termo_um in tuplas:
        termo_um = (nome_termo_um, valor_termo_um)

        del valores_para_combinar[index] # a função del serve para remover o valor atual da lista de combinação, dessa forma evitando que os números se repitam (ex.: A+A)

        index += 1

        for nome_termo_dois, valor_termo_dois in valores_para_combinar:
            termo_dois = (nome_termo_dois, valor_termo_dois)

            printar_valores(termo_um, termo_dois)

        valores_para_combinar = tuplas[:]


if len(valores_input) == 4:
    combinar_valores(valores_input)

else:
    print('Você precisa inserir 4 valores')
