# Meus-Estudos-Tech

Repositório dedicado ao registro da minha jornada de estudos em tecnologia, centralizando anotações, exercícios e projetos práticos baseados no curso de MySQL do Curso em Vídeo (Prof. Gustavo Guanabara).

----------------------------------------------------------------------------------------------------------

TIPOS PRIMITIVOS NO SQL

Ao criar campos em uma tabela, precisamos definir a natureza dos dados que eles irão receber. Os principais tipos primitivos são:

. Numéricos:
  - Inteiros: Usados para contagens e números sem casas decimais (Ex: TINYINT, INT, BIGINT).
  - Reais: Usados para valores com casas decimais (Ex: FLOAT, DOUBLE, DECIMAL).
  - Lógicos: Usados para estados verdadeiro/falso (Ex: BOOLEAN, representado internamente como TINYINT).

. Data/Tempo: Usados para armazenar registros cronológicos (Ex: DATE para datas YYYY-MM-DD, TIME para horas, DATETIME e TIMESTAMP para data e hora, YEAR para anos).

. Literais (Textos):
  - Caracteres: CHAR (tamanho fixo, ideal para siglas como sexo ou estados) e VARCHAR (tamanho variável, economiza memória).
  - Textos Longos: TEXT e LONGTEXT (para descrições e grandes blocos de texto).
  - Binários: BLOB e LONGBLOB (para arquivos, imagens ou mídias armazenadas no banco).
  - Coleções: ENUM (lista fechada de opções pré-definidas) e SET.

. Espaciais: Usados para dados geográficos e de geolocalização (Ex: GEOMETRY, POINT, POLYGON).

---------------------------------------------------------------------------------------------------------

CONCEITOS BÁSICOS DE ESTRUTURA

Para começar, entende-se a hierarquia de um banco de dados relacional da seguinte forma: um BANCO DE DADOS possui TABELAS, que por sua vez possuem REGISTROS (linhas ou tuplas), e esses REGISTROS são compostos por CAMPOS (colunas ou atributos).

Para criar um novo banco de dados, utiliza-se o comando:
CREATE DATABASE nome_do_banco;

Para criar tabelas, utiliza-se o comando:
CREATE TABLE nome_da_tabela ( ... );

. Regra dos parênteses: Dentro dos parênteses do comando CREATE TABLE, colocamos os nomes e tipos dos campos a serem utilizados, SEMPRE SEPARADOS POR VÍRGULA. Apenas o último campo da lista NÃO leva vírgula antes do fechamento dos parênteses.

. Na frente de cada campo, é obrigatório identificar o seu tipo primitivo e tamanho (quando necessário), conforme o exemplo abaixo:

nome varchar(30),
idade tinyint(3),
peso float,
sexo char(1),
altura float,
nacionalidade varchar(20)

---------------------------------------------------------------------------------------------------------

DICAS E COMANDOS DE AMBIENTE

. Atalho essencial: No MySQL Workbench, o atalho para executar a linha de comando atual (onde o cursor está posicionado) é Ctrl + Enter.

. Para apagar um banco de dados completo e todos os seus dados permanentemente, utiliza-se o comando:
DROP DATABASE nome_do_banco;

----------------------------------------------------------------------------------------------------------

PADRONIZAÇÃO E INTERNACIONALIZAÇÃO (CHARSET)

Para criar um banco de dados robusto e preparado para o idioma português, configuramos parâmetros de codificação de caracteres logo após o CREATE DATABASE. Isso garante o suporte correto a acentos, cedilhas e caracteres especiais:

CREATE DATABASE cadastro
DEFAULT CHARACTER SET utf8mb4
DEFAULT COLLATE utf8mb4_general_ci;

*(Nota: O uso de utf8mb4 é o padrão moderno recomendado para o MySQL, pois além de caracteres latinos, oferece suporte completo até para emojis).*

----------------------------------------------------------------------------------------------------------

RESTRICÕES DE COLUNAS (CONSTRAINTS)

Para criar tabelas mais estruturadas, seguras e detalhadas, definimos regras de comportamento para as colunas (chamadas de constraints). Veja o exemplo de uma tabela estruturada:

CREATE TABLE pessoas (
    nome varchar(30) NOT NULL,
    nascimento date,
    sexo enum('M', 'F'),
    peso decimal(5, 2),
    altura decimal(3, 2),
    nacionalidade varchar(20) DEFAULT 'Brasil'
) DEFAULT CHARSET = utf8mb4;

. A restrição NOT NULL força o preenchimento obrigatório daquele campo. No exemplo acima, o banco rejeitará qualquer tentativa de cadastro que deixe o "nome" em branco.

. O tipo primitivo ENUM funciona como uma restrição de lista fechada. No campo "sexo", o banco só aceitará os valores explicitamente definidos entre aspas e separados por vírgula ('M' ou 'F'). Qualquer outro valor inserido causará um erro.

. No campo "peso" e "altura", utilizamos o tipo DECIMAL para obter precisão numérica exata (evitando os arredondamentos incorretos do tipo FLOAT). Na configuração decimal(5, 2), o primeiro número (5) representa o total de dígitos que a memória irá guardar, enquanto o segundo número (2) indica quantos desses dígitos serão após a vírgula. Exemplos válidos: 105.12, 65.29, 7.50.

. A restrição DEFAULT serve para definir um valor padrão. No campo "nacionalidade", se o usuário omitir essa informação durante o cadastro, o MySQL preencherá o campo de forma automática com o texto 'Brasil'.

----------------------------------------------------------------------------------------------------------

A IMPORTÂNCIA DA CHAVE PRIMÁRIA (PRIMARY KEY)

. Em um banco de dados profissional, todo registro precisa de uma identidade única que o diferencie dos demais. Duas pessoas podem ter exatamente o mesmo nome, peso e altura, mas precisam ter identificadores diferentes (como o CPF no mundo real, ou uma Matrícula). Essa é a função da Chave Primária (PRIMARY KEY).

. Para implementar uma Chave Primária com numeração automática, adicionamos a coluna correspondente no início e a regra no encerramento da tabela:

CREATE TABLE pessoas (
    id int NOT NULL AUTO_INCREMENT,
    nome varchar(30) NOT NULL,
    nascimento date,
    sexo enum('M', 'F'),
    peso decimal(5, 2),
    altura decimal(3, 2),
    nacionalidade varchar(20) DEFAULT 'Brasil',
    PRIMARY KEY (id)
) DEFAULT CHARSET = utf8mb4;

. A propriedade AUTO_INCREMENT faz com que o próprio MySQL gerencie a numeração sequencial dos registros (1, 2, 3, 4...). O desenvolvedor não precisa se preocupar em adivinhar qual é o próximo número.

. Existe também a restrição UNIQUE. Enquanto a Chave Primária é o identificador principal da linha, a constraint UNIQUE garante que uma coluna secundária não possua valores repetidos no banco de dados (muito utilizada para colunas de E-mail, CPF ou Título de Eleitor).

----------------------------------------------------------------------------------------------------------

MANIPULAÇÃO DE DADOS: INSERÇÃO (INSERT INTO)

. Para alimentar a tabela com dados, utilizamos o comando DML chamado INSERT INTO, especificando o nome da tabela, a lista de colunas desejadas e, em seguida, a cláusula VALUES com os respectivos registros:

INSERT INTO pessoas (id, nome, nascimento, sexo, peso, altura, nacionalidade)
VALUES (DEFAULT, 'Roberto', '1996-08-07', 'M', 95.50, 1.85, 'Brasil');

. Atenção às regras: Os valores textuais e datas devem ficar entre aspas simples (' '), os números decimais utilizam ponto (.) como separador, e todos os valores devem seguir rigorosamente a mesma ordem das colunas declaradas.

. Atalho de inserção: Se você for preencher TODOS os campos da tabela e possuir os dados na ordem exata em que as colunas foram criadas, a declaração inicial das colunas pode ser omitida:

INSERT INTO pessoas VALUES (DEFAULT, 'Roberto', '1996-08-07', 'M', 95.50, 1.85, 'Brasil');

. Inserção múltipla: Para cadastrar vários registros de uma única vez (otimizando a performance do banco), separamos os blocos de dados por VÍRGULA e inserimos o PONTO E VÍRGULA (;) apenas no final do último bloco:

INSERT INTO pessoas VALUES
(DEFAULT, 'Cassia', '1995-02-28', 'F', 60.5, 1.65, 'Brasil'),
(DEFAULT, 'Murilo', '2025-08-10', 'M', 12.0, 1.00, 'Brasil'),
(DEFAULT, 'Roberto', '1996-08-07', 'M', 95.5, 1.85, 'Brasil');

. O uso do DEFAULT no campo ID aciona o mecanismo do AUTO_INCREMENT, instruindo o banco a calcular e preencher o próximo número da sequência de forma automática.

----------------------------------------------------------------------------------------------------------

CONCEITOS COMPLEMENTARES: DDL VS DML

As instruções SQL são divididas em subgrupos de acordo com o seu objetivo no banco de dados:

. Comandos DDL (Data Definition Language): São comandos de DEFINIÇÃO de estrutura. Eles manipulam os objetos do banco de dados, ou seja, criam, alteram ou destroem as tabelas e colunas em si (Exemplos: CREATE DATABASE, CREATE TABLE, ALTER TABLE, DROP TABLE, RENAME TABLE).

. Comandos DML (Data Manipulation Language): São comandos de MANIPULAÇÃO de dados. Eles interagem diretamente com as informações salvas dentro das linhas das tabelas (Exemplos: INSERT INTO, UPDATE, DELETE).

----------------------------------------------------------------------------------------------------------

MODIFICANDO A ESTRUTURA DAS TABELAS (ALTER TABLE)

Quando precisamos realizar manutenções ou evoluções na estrutura de uma tabela já existente, utilizamos comandos DDL iniciando com a instrução ALTER TABLE:

. Para adicionar uma nova coluna comum ao final da tabela:
ALTER TABLE pessoas ADD COLUMN profissao varchar(20);

. Para adicionar uma nova coluna em uma posição específica (logo após uma coluna de referência):
ALTER TABLE pessoas ADD COLUMN profissao varchar(20) AFTER nome;

. Para adicionar uma nova coluna na primeiríssima posição da tabela:
ALTER TABLE pessoas ADD COLUMN profissao varchar(20) FIRST;

. Para modificar as propriedades internas de uma coluna (como alterar o seu tipo primitivo ou adicionar NOT NULL):
ALTER TABLE pessoas MODIFY COLUMN profissao varchar(30) NOT NULL;

. Para renomear o nome de uma coluna e alterar suas propriedades ao mesmo tempo:
ALTER TABLE pessoas CHANGE COLUMN profissao cargo varchar(30);

. Para excluir permanentemente uma coluna e todos os dados armazenados nela:
ALTER TABLE pessoas DROP COLUMN cargo;

. Para renomear o nome da tabela inteira:
ALTER TABLE pessoas RENAME TO gafanhotos;

. Para definir uma Chave Primária em uma tabela que foi criada sem ela:
ALTER TABLE cursos ADD PRIMARY KEY (idcurso);

. Para excluir uma tabela inteira do banco de dados:
DROP TABLE nome_da_tabela;

. Para verificar detalhadamente a estrutura estrutural atual de uma tabela (nomes, tipos, restrições e chaves):
DESCRIBE pessoas; (ou simplesmente: DESC pessoas;)

. Boas práticas de criação: Para evitar que o script falhe tentando criar uma tabela que já existe no sistema, adicionamos a cláusula de verificação IF NOT EXISTS:
CREATE TABLE IF NOT EXISTS nome_da_tabela ( ... );

----------------------------------------------------------------------------------------------------------

MODIFICANDO E EXCLUINDO REGISTROS (UPDATE E DELETE)

Para alterar ou remover dados que já estão salvos nas linhas das tabelas, utilizamos comandos DML combinados com filtros de seleção:

. O comando UPDATE altera informações armazenadas. A cláusula SET especifica a coluna e o novo valor, enquanto a cláusula WHERE cria a condição de filtro (geralmente apontando para o ID do registro) para determinar qual linha exata será modificada.

UPDATE cursos
SET nome = 'HTML5'
WHERE idcurso = 1;

. Para atualizar múltiplos campos de uma mesma linha simultaneamente, separamos as atribuições na cláusula SET por vírgula:

UPDATE cursos
SET nome = 'PHP', ano = '2015'
WHERE idcurso = 4;

. ⚠️ Trava de segurança essencial (LIMIT): O comando UPDATE é extremamente perigoso. Se a cláusula WHERE for omitida ou escrita incorretamente, o banco atualizará TODAS as linhas da tabela. Como boa prática de segurança em ambientes de desenvolvimento, utilizamos o comando LIMIT 1 no final do bloco para garantir que, mesmo em caso de erro no filtro, apenas uma única linha seja afetada:

UPDATE cursos
SET nome = 'Java', carga = 40, ano = '2015'
WHERE idcurso = 5
LIMIT 1;

. Para excluir linhas específicas de uma tabela, utilizamos o comando DELETE FROM associado obrigatoriamente a uma condição de filtro WHERE:

DELETE FROM cursos
WHERE idcurso = 8;

. Para esvaziar completamente uma tabela, apagando todas as suas linhas de forma ultra rápida e reiniciando o contador do AUTO_INCREMENT de volta para o número 1, utiliza-se o comando DDL:
TRUNCATE TABLE nome_da_tabela;

----------------------------------------------------------------------------------------------------------

GERENCIAMENTO E SEGURANÇA (BACKUP E RESTAURAÇÃO)

. No ecossistema de bancos de dados, o termo técnico utilizado para se referir à cópia de segurança e exportação dos dados é DUMP.

. Passo a passo para gerar um Backup (Export) no MySQL Workbench:
Menu superior SERVER >> DATA EXPORT >> Selecione o banco de dados desejado >> Selecione as tabelas envolvidas >> Escolha o tipo de Dump no menu suspenso (Selecione "Dump Structure and Data" para fazer a cópia completa da estrutura das tabelas e dos registros) >> Marque a opção "Export to Self-Contained File" (Arquivo Único) >> Defina a pasta de destino no seu computador >> Ative a caixa de seleção **INCLUDE CREATE SCHEMA** (isso fará com que o arquivo inclua as instruções de criação do banco de dados automaticamente, eliminando a necessidade de criá-lo manualmente na máquina de destino) >> Clique no botão START EXPORT (insira a senha do banco caso seja solicitada). Por padrão, se não alterado, o arquivo será salvo na pasta Documentos/Dump do Windows.

. Passo a passo para restaurar um Backup (Import) no MySQL Workbench:
Menu superior SERVER >> DATA IMPORT >> Selecione a opção correspondente ao seu modelo de exportação (Pasta ou Arquivo único) >> Localize o arquivo do DUMP no computador >> Clique no botão START IMPORT.

----------------------------------------------------------------------------------------------------------

AMBIENTES DE GERENCIAMENTO GRÁFICO (PHP_MY_ADMIN)

O phpMyAdmin é uma ferramenta de código aberto baseada na web projetada para lidar com a administração do MySQL. Nele, a criação de bancos de dados, tabelas, chaves e restrições pode ser feita de forma visual, automatizada e intuitiva através de telas e formulários, poupando o desenvolvedor de escrever códigos DDL manualmente para operações rotineiras.

----------------------------------------------------------------------------------------------------------

A ARTE DA CONSULTA DE DADOS (COMANDOS SELECT)

O comando SELECT é a ferramenta do grupo DQL (Data Query Language) utilizada para filtrar, extrair e exibir as informações salvas no banco de dados.

. O caractere asterisco (*) funciona como um caractere curinga, instruindo o banco a selecionar TODAS as colunas disponíveis na tabela:
SELECT * FROM nome_da_tabela;

. A cláusula ORDER BY organiza a exibição das linhas com base em uma coluna informada. Por padrão, a ordenação ocorre de forma ascendente (Ordem alfabética de A-Z ou numérica do menor para o maior).

. Para inverter a ordenação e exibir os dados de forma decrescente (Z-A ou do maior para o menor), adicionamos a palavra-chave DESC (Descendente) logo após o nome da coluna:
SELECT * FROM cursos ORDER BY nome DESC;

. Para otimizar o tráfego de dados e exibir apenas colunas específicas no painel de resultados, removemos o asterisco e listamos os campos desejados separados por vírgula:
SELECT nome, profissao, nascimento FROM pessoas;

. Para extrair registros específicos aplicando critérios de filtragem nas linhas, acoplamos a cláusula WHERE à consulta:

SELECT * FROM cursos
WHERE ano = 2016
ORDER BY nome;

. Operadores relacionais permitidos na cláusula WHERE:
  - = (Igual)
  - > (Maior que)
  - < (Menor que)
  - >= (Maior ou igual a)
  - <= (Menor ou igual a)
  - != ou <> (Diferente de)

. Seleção por intervalo integrado (BETWEEN): Permite buscar registros que estejam compreendidos dentro de uma faixa de valores mínima e máxima (inclusive). Exige a utilização do operador lógico AND para conectar os limites:

SELECT nome, ano FROM cursos
WHERE ano BETWEEN 2014 AND 2016;

. Seleção por lista de correspondência (IN): Permite filtrar registros que correspondam exatamente aos valores específicos declarados dentro dos parênteses, funcionando de maneira diferente do BETWEEN:

SELECT nome, descricao, ano FROM cursos
WHERE ano IN (2014, 2015);

. Sofisticação de filtros: Operadores lógicos avançados como AND (E), OR (OU) e NOT (NÃO) podem ser combinados livremente na cláusula WHERE para estruturar consultas com critérios cirúrgicos de filtragem.

. Para filtrarmos os campos de acordo com alguma palavra especifica, utilizamos o comando LIKE, segue o exemplo:

Select * from nomes
Where nome LIKE 'P%';

. Nesse comamando ele filtrará todos os nomes que COMEÇAM com a letra 'P'
. O simbolo de PORCENTO significa que é um curinga, onde ele substitui nenhum, ou todos os caracteres, LEMBRANDO QUE A POSIÇÃO DO PORCENTO IMPORTA, COLOCANDO O SINAL % ANTES DA LETRA ELE FILTRA TUDO QUE TERMINA COM A LETRA EM QUESTÃO, JA COLOCANDO O SINAL APÓS A LETRA, E FILTRA TUDO QUE COMEÇA COM A LETRA EM QUESTÃO, E PARA FILTRAR COM A LETRA EM QUESTAO EM QUALQUER POSIÇÃO, UTILIZA-SE O SINAL DE % ANTES E DEPOIS DA LETRA
. Para fazer o filtro de um campo que nao contenha uma letra em especifica utilizamos o NOT LIKE, segue o exemplo:

Select * from nomes
Where nome NOT LIKE 'p%';

. Nesse caso ele filtrará tudo o que NAO contem a letra 'P'

. No caso do simbolo % ele filtra tanto com ou sem caracteres no campo em questao, ja o simbolo UNDERLINE (_) ele exige que tenha algum caracter após o filtro especificado, seja letra ou numero

. Com o comando DISTINCT o filtro puxará somente um valor de cada campo, se tiver varios campos com o mesmo valor, como por exemplo a NACIONALIDADE das pessoas no banco de dados, ele irá puxar somente uma nacionalidade de cada nacionalidade cadastrada, simplificando, ele ignora valores repetitivos. 

. Para contar a quantidade de registros de um campo, utiliza-se COUNT(), onde podemos definir o que será contado, qual campo, sera contado, ou se sera contado tudo, utilizando ASTERISTICO(*), segue o exemplo:

select COUNT(*) from cursos;

. Para filtramos o maior valor de um campo, utilizamos o comando MAX, segue o exemplo:

select MAX(carga) from cursos;

. Neste caso ele filtra o curso com a maior carga de horas

. Usando o mesmo conceito podemos utiliza o comando MIN, que pega o menor valor de um campo

. Podemos usar o comando SUM para somar o conteudo de um campo, como por exemplo quantas aulas tem no total o banco de dados CURSO, segue o exemplo:

select SUM(totaulas) from cursos;

. Para usar o filtro e tirar a media de algum valor, usamos o comando AVG

select AVG(totaulas) from cursos;