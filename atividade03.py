def classificador_idade():
    idade_do_usuario = int(input("Digite a sua idade:"))
    if idade_do_usuario > 0 and idade_do_usuario < 12:
        return "Você é uma criança."
    elif idade_do_usuario >= 13 and idade_do_usuario <= 17:
        return "Você é um adolescente."
    elif idade_do_usuario >= 18 and idade_do_usuario <= 59:
        return "Você é um adulto."
    elif idade_do_usuario >= 60:
        return "Você é um idoso."
    else:
        return "Idade inválida."

# print(classificador_idade())

def calculadora_imc():
    peso = float(input("Digite seu peso em kg usando ponto em vez de vírgula:"))
    altura = float(input("Digite sua altura em metros usando ponto em vez de vírgula:"))
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return f"Seu IMC é {round(imc, 2)}. Você está abaixo do peso."
    if imc >= 18.5 and imc < 25:
        return f"Seu IMC é {round(imc, 2)}. Você está com peso normal."
    if imc >= 25 and imc < 30:
        return f"Seu IMC é {round(imc, 2)}. Você está acima do peso."
    if imc >= 30:
        return f"Seu IMC é {round(imc, 2)}. Você está obeso."
    else:
        return "Valor de IMC inválido."

# print(calculadora_imc())

def conversor_temperatura():
    temperatura = float(input("Digite a temperatura usando ponto em vez de vírgula:"))
    unidade_temperatura_origem = input("Digite a unidade da temperatura de origem (Celsius, Fahrenheit ou Kelvin):").lower()
    unidade_temperatura_destino = input("Digite a unidade da temperatura de destino (Celsius, Fahrenheit ou Kelvin):").lower()
    if unidade_temperatura_origem == "celsius" and unidade_temperatura_destino == "fahrenheit":
        return f"A temperatura em graus Fahrenheit é {round((temperatura * 9/5) + 32, 2)}."
    if unidade_temperatura_origem == "celsius" and unidade_temperatura_destino == "kelvin":
        return f"A temperatura em Kelvin é {round(temperatura + 273.15, 2)}."
    if unidade_temperatura_origem == "fahrenheit" and unidade_temperatura_destino == "celsius":
        return f"A temperatura em graus Celsius é {round((temperatura - 32) * 5/9, 2)}."
    if unidade_temperatura_origem == "fahrenheit" and unidade_temperatura_destino == "kelvin":
        return f"A temperatura em Kelvin é {round((temperatura - 32) * 5/9 + 273.15, 2)}."
    if unidade_temperatura_origem == "kelvin" and unidade_temperatura_destino == "celsius":
        return f"A temperatura em graus Celsius é {round(temperatura - 273.15, 2)}."
    if unidade_temperatura_origem == "kelvin" and unidade_temperatura_destino == "fahrenheit":
        return f"A temperatura em graus Fahrenheit é {round((temperatura - 273.15) * 9/5 + 32, 2)}."
    else:
        return "Unidade de temperatura não suportada ou inválida."

# print(conversor_temperatura())

def verifica_ano_bissexto():
    ano = int(input("Digite um ano para verificar se é bissexto:"))
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return f"O ano {ano} é bissexto."
    else:
        return f"O ano {ano} não é bissexto."

print(verifica_ano_bissexto())