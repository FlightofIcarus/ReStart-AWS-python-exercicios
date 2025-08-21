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

print(conversor_moedas(100, "real", "real"))

