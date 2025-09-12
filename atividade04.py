def calculadora(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return 'Erro: Divisão por zero'
    else:
        return 'Operação inválida'

def calcular_media_turma(notas):
    if not notas:
        return 'Nenhuma nota registrada'
    return sum(notas) / len(notas)

def validar_senha(senha):
    if len(senha) < 8:
        return False
    
    tem_numero = False
    for char in senha:
        if char.isdigit():
            tem_numero = True
            break
            
    if not tem_numero:
        return False
    
    return True

def analisar_numeros():
    numeros = []
    while True:
        entrada = input("Digite um número (ou 'fim' para encerrar): ")
        if entrada.lower() == 'fim':
            break
        try:
            numeros.append(int(entrada))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            continue
            
    pares = 0
    impares = 0
    for num in numeros:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
            
    return f'Números pares: {pares}\nNúmeros ímpares: {impares}'