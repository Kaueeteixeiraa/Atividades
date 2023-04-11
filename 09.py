def ler_valores():
    return float(input("Informe o tempo gasto na viagem (em horas): ")), float(input("Informe a velocidade média durante a viagem (em km/h): "))

def calcular_litros(tempo, velocidade_media):
    distancia = tempo * velocidade_media
    return distancia, distancia / 12

def apresentar_resultado(tempo, velocidade_media, distancia, litros_usados):
    print(f"Velocidade média: {velocidade_media:.2f} km/h\nTempo gasto na viagem: {tempo:.2f} horas\nDistância percorrida: {distancia:.2f} km\nLitros de combustível utilizados: {litros_usados:.2f} L")

tempo, velocidade_media = ler_valores()
distancia, litros_usados = calcular_litros(tempo, velocidade_media)
apresentar_resultado(tempo, velocidade_media, distancia, litros_usados)