# 🐍 Integração Python + Banco de Dados

Neste módulo, documento os meus estudos sobre como conectar aplicações escritas em Python a bancos de dados relacionais (MySQL), permitindo a automação de processos e manipulação de dados via código.

---

## 🛠️ Primeiros Passos: Instalação e Ambiente

Para fazer o Python conversar com o MySQL, é necessário instalar o driver/conector oficial do banco.

### Como instalar o conector no terminal:
```bash
pip install mysql-connector-python

. Para começarmos importamos o script para MySQL

import mysql.connector

. Em seguida criamos uma variavel com o nome que desejarmos e colocamos o script com os parametros de conexão

con = mysql.connector.connect(host='localhost',database='cadastro',user='root',password='123456')

. Seguindo a ordem do script acima, 'mysqlconnetor.connect', é o parametro que usamos para chamar a função de LOGIN, dentro dos parentese em ordem temos primeiro o HOST, que nesse caso é o HOST LOCAL, se for um host que nao seja local, precisa colocar o nome exato, em seguida temos DATABASE, que é o nome do banco de dados criado no WORKBENC do MYSQL, depois temos o USER que é o usuario do proprio MYSQL e por fim o PASSWORD que é a senha do MYSQL 

. Depois criamos um condição de verificação com IF, onde vamos retornar valor booleano se o servidor foi conectado ou não

if con.is_connected():
    db_info = con.server_info

. Nesse IF temos a variavel DB_INFO(Variavel pode receber qualquer nome desejado) e ela recebe um comando onde as informações do servidores são puxadas e atreladas a variavel   

. Em seguida damos o comando PRINT para retornar ao usuario a conexão com o servidor, mais as informações do servidor em questao, puxadas e armazenadas na variavel acima

if con,is_connected():
    db_info = con.server_info
    print('Conectado ao servidor MySQL versão', db_info)

. Agora vamos criar o comando que transporta as informações entre o banco de dados e o Python, que é o chamado CURSOR, esse comando SEMPRE é utilizado para buscar informaçoes no banco de dados e devolver para o Python

if con.is_connected():
    db_info = con.server_info
    print('Conectado ao servidor MySQL versão', db_info)
    cursor = con.cursor()
    cursor.execute('select database();')
    linha = cursor.fetchone()
    print('Conectado ao banco de dados', linha)

. Explicando a estrutura do codigo acima, criamos a variavel CURSOR para podermos "conversar" com o banco de dados, e darmos comandos SQL ao python e ele retornar os valores para gente por isso o comando   CURSOR = CON.CURSOR() , em seguida damos um comando para esse cursor ir buscar no banco de dados e retornar no Python para gente, com o comando CURSO.EXECUTE('SELECT DATABASE();'), dentro do parenteses colocamos o COMANDO EM SQL que queremos buscar ou executar no banco de dados  

. O comando dentro da VARIAVEL LINHA é utilizado para pegar somente a primeira informação do comando que foi dado no CURSOR.EXECUTE e ATRIBUIDO a variavel LINHA para podermos utiliza a informação no PRINT, ou seja se o banco de dados contiver 10 pessoas, esse FETCHONE mostrará somente as informaçoes da primeira pessoa

. Para encerrarmos a conexão com o banco de dados, utilizamos outro IF

if con.is_connected():
    cursor.close()
    con.close()
    print('Conexão ao MySQL foi encerrada!')

. Explicando a estrutra do codigo acima, verificamos se ainda estamos conectado ao banco de dados, caso estejamos, utilizamos o comando CURSOR.CLOSE() que é para encerrarmos a procura de informação no banco de dados, em seguida utilizamos CON.CLOSE que encerra a conexão com o banco de dados, e o print para exibir que a conexão foi devidamente encerrada    

. Para criarmos um tabela direto no Python utilizamos o TRY/EXCEPT para termos uma interface limpa caso aconteça algum erro de conexão, vamos utilizar o scrip abaixo para exemplificar e fixar na cabeça:

import mysql.connector

try:
    con = mysql.connector.connect(host='localhost',database='cadastro',user='root',password='123456')

    # Nesse comando vamos criar uma variavel para definirmos todo o script de craição no banco de dados com o CREATE TABLE
    criar_tabela_SQL = 'create table jogos (
                        id_jogo int not null auto_increment primary key,
                        NomeJogo varchar(50) not null,
                        preco decimal (5 , 2) not null,
                        duracao_em_horas float not null);

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


    
