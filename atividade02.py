def conversor_moedas(valor, moeda_origem, moeda_destino):
    if moeda_origem == "real" and moeda_destino == "dolar":
        return f"U${round(valor / 5.20, 2)}"
    if moeda_origem == "real" and moeda_destino == "euro":
        return f"€{round(valor / 6.15, 2)}"
    if moeda_destino == "real" and moeda_origem == "dolar":
        return f"R${round(valor * 5.20, 2)}"
    if moeda_destino == "real" and moeda_origem == "euro":
        return f"R${round(valor * 6.15, 2)}"
    if moeda_origem == moeda_destino:
        return round(valor, 2)
    return "Moeda não suportada"

print(conversor_moedas(100, "real", "dolar"))

def calculadora_desconto(valor, percentual):
    percentual = percentual / 100
    preco_final = valor - (valor * percentual)
    return f" o preço final de seu item é R${round(preco_final, 2)}. Você teve um desconto de R${round(valor * percentual, 2)}"

print(calculadora_desconto(50, 20))

def calculadora_media_escolar(notas):
    if notas == []:
        return "Nenhuma nota disponível para cálculo."
    media = sum(notas) / len(notas)
    for nota in notas:
        print(f"Nota: {nota}")
    return f"A média das notas é {round(media, 2)}"

print(calculadora_media_escolar([7.5, 8.0, 6.5]))

def calculadora_consumo_combustivel(distancia_percorrida, combustivel_gasto):
    if combustivel_gasto == 0:
        return "O consumo de combustível não pode ser zero."
    consumo = distancia_percorrida / combustivel_gasto
    return f"Você percorreu {distancia_percorrida}km, gastando um total de {combustivel_gasto} litros de combustível. O consumo médio de combustível é {round(consumo, 2)} km/l."

print(calculadora_consumo_combustivel(300, 25))