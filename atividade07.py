import pandas as pd
import csv
import json

def processar_logs_treinamento(nome_arquivo):
    try:
        leitor = pd.read_csv(nome_arquivo)
        media_tempo = leitor['tempo_execucao'].mean()
        desvio_padrao = leitor['tempo_execucao'].std()
        return f"""
                Média do tempo de execução: {media_tempo}
                Desvio padrao do tempo de execução: {desvio_padrao:.2f}
                """
    except FileNotFoundError:
        return "Arquivo não encontrado."
    

nome_arquivo = input("Digite o nome do arquivo csv: ")

print(processar_logs_treinamento(nome_arquivo))



def escrever_csv(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(['Nome', 'Idade', 'Cidade'])
            for linha in dados:
                escritor.writerow(linha)
            return (f"Dados salvos em {nome_arquivo}")
    except Exception as e:
        return(f"Erro ao escrever no arquivo: {e}")


dados = [
    ['Ana', 18, 'João Pessoa'],
    ['Joaquim', 35, 'São Paulo'],
    ['Maicon Jebson', 20, 'Caicó']
]

nome_arquivo = input("Digite o nome do arquivo: ")
print(escrever_csv(nome_arquivo, dados))

def ler_csv(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            for linha in leitor:
                print(linha)
    except FileNotFoundError:
        return(f"Arquivo não encontrado")



nome_arquivo = input("Digite o nome do arquivo: ")
print(ler_csv(nome_arquivo))

def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
            dados_json = json.load(arquivo_json)
            print(dados_json)
    except FileNotFoundError:
        return(f"Arquivo não encontrado")
    

def escrever_json(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json, ensure_ascii = False, indent = 4)
        print(f"Dados salvos em: {nome_arquivo}")
    except Exception as e:
        return(f"Erro ao escrever no arquivo: {e}")
    
dados = {
    "nome": "João",
    "idade": 20,
    "cidade": "São Paulo"
}

nome_arquivo = input("Digite o nome do arquivo: ")
escrever_json(nome_arquivo, dados)
ler_json(nome_arquivo)