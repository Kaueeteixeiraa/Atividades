def converter_temperatura(temperatura_celsius):
    temperatura_fahrenheit = (9 * temperatura_celsius + 160) / 5
    return temperatura_fahrenheit

temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))
temperatura_fahrenheit = converter_temperatura(temperatura_celsius)
print("A temperatura em graus Fahrenheit é: {:.2f}".format(temperatura_fahrenheit))