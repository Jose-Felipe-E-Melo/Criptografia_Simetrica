import Chave
import Cripto_simetrica
import Descripto_simétrica

def print_menu():
    print('[1] Gerar nova Chave')
    print('[2] Criptografar')
    print('[3] Traduzir')
    print('[0] SAIR')

def main():
    # Inicialização da escolha com None fora do loop
    escolha = None
    
    while escolha != 0:
        # Print do menu
        print_menu()
        
        # Variável de escolha do menu
        escolha = input('Digite uma opção: ')
        
        # Criação da chave
        if escolha == '1':
            num_separador = int(input('Quantos separadores terão na mensagem: '))
            Chave.criar_chave(num_separador)
            print('NOVA CHAVE CRIADA\n')
        
        # Criptografia da mensagem
        elif escolha == '2':
            # Mensagem a ser criptografada
            mensagem = input('Digite sua mensagem: ')
            Cripto_simetrica.recebe_mesagem(mensagem)
            print('MENSAGEM CRIPTOGRAFADA\n')
           
        # Tradução da mensagem
        elif escolha == '3':
            # Uma escolha entre usar a mensagem recém salva ou digitar
            esc_interna = input('[1] Mensagem Criptografada salva | [2] Digitar Mensagem Criptografada:  ')
            
            # Mensagem recém salva
            if esc_interna == '1':
                mensagem_salva = Cripto_simetrica.recebe_mesagem(mensagem)
                Descripto_simétrica.descripto(mensagem_salva)
            
            # Digitar toda a mensagem
            elif esc_interna == '2':
                cripto_digitada = input('Digite a mensagem criptografada: ')
                Descripto_simétrica.descripto(cripto_digitada)
                
            print('MENSAGEM TRADUZIDA\n')
        
        # Saindo do loop
        elif escolha == '0':
            break
    
if __name__ == "__main__":
    main()
