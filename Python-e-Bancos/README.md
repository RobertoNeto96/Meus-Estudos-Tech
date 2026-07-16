# 🐍 Python + MySQL: Sistema de Gerenciamento de Jogos

Bem-vindo ao meu repositório de estudos de integração entre Python e bancos de dados relacionais! 

Este projeto nasceu da necessidade de conectar uma aplicação Python a um banco de dados **MySQL** real. Aqui, eu estruturei um sistema de gerenciamento de jogos (CRUD) totalmente modular que roda direto no terminal, tratando erros e garantindo que os dados sejam salvos com segurança.

---

## 🗂️ Módulos do Sistema (Acesso Rápido)

Clique em qualquer um dos módulos abaixo para abrir o arquivo de código correspondente com as minhas anotações e explicações detalhadas:

* 🎮 **[Controlador Central do Menu (main.py)](./Pratica/main.py)** - Onde o menu interativo roda e direciona o usuário.
* ➕ **[Cadastro de Novos Jogos (InserçãoDados.py)](./Pratica/InserçãoDados.py)** - Script responsável por inserir novos registros no banco.
* 🔍 **[Consulta Completa do Banco (ConsultaCompleta.py)](./Pratica/ConsultaCompleta.py)** - Puxa e exibe todos os jogos salvos no MySQL.
* 🆔 **[Consulta de Jogo por ID (ConsultaUnica.py)](./Pratica/ConsultaUnica.py)** - Filtra e exibe os dados detalhados de apenas um jogo.
* ✏️ **[Alterar Preço do Jogo (AlterarDados.py)](./Pratica/AlterarDados.py)** - Altera o valor de um jogo específico buscando pelo ID.
* 🏗️ **[Criação da Tabela de Jogos (CriandoTabela.py)](./Pratica/CriandoTabela.py)** - Script de conexão básica e estrutura de criação da tabela.

---

## 🛠️ Primeiros Passos: Instalação e Ambiente

Para que o Python consiga "falar a língua" do MySQL, precisamos instalar um tradutor oficial (o driver/conector).

Abra o seu terminal e execute o comando:
```bash
pip install mysql-connector-python

🔌 Conexão Básica: O "Hello World" do Banco de Dados
📦 1. Importando o Conector
Antes de qualquer linha de código, precisamos trazer a biblioteca para o jogo:

import mysql.connector

🔐 2. Batendo na Porta do Servidor (Parâmetros de Login)Para se conectar, você precisa passar as credenciais corretas. Criamos uma variável (geralmente chamada con ou conexao) para receber as chaves de acesso:Pythoncon = mysql.connector.connect(
    host='localhost',
    database='cadastro',
    user='root',
    password='123456'
)
ParâmetroO que ele significa na prática?hostOnde o banco está rodando. Usamos localhost porque ele está na nossa própria máquina.databaseO nome exato do banco de dados que você criou lá no MySQL Workbench.userO usuário do seu MySQL (o padrão do sistema é root).passwordA senha que você definiu na instalação do MySQL.🚦 3. Verificando se a Porta Abriu (is_connected)Não dá para mandar comandos se a conexão falhou. Por isso, usamos um if inteligente para testar o status e exibir as informações do servidor na tela:Pythonif con.is_connected():
    db_info = con.server_info
    print('✅ Conectado ao servidor MySQL versão:', db_info)
💡 O que está acontecendo aqui?O is_connected() é um validador que devolve True (Verdadeiro) ou False (Falso). Se der tudo certo, a propriedade server_info captura a versão do MySQL e nós a exibimos no terminal.🎛️ O Poder do Cursor e QueriesO Cursor é o "mensageiro" do seu código. Ele pega a sua instrução em Python, leva até o MySQL, executa o comando lá dentro e traz o resultado de volta debaixo do braço.Pythonif con.is_connected():
    # 1. Criamos o mensageiro
    cursor = con.cursor()
    
    # 2. Mandamos ele executar um comando SQL no banco
    cursor.execute('SELECT DATABASE();')
    
    # 3. Pegamos de volta o primeiro resultado
    linha = cursor.fetchone()
    print('📂 Conectado com sucesso ao banco:', linha)
🧠 Saco de Truques do Desenvolvedor:cursor = con.cursor(): Cria o canal ativo de comunicação.cursor.execute('SELECT DATABASE();'): Roda o comando SQL que você colocou entre aspas.linha = cursor.fetchone(): Pega apenas o primeiro resultado que a busca encontrou. Se a sua tabela tivesse 10 cadastros, o fetchone() traria apenas o primeiro da fila.🚪 Encerrando a Visita (Sempre feche a porta!)Terminou de usar? Sempre feche o cursor e a conexão para liberar memória e evitar gargalos no seu computador.Pythonif con.is_connected():
    cursor.close()
    con.close()
    print('🔌 Conexão ao MySQL encerrada com segurança!')
🏗️ Criando Tabelas com Escudo de Segurança (Try/Except/Finally)Para projetos reais, usar apenas códigos soltos é perigoso. Se o servidor cair ou a senha mudar, o programa quebra no meio. Para evitar isso, usamos a estrutura blindada try/except/finally:Pythonimport mysql.connector

try:
    # 🎯 Tentativa: Se tudo estiver certo, o Python roda este bloco
    con = mysql.connector.connect(
        host='localhost',
        database='cadastro',
        user='root',
        password='123456'
    )

    # Definimos o roteiro de criação da tabela (Query SQL)
    criar_tabela_sql = """
    CREATE TABLE IF NOT EXISTS jogos (
        id_jogo INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        NomeJogo VARCHAR(50) NOT NULL,
        preco DECIMAL(5, 2) NOT NULL,
        duracao_em_horas FLOAT NOT NULL
    );
    """

    cursor = con.cursor()
    cursor.execute(criar_tabela_sql)
    print('🎮 Tabela "jogos" criada com absoluto sucesso!')

except mysql.connector.Error as erro:
    # 🛡️ Escudo de Erros: Se algo der ruim lá em cima, o código vem para cá de forma amigável
    print(f'❌ Ops! Falha ao criar a tabela no MySQL. Erro detalhado: {erro}')    

finally:
    # 🔒 Trava de Segurança: Esse bloco roda OBRIGATORIAMENTE, dando erro ou não!
    if con.is_connected():
        cursor.close()
        con.close()
        print('🚪 Canal de conexão encerrado e recursos liberados.')
🔮 O Próximo Passo da Jornada...Para fazer consultas, inserções ou atualizações de dados (CRUD), a base estrutural vai ser exatamente a mesma que você acabou de ver aqui. Só vamos mudar a query SQL que passamos para o cursor.execute()!