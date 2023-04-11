def calcular_media(lista):
    return sum(lista) / len(lista)

numeros = [90, 80, 70, 60, 50]
print(f"A média dos números na lista {numeros} é: {calcular_media(numeros):.2f}")