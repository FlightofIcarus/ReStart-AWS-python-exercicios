import random
import string
import requests

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + "!@#$%&"
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

    return senha

tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
senha_gerada = gerar_senha(tamanho_senha)
print("Senha gerada:", senha_gerada)

def obter_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()['results'][0]
        nome = f"{dados['name']['first']} {dados['name']['last']}"
        email = dados['email']
        pais = dados['location']['country']
        return f"""
            Nome: {nome}
            Email: {email}
            País: {pais}
        """
    except requests.RequestsException as e:
        print(f"Erro ao obter usuário aleatório: {e}")
        return None
    
print("Obtendo usuário aleatório...")
usuario = obter_usuario_aleatorio()
print(usuario)

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

        if "erro" in dados:
            return "CEP não encontrado"
        
        return f"""
                CEP: {dados['cep']}
                Logradouro: {dados['logradouro']}
                Bairro: {dados['bairro']}
                Cidade: {dados['localidade']}
                Estado: {dados['estado']}
                """
    except requests.RequestException as e:
        return f"Erro ao consultar o CEP: {e}"
    


cep = input("Digite o CEP (apenas números): ")
resultado = consultar_cep(cep)
print(resultado)

def obter_cotacao_atual(moeda):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()[f"{moeda}BRL"]
        return f"""
                Cotação de {moeda} para BRL:
                Valor: R$ {float(dados['bid']):.2f}
                Máxima: R$ {float(dados['high']):.2f}
                Mínima: R$ {float(dados['low']):.2f}
                Data/hora: {dados['create_date']}
                """
    except requests.RequestException as e:
        return f"Erro ao obter a cotação: {e}"
    
moeda = input("Digite o código da moeda para cotação (EUR, USD, GBP)")
resultado = obter_cotacao_atual(moeda)
print(resultado)