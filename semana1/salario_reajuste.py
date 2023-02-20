# ENUNCIADO:
# Elaborar um programa que leia o valor numérico correspondente ao
# salário mensal (variável SM) de um trabalhador e também fazer a
# leitura do valor do percentual de reajuste (variável PR) a ser atribuído.
# Apresentar o valor do novo salário (variável NS) após o armazenamento do cálculo em memória

salario_input = input('Insira o salário mensal: ')
percentual_input = input('Insira valor do percentual de reajuste: ')


def reajustar_salario(salario, percentual):
    return float(salario) * (1 + float(percentual) / 100)


salario_output = reajustar_salario(salario_input, percentual_input)

print(f'O valor do salário reajustado é de {salario_output}')
