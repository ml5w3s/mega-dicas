def adicionar_virgula(entrada, saida):
    try:
        # Abre o arquivo de entrada para leitura
        with open('resultados_filtrados.csv', 'r') as arquivo_entrada:
            linhas = arquivo_entrada.readlines()

        # Adiciona uma vírgula ao final de cada linha
        linhas_com_virgula = [linha.strip() + ',' for linha in linhas]

        # Abre o arquivo de saída para escrita
        with open('resultados_ajustados.csv', 'w') as arquivo_saida:
            arquivo_saida.write('\n'.join(linhas_com_virgula))

        print(f"Arquivo salvo como '{saida}' com sucesso.")

    except FileNotFoundError:
        print(f"Arquivo '{entrada}' não encontrado.")
    except IOError as e:
        print(f"Erro ao ler ou escrever o arquivo: {e}")


# Exemplo de uso
entrada = 'resultados_filtrados.csv'  # Nome do arquivo de entrada
saida = 'arquivo_saida.csv'      # Nome do arquivo de saída

(adicionar_virgula(entrada, saida))
