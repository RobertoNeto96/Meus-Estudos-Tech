import mysql.connector
from mysql.connector import Error

def conectar():
        try:
            conexao = mysql.connector.connect(host = 'localhost' , database = 'cadastro' , user = 'root' , password ='123456')
            return conexao
        except Error as e:
            print(f'Falha ao conectar ao banco de dados, erro: {e}')

def atualizacao_preco(id_jogo , novo_preco):
    
        con = conectar()
        if con:
            cursor = con.cursor()
            comando_sql = f'UPDATE jogos SET preco = {novo_preco} WHERE id_jogo = {id_jogo}'
            cursor.execute(comando_sql)
            con.commit()
            print('Preço atualizado com sucesso!')

        if con and con.is_connected():
            cursor.close()
            con.close()    


if __name__ == '__main__':

    print('--- Bem vindo a seção de alteração de valores ---')  

    try:
        id_escolhido = int(input('Digite qual o ID do jogo que deseja alterar seu valor: '))
        preco_atualizado = float(input('Qual é o novo valor: '))
        atualizacao_preco(id_escolhido , preco_atualizado)   
    except ValueError:
        print('Digite apenas valores em formato NUMÉRICO')       