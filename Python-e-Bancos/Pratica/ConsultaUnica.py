import mysql.connector
from mysql.connector import Error

# Praticando a organização do codigo com Def's para deixar o codigo mais limpo e facil de entender, primeiro fazemos uma função para conexão do python com o MySQL, utilizando um RETURN para sempre que quisermos conexão com o servidor
def conectar():
    try:
        conexao = mysql.connector.connect(host = 'localhost' , database = 'cadastro' , user = 'root' , password = '123456')
        return conexao
    except Error as e:
        print(f'Ocorreu um erro durante a tentativa de conexão, Erro:{e}')


def consulta_id(id_jogo):    
        con = conectar()
        cursor = con.cursor()
        comando_sql = f'SELECT * FROM jogos WHERE id_jogo = {id_jogo}'
        cursor.execute(comando_sql)
        linhas = cursor.fetchall()

        for linha in linhas:
            print(f'ID do jogo: {linha[0]}')
            print(f'Jogo: {linha[1]}')
            print(f'Preço: {linha[2]}')

        if con and con.is_connected():
            cursor.close()
            con.close()    
 
if __name__ == '__main__':

    print('--- Bem Vindo a consulta de jogos ---')
    try:
        id_escolhido = int(input('Digite qual ID do jogo que deseja consultar:'))
        consulta_id(id_escolhido)   
    except ValueError:
        print('Por favor digite o ID do jogo utilizando números')        