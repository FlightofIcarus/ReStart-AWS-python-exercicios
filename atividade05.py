import datetime

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)

    return round(gorjeta,2)





#codigo main
total_conta = float(input("Digite o valor total da conta: "))
porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta: "))

gorjeta = calcular_gorjeta(total_conta, porcentagem_gorjeta)

print(f"O valor da gorjeta é: R${gorjeta}")

def eh_palindromo(texto):
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())

    #invertido = texto_limpo[::-1]

    invertido = ''
    for letra in texto_limpo:
        invertido = letra + invertido

    if texto_limpo == invertido:
        return True
    else:
        return False
    
texto = input("Digite um texto: ")
resultado = eh_palindromo(texto)
print(f"{texto} é um palíndromo? {resultado}")

def calcular_desconto(valor_produto, porcentagem_desconto):
    desconto = valor_produto * (porcentagem_desconto / 100)
    valor_com_desconto = valor_produto - desconto

    return round(valor_com_desconto,2)





#codigo main
total_conta = float(input("Digite o valor total da conta: "))
porcentagem_desconto = float(input("Digite a porcentagem do desconto: "))

valor_final = calcular_desconto(total_conta, porcentagem_desconto)

print(f"O valor da gorjeta é: R${valor_final}")

def calcular_idade_em_dias(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade * 365


ano_nascimento = int(input("Digite o ano de nascimento: "))
idade_em_dias = calcular_idade_em_dias(ano_nascimento)
print(f"A idade em dias é aproximadamente: {idade_em_dias} dias")