# utils.py

import csv

def ler_combinacoes_arquivo(arquivo_csv):
    """Lê o arquivo CSV e retorna uma lista de combinações de números."""
    combinacoes = []
    try:
        with open(arquivo_csv, 'r', encoding='utf-8') as arquivo:
            leitor_csv = csv.reader(arquivo)
            for linha in leitor_csv:
                # Trata casos de linhas vazias
                if not linha:
                    continue
                # Remove espaços extras, junta múltiplos elementos da linha (se houver) e divide por espaços
                numeros = [numero.strip() for numero in ' '.join(linha).split()]
                # Converte cada número para inteiro e adiciona à lista como uma tupla
                combinacoes.append(tuple(map(int, numeros)))
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_csv}' não foi encontrado.")
        return []
    return combinacoes