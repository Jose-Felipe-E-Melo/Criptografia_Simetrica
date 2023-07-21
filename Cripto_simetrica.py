import pandas as pd

def criptografia(linha, bloco_fatiado, palavra, mensagem, mensagem_criptografada):
    
    # .zfill(bloco_fatiado) | reconhece zeros a esquerda segundo o tamanho (de bits) dito
    mensagem_criptografada.append([str(linha.get(letra)).zfill(bloco_fatiado) for letra in palavra])
        
        # Verifica se tem ' ' na mensagem | Separador
    if ' ' in mensagem:  
        mensagem_criptografada.append(str(linha[' ']).zfill(bloco_fatiado))

def recebe_mesagem(mensagem):
    # Importando chave
    dataframe = pd.read_excel('chave.xlsx', dtype=str)

    # Numero de palavras na mensgem
    palavras = mensagem.split()

    # Lista onde a mensagem será salva
    mensagem_criptografada = []

    # Variáveis de controle das linhas e da divisão
    linha_inicial = dataframe.iloc[0]
    num_linha = 0
    divisao_blocos = 9

    # Criptografia
    for palavra in palavras:
        
        criptografia(linha_inicial, divisao_blocos, palavra, mensagem, mensagem_criptografada)
        
        # Divisao circular do indice das linhas
        num_linha = (num_linha + 1) % dataframe.shape[0]
        
        # Divisao dinamica dos blocos seguindo o padrao das linhas
        divisao_blocos = 9 - (num_linha % 2)
        
        # Próxima linha do dataframe
        linha_inicial = dataframe.iloc[num_linha]
        

    # Lista onde a mensagem será unificada
    mensagem_unif = []

    # Unindo as informações das listas em uma única lista
    for item in mensagem_criptografada:
        mensagem_unif.extend(item)

    # Com o .join() a mensagem é enviada sem , ou []
    print(''.join(mensagem_unif))

    return ''.join(mensagem_unif)
