# ENUNCIADO:
# Ler uma temperatura em graus Fahrenheit e apresentá-la convertida em graus Celsius.
# A fórmula de conversão é C ← ((F – 32) * 5) / 9, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

graus_input = float(input("Insira a temperatura em °F para que seja convertida em °C: "))


def farenheit_para_celsius(graus_farenheit):
    graus_celsius = ((graus_farenheit - 32) * 5) / 9
    return round(graus_celsius,2)


graus_output = farenheit_para_celsius(graus_input)


print(f'A temperatura {graus_input}°F equivale a {graus_output}°C')
