import csv
from collections import Counter
10 - 53 - 5 - 34 - 42 - 37
def ler_numeros_arquivo(arquivo_csv):
    """Lê o arquivo CSV e retorna uma lista de todos os números encontrados."""
    numeros = []
    with open(arquivo_csv, 'r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        for linha in leitor_csv:
            # Remove espaços extras e divide a linha com base em espaços
            numeros.extend([int(numero.strip()) for numero in ' '.join(linha).split()])
    return numeros

def eh_primo(n):
    """Verifica se um número é primo."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def analisar_numeros(numeros):
    """Realiza a análise dos números e imprime os resultados."""
    # Frequência dos números
    contagem_numeros = Counter(numeros)
    numeros_mais_frequentes = contagem_numeros.most_common(6)

    # Pares e Ímpares
    pares = sum(1 for num in numeros if num % 2 == 0)
    impares = len(numeros) - pares

    # Números Primos
    primos = sum(1 for num in numeros if eh_primo(num))

    # Quantidade acima e abaixo de certos limiares
    def contar_acima_abaixo(limite):
        return sum(1 for num in numeros if num < limite), sum(1 for num in numeros if num >= limite)

    abaixo_10, acima_10 = contar_acima_abaixo(10)
    abaixo_20, acima_20 = contar_acima_abaixo(20)
    abaixo_30, acima_30 = contar_acima_abaixo(30)
    abaixo_40, acima_40 = contar_acima_abaixo(40)
    abaixo_50, acima_50 = contar_acima_abaixo(50)

    # Frequência nas zonas
    faixas = {
        "10-20": sum(1 for num in numeros if 10 <= num < 20),
        "20-30": sum(1 for num in numeros if 20 <= num < 30),
        "30-40": sum(1 for num in numeros if 30 <= num < 40),
        "40-50": sum(1 for num in numeros if 40 <= num < 50),
        "50-60": sum(1 for num in numeros if 50 <= num < 60),
    }

    # Impressão dos resultados
    print("6 Números mais frequentes:", numeros_mais_frequentes)
    print("Quantidade de pares:", pares)
    print("Quantidade de ímpares:", impares)
    print("Quantidade de números primos:", primos)
    print("Quantidade abaixo de 10:", abaixo_10)
    print("Quantidade acima de 10:", acima_10)
    print("Quantidade abaixo de 20:", abaixo_20)
    print("Quantidade acima de 20:", acima_20)
    print("Quantidade abaixo de 30:", abaixo_30)
    print("Quantidade acima de 30:", acima_30)
    print("Quantidade abaixo de 40:", abaixo_40)
    print("Quantidade acima de 40:", acima_40)
    print("Quantidade abaixo de 50:", abaixo_50)
    print("Quantidade acima de 50:", acima_50)
    print("Frequência nas zonas:")
    for faixa, contagem in faixas.items():
        print(f"  {faixa}: {contagem}")

# Nome do arquivo CSV
arquivo_csv = 'resultados_filtrados.csv'

# Ler os números e realizar a análise
numeros = ler_numeros_arquivo(arquivo_csv)
analisar_numeros(numeros)
