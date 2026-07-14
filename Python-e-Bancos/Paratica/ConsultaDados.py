import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(host='localhost',database='cadastro',user='root',password='123456')

# Nessa variavel inserimos o comando que queremos passar para o banco de dados
    consulta_SQL = """select * from jogos"""

# Nesse bloco de comando mandamos o comando para o banco de dados através do CURSOR
    cursor = con.cursor()
    cursor.execute(consulta_SQL)
# Nessa variavel usamos o FETCHALL que é um comando do cursor para trazer todos os dados da tabela do banco de dados    
    linhas = cursor.fetchall()
# Nesse print temos um recurso do CURSOR, que é o ROWCOUNT, ele conta todos os resultados que foram trazidos da busca no banco de dados    
    print(f'Numero total de registros retornados: {cursor.rowcount}')
# Nese laço de repetição vamos utilizar os valores que foram buscados e trazidos pelo FETCHALL e separa-los linha por linha de cada cadastro dentro do banco de dados
    print('\nMostrando os jogos cadastrados\n')
    for linha in linhas:
        print(f'ID do jogo: {linha[0]}')
        print(f'Nome do jogo: {linha[1]}')
        print(f'Preço do jogo: {linha[2]}')
        print(f'Duração em Horas do jogo: {linha[3]}h' , '\n')
# Nesse modo de fazer o except fica de uma forma mais profissional, importando o modulo Error direto do mysql connector e depois o chamando de apenas 'e'
except Error as e:
    print(f'Erro ao acessar tabela MySQL {e}')    
  
finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print('Conexão com o MySQL finalizada.')