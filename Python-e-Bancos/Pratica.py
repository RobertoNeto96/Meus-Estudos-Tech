import mysql.connector

con = mysql.connector.connect(host='localhost', database='cadastro',user='root',password='123456')

if con.is_connected():
    db_info = con.server_info
    print('Conectado ao servidor MySQL versão', db_info)
    cursor = con.cursor()
    cursor.execute('select database();')
    linha = cursor.fetchone()
    print('Conectado ao banco de dados', linha)

if con.is_connected():
    cursor.close()
    con.close()
    print('Conexão ao MySQL foi encerrada!')