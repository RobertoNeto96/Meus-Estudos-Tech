from AlterarDados import atualizacao_preco
from ConsultaCompleta import consulta_completa
from ConsultaUnica import consulta_id
from InserçãoDados import cadastrar_jogos

while True:
    print('--- MENU INTERATIVO DO BANCO DE DADOS ---\n\n')
    print('[1] CONSULTAR TODOS CADASTROS DO BANCO DE DADOS')
    print('[2] CONSULTAR CADASTRO UNICO ATRAVÉS DO ID')
    print('[3] ALTERAR O VALOR DE UM DADO ATRAVÉS DO ID')
    print('[4] INSERIR NOVOS DADOS NO BANCO DE DADOS')
    print('[0] PARA ENCERRAR O PROGRAMA')

    try:
        escolha = int(input('QUAL CAMPO DESEJA ACESSAR:  '))
        if escolha == 0:
            print('OBRIGADO POR USAR NOSSO SISTEMA!!')
            break
        elif escolha == 1:
            consulta_completa()

        elif escolha == 2:
            id_procurado = int(input('DIGITE O ID DO JOGO QUE DESEJA BUSCAR:  '))
            consulta_id(id_procurado)  

        elif escolha == 3:
            id_jogo = int(input('QUAL ID DO JOGO A SER ALTERADO: '))
            novo_preco = float(input('NOVO VALOR A SER INSERIDO: '))
            atualizacao_preco(id_jogo , novo_preco) 
               
        elif escolha == 4:
            cadastrar_jogos()     

    except ValueError:
        print('COMANDO INCORRETO, DIGITE A ESCOLHA DE ACORDO COM AS OPÇÕES DO MENU!')

