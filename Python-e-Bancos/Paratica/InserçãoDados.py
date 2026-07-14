import mysql.connector

try:
    con = mysql.connector.connect(host='localhost',database='cadastro',user='root',password='123456')

    inserir_dados_SQL = """insert into jogos (id_jogo , NomeJogo , preco , duracao_em_horas)
                           values (default , 'Spider Man' , 200.00 , 90),
                                  (default , 'Marvel Avengers' , 120.00 , 45),
                                  (default , 'Silent Hill' , 100.00 , 65),
                                  (default , 'Mortal Kombat 1' , 299.00 , 35),
                                  (default , 'Final Fantasy' , 125.50 , 75);"""

    cursor = con.cursor()
    cursor.execute(inserir_dados_SQL)
    con.commit()
    print('Dados inseridos na tabela jogos com sucesso!')

except mysql.connector.Error as erro:
    print(f'Falha ao inserir os dados no MySQL: {erro}')    
    
finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print('Conexão com o MySQL finalizada.')