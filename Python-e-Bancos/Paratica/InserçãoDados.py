import mysql.connector
from mysql.connector import Error

print('--- SISTEMA DE CADASTRO DE JOGOS ---')

# 1. Perguntamos ao usuário quantos jogos ele quer cadastrar
# Usamos int() porque a quantidade precisa ser um número inteiro!
qtd_jogos = int(input('Quantos jogos você deseja cadastrar hoje? '))

try:
    # Abrimos a conexão uma única vez antes de começar o laço (muito mais eficiente!)
    con = mysql.connector.connect(host='localhost', database='cadastro', user='root', password='123456')
    cursor = con.cursor()

    # 2. Criamos o laço para repetir o cadastro "qtd_jogos" vezes
    for i in range(qtd_jogos):
        print(f'\n--- Cadastrando o {i + 1}º jogo ---')
        
        # Os inputs agora rodam dentro do loop!
        nomejogo = input('Nome do jogo: ')
        precojogo = float(input('Preço do jogo: '))
        quantidadehoras = int(input('Quantidade em horas de duração: '))

        # O molde SQL com os placeholders
        inserir_dados_SQL = """INSERT INTO jogos (id_jogo, NomeJogo, preco, duracao_em_horas)
                               VALUES (default, %s, %s, %s);"""

        dados = (nomejogo, precojogo, quantidadehoras)

        # Executamos e salvamos a cada repetição
        cursor.execute(inserir_dados_SQL, dados)
        con.commit()
        
        print(f'-> "{nomejogo}" cadastrado com sucesso!')

    print('\n Todos os jogos foram inseridos com sucesso!')

except Error as e:
    print(f'\nHouve um erro no banco de dados: {e}')    
    
finally:
    if con.is_connected():
        cursor.close()
        con.close()
        print('\nConexão com o MySQL finalizada.')