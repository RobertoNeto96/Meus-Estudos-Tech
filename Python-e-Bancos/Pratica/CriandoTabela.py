import mysql.connector

def criacao_tabela():
    try:
        con = mysql.connector.connect(host='localhost',database='cadastro',user='root',password='123456')

    # Nesse comando vamos criar uma variavel para definirmos todo o script de craição no banco de dados com o CREATE TABLE
        criar_tabela_SQL = """create table jogos (
                            id_jogo int not null auto_increment primary key,
                            nome_jogo varchar(50) not null,
                            preco decimal (5 , 2) not null,
                            duracao_em_horas float not null);"""

    # Agora vamos criar um CURSOR para que possamos dar comandos no banco de dados através do Python
        cursor = con.cursor()
        cursor.execute(criar_tabela_SQL)
        print('Tabela de jogos criada com sucesso!')

    except mysql.connector.Error as erro:
        print(f'Falaha ao criar tabela no MySQL: {erro}')    

    # Aqui vamos utilizar um comando FINALLY, que funciona como uma trava de segurança pra caso aconteça algum erro de conexão nos campos de codigos acima, basicamente o python fechara a conexão com o banco de dados caso aconteça algum erro e se a conexão posteriormente tiver sido bem sucedida, ou seja, se o usuario conseguiu conectar no banco de dados corretamente, executou todos os comandos necessarios, e quiser fechar o banco de dados apos isso, o programa fechara corretamente, pois houve uma conexão bem sucedida. lembrando que a conexao fechará independente se houve um erro ou nao, nos codigos acima    
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
            print('Conexão com o MySQL finalizada.')