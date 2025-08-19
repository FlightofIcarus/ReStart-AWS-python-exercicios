print("Hello world!")

numero1 = 2
numero2 = 5

soma = numero1 + numero2
print(soma)

comprimento = 12
largura = 14
altura = 20

def calcular_volume(comprimento, largura, altura):
    resultado = comprimento * largura * altura
    return f"O volume é {resultado} cm³"

print(calcular_volume(comprimento, largura, altura))

def calcula_preco_total(nome_produto, quantidade, preco_unitario):
    resultado = preco_unitario * quantidade
    return f"O valor total do produto {nome_produto} é {resultado} reais."

nome_do_produto = "Cadeira Infantil"
preco_unitario = 12.40
quantidade = 3

print(calcula_preco_total(nome_do_produto, quantidade, preco_unitario))