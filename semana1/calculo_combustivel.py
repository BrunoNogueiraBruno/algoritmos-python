# ENUNCIADO:
# Efetuar o cálculo da quantidade de litros de combustível gasta em uma viagem,
# utilizando um automóvel que faz 12 quilômetros por litro. Para obter o cálculo,
# o usuário deve fornecer o tempo gasto (variável TEMPO) e a
# velocidade média (variável VELOCIDADE) durante a viagem. Dessa forma,
# será possível obter a distância percorrida com a fórmula DISTÂNCIA ← TEMPO * VELOCIDADE.
# A partir do valor da distância, basta calcular a quantidade de litros de
# combustível utilizada na viagem com a fórmula LITROS_USADOS ← DISTÂNCIA / 12.
# O programa deve apresentar os valores da velocidade média,
# tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem.


KM_POR_LITRO = 12

tempo_input = float(input("Insira o tempo gasto em horas na viagem de carro: "))
velocidade_media_input = float(input("Insira a velocidade média do carro durante a viagem: "))


def calculo_combustivel(tempo, velocidade_media):
    distancia = tempo * velocidade_media
    gasto_combustivel = distancia / KM_POR_LITRO

    return round(distancia,2), round(gasto_combustivel, 2)


distancia, gasto_combustivel = calculo_combustivel(tempo_input, velocidade_media_input)


print(f'A uma velocidade média de {velocidade_media_input} km/h, em {tempo_input} horas de viagem e percorrendo uma distância de {distancia} km, o gasto de combustível foi de {gasto_combustivel} litros')
