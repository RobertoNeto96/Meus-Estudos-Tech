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

except mysql.connector.Error as erro:
    print(f'Falaha ao criar tabela no MySQL: {erro}')    
  
finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print('Conexão com o MySQL finalizada.')