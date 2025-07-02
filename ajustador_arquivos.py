# ajustador_arquivos.py

def ajustar_linhas(entrada, saida):
    """
    Ordena as combinações numéricas de cada linha e adiciona vírgula ao fim.
    Garante que os dados são realmente escritos corretamente.
    """
    try:
        with open(entrada, 'r', encoding='utf-8') as arquivo_entrada:
            linhas = arquivo_entrada.readlines()

        linhas_formatadas = []

        for i, linha in enumerate(linhas, 1):
            linha_original = linha.strip()

            if not linha_original:
                continue

            partes = linha_original.replace(',', ' ').split()
            numeros = []

            for parte in partes:
                if parte.isdigit():
                    numero = int(parte)
                    if 1 <= numero <= 60:
                        numeros.append(numero)

            if len(numeros) != 6:
                print(f"[Linha {i}] Ignorada: esperava 6 números, recebeu {len(numeros)}: '{linha_original}'")
                continue

            numeros_ordenados = sorted(numeros)
            linha_formatada = ' '.join(f"{n:02}" for n in numeros_ordenados) + ','

            print(f"[Linha {i}] Gravando: {linha_formatada}")  # Debug para confirmar

            linhas_formatadas.append(linha_formatada)

        with open(saida, 'w', encoding='utf-8') as arquivo_saida:
            for linha in linhas_formatadas:
                arquivo_saida.write(linha + '\n')

        print(f"✅ Arquivo '{saida}' salvo com {len(linhas_formatadas)} linhas.")

    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

# --- Uso ---

arquivo_de_entrada = 'resultados_filtrados.csv'
arquivo_de_saida = 'resultados_ajustados.csv'

ajustar_linhas(arquivo_de_entrada,arquivo_de_saida)
