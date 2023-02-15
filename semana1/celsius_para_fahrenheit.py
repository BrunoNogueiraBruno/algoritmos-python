# ENUNCIADO:
# Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit.
# A fórmula de conversão é F ← C * 9 / 5 + 32, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

graus_input = float(input("Insira a temperatura em °C para que seja convertida em °F: "))


def celsius_para_farenheit(graus_celsius):
    graus_farenheit = graus_celsius * 9 / 5 + 32
    return round(graus_farenheit,2)


graus_output = celsius_para_farenheit(graus_input)


print(f'A temperatura {graus_input}°C equivale a {graus_output}°F')
