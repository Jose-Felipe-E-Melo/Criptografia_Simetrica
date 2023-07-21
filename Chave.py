import pandas as pd
import random


def gerar_dicionario(dicionario_vazio):
    # Conjunto vazio para rastrear valores atribuídos ao dicionario
    # Garante a não repetição dos valores em chaves
    valores = set()
    
    for key in dicionario_vazio:
        # Preenche os valores do dicionario entre 0 e 256
        valor = random.randint(0, 256)
        
        # Garante que o valor gerado seja único. Se não for ele gera novamente
        while valor in valores:
            valor = random.randint(0, 256)
        
        # Adiciona valor ao dicionário e ao conjunto 'valores' (SET)
        dicionario_vazio[key] = valor
        valores.add(valor)


def traduzir_dicionario(dicionario_numerico, cond_tamanho):
    for chave, valor in dicionario_numerico.items():
        # Convertendo valor para binário e removendo prefixo '0b'
        binario = bin(valor)[2:]
        
        # Garantindo a quantidade de bits por binário
        # Geração padrão 9 8 9 
                
        #binario = binario.zfill(random.randint(8,16))
        #dicionario_numerico[chave] = binario
        
        if cond_tamanho == 0 or cond_tamanho % 2 == 0:
            binario = binario.zfill(9)
            dicionario_numerico[chave] = binario
        elif cond_tamanho % 2 != 0:
            binario = binario.zfill(8)
            dicionario_numerico[chave] = binario
            

def criar_chave(qtd_separadores):
    # Quantidade de separadores = tamanho da mensagem ou quantos separadores terão

    # Dicionario padrão para gerar a chave
    dicionario_default = {
            'A': '', 'B': '', 'C': '', 'D': '', 'E': '',
            'F': '', 'G': '', 'H': '', 'I': '', 'J': '',
            'K': '', 'L': '', 'M': '', 'N': '', 'O': '',
            'P': '', 'Q': '', 'R': '', 'S': '', 'T': '',
            'U': '', 'V': '', 'W': '', 'X': '', 'Y': '',
            'Z': '',
            
            'a': '', 'b': '', 'c': '', 'd': '', 'e': '',
            'f': '', 'g': '', 'h': '', 'i': '', 'j': '',
            'k': '', 'l': '', 'm': '', 'n': '', 'o': '',
            'p': '', 'q': '', 'r': '', 's': '', 't': '',
            'u': '', 'v': '', 'w': '', 'x': '', 'y': '',
            'z': '',
            
            '0': '', '1': '', '2': '', '3': '', '4': '',
            '5': '', '6': '', '7': '', '8': '', '9': '',
            
            '?': '', '!': '', '.': '', ',': '', '@': '',
            '+': '', '-': '', '*': '', 
            
            ' ': '' 
        }

    # Criando dataframe
    dataframe = pd.DataFrame()

    # Dados para inserir no dataframe | Array de Dicionarios
    dados = []

    # Criando a chave
    for i in range(0, qtd_separadores):
        #  return: Preenche de forma random os valores do dicionário
        gerar_dicionario(dicionario_default)

        # return: Traduz o dicionário de decimal para binário
        traduzir_dicionario(dicionario_default, i)

        # Adicionando dicionario_completo no array de dados
        dados.append(dicionario_default)
        
        # Atribui null para todos os valores do dicionário
        dicionario_default = {
            'A': '', 'B': '', 'C': '', 'D': '', 'E': '',
            'F': '', 'G': '', 'H': '', 'I': '', 'J': '',
            'K': '', 'L': '', 'M': '', 'N': '', 'O': '',
            'P': '', 'Q': '', 'R': '', 'S': '', 'T': '',
            'U': '', 'V': '', 'W': '', 'X': '', 'Y': '',
            'Z': '',
            
            'a': '', 'b': '', 'c': '', 'd': '', 'e': '',
            'f': '', 'g': '', 'h': '', 'i': '', 'j': '',
            'k': '', 'l': '', 'm': '', 'n': '', 'o': '',
            'p': '', 'q': '', 'r': '', 's': '', 't': '',
            'u': '', 'v': '', 'w': '', 'x': '', 'y': '',
            'z': '',
            
            '0': '', '1': '', '2': '', '3': '', '4': '',
            '5': '', '6': '', '7': '', '8': '', '9': '',
            
            '?': '', '!': '', '.': '', ',': '', '@': '',
            '+': '', '-': '', '*': '', 
            
            ' ': ''
        }
        

    # Compila as chaves do dicionário como colunas e os valores como linhas
    dataframe = pd.DataFrame.from_records(dados)
    print(dataframe)

    # Exportando a chave em .xlsx
    dataframe.to_excel('.\chave.xlsx' ,index=False)

