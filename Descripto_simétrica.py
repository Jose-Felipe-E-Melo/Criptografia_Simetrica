import pandas as pd
import re


def traducao(mensagem_num, chave, indice_linha, mensagem_ordenada, msg_traduzida):
    # Verificando se o valor procurado está na mensagem passada
    for valor_procurado in mensagem_num:
        mensagem_ordenada.append(valor_procurado)
        
    # Tradução da mensagem com o ' '
    for valor_procurado in mensagem_ordenada:
        for coluna, valor in chave.iloc[indice_linha].items():
            if valor == valor_procurado:
                msg_traduzida.append(coluna)
                break

def descripto(mensagem):
    # Importando a chave
    dataframe = pd.read_excel('chave.xlsx', dtype=str)

    # Separadores das tabelas | Espaços
    separador = dataframe[' '].tolist()
    #print('Separadores: ', separador)

    #Lista onde a mensagem fica salva 
    lista_provisoria = []

    #Variável e lista de controle da separação
    indices_separadores = []
    indice = 0

    for i in range(len(separador)):
        # Encontra o índice do separador atual após o índice anterior
        indice_atual = mensagem.find(separador[i], indices_separadores[indice-1] + len(separador[indice-1])) if i > 0 else mensagem.find(separador[i])
        indices_separadores.append(indice_atual)

    # Encontra o índice do primeiro separador após o último separador
    indice_separador_final = mensagem.find(separador[indice], indices_separadores[indice] + len(separador[indice]))
    indices_separadores.append(indice_separador_final)

    #Variável e lista de controle da segunda parte da separação
    partes = []
    indice_anterior = 0

    for i, separador in enumerate(separador):
        indice_separador = indices_separadores[i]
        parte = mensagem[indice_anterior:indice_separador + len(separador)].strip()
        partes.append(parte)
        indice_anterior = indice_separador + len(separador)

    # Adicione a parte final da mensagem após o último separador
    partes.append(mensagem[indice_anterior:].strip())
    print('\n')
    print(partes)

    # Fatiando as mensagens divididas com seu respectivo tamanho
    fatiamento_9_bits = r'\d{9}'
    fatiamento_8_bits = r'\d{8}'


    for i, parte in enumerate(partes):
        tamanho = len(parte)
        
        if tamanho % 9 == 0:
            partes[i] = re.findall(fatiamento_9_bits, parte)
        
        elif tamanho % 8 == 0:
            partes[i] = re.findall(fatiamento_8_bits, parte)

        lista_provisoria.append(partes[i])

    print('\n')
    print(lista_provisoria)

    # Lista onde será armazenada a mensagem traduzida
    msg_traduzida = []

    # Chamando a função de tradução quantas vezes necessário
    linha = 0

    # Chamada de tradução em loop
    for index, valor in enumerate(lista_provisoria):
        mensagem_ordenada = []
        
        traducao(valor, dataframe, linha, mensagem_ordenada, msg_traduzida)
        
        # Após percorrer a última linha: volta para a primeira
        linha = (linha + 1) % dataframe.shape[0]

    # Saída
    #print('Divisão em %d partes' %len(lista_provisoria))
    #print('\nArray em blocos: ', lista_provisoria)
    print('\nMensagem traduzida: ', msg_traduzida)
    print('\n'+''.join(msg_traduzida))
