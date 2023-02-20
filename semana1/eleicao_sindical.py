# ENUNCIADO:
# Em uma eleição sindical concorreram ao cargo de presidente três candidatos
# (representados pelas variáveis A, B e C). Durante a apuração dos votos foram
# computados votos nulos e em branco, além dos votos válidos para cada candidato.
# Deve ser criado um programa de computador que faça a leitura da quantidade de
# votos válidos para cada candidato, além de ler também a quantidade de votos
# nulos e em branco. Ao final, o programa deve apresentar o número total de eleitores,
# considerando votos válidos, nulos e em branco; o percentual correspondente de
# votos válidos em relação à quantidade de eleitores; o percentual correspondente
# de votos válidos do candidato A em relação à quantidade de eleitores; o percentual
# correspondente de votos válidos do candidato B em relação à quantidade de eleitores;
# o percentual correspondente de votos válidos do candidato C em relação à quantidade
# de eleitores; o percentual correspondente de votos nulos em relação à quantidade de
# eleitores; e, por último, o percentual correspondente de votos em branco em relação
# à quantidade de eleitores. Todos os cálculos devem efetivamente ser armazenados em memória.

votos_input = input('Insira a lista dos votos separdos por vírgula, "A", "B" e "C" correspondem respectivamente aos candidatos: "Ana", "Bruno" e "Carlos", além deles é possível também optar por "BRANCO" e "NULO": ').split(',')

    
def contar_votos(votos):
    votos_computados = { 'A': 0, 'B': 0, 'C': 0, 'BRANCO': 0, 'NULO': 0}
    total = 0
    
    for voto in votos:
        votos_computados[voto] += 1
        total += 1
        
    return votos_computados, total


def calcular_percentual(votos, total, opcao):
    valor_opcao = votos[opcao]
    return (valor_opcao / total) * 100


votos, total = contar_votos(votos_input)

total_votos_validos = total - (votos['BRANCO'] + votos['NULO'])
percentual_votos_validos = round((total_votos_validos / total) * 100)

percentual_A = round((votos['A'] / total) * 100)
percentual_B = round((votos['B'] / total) * 100)
percentual_C = round((votos['C'] / total) * 100)
percentual_NULO = round((votos['NULO'] / total) * 100)
percentual_BRANCO = round((votos['BRANCO'] / total) * 100)

print(f'O total de votos é de {total}')
print(f'O percentual de votos válidos é de {percentual_votos_validos}%')
print(f'A candidata Ana recebeu {percentual_A}% dos votos')
print(f'O candidato Bruno recebeu {percentual_B}% dos votos')
print(f'O candidato Carlos recebeu {percentual_C}% dos votos')
print(f'O percentual de votos nulos foi de {percentual_NULO}%')
print(f'O percentual de votos brancos foi de {percentual_BRANCO}%')
