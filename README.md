# Meus-Estudos-Tech

Repositório dedicado ao registro da minha jornada de estudos em tecnologia, centralizando anotações, exercícios e projetos práticos

----------------------------------------------------------------------------------------------------------

TIPOS PRIMITIVOS SQL

. Numérico
Sub Tipos : Inteiros , Reais e Lógicos

. Data/Tempo

. Literal
Sub Tipos: Caracteres , Textos , Binários e Coleções

. Espacial

---------------------------------------------------------------------------------------------------------

Para começar entende-se que BANCO DE DADOS possuem TABELAS que por sua vez TABELAS possuem REGISTROS que por sua vez REGISTROS são compostos por CAMPOS

Para criar um novo banco de dados utiliza-se CREATE DATABASE (nome do banco de dados)

Para criar TABELAS utiliza-se CREATE TABLE (nome da tabela) (

. Dentro desse parenteses, colocamos os nomes dos registros a serem utilizados, SEMPRE COLOCANDO VIRGULA APOS CADA REGISTRO, E SOMENTE NO ULTIMO REGISTRO NAO UTILIZA-SE A VIRGULA

. Na frente de cada registro precisa identificar exatamente o tipo primitivo de cada um, como egue os exemplos:

nome varchar(30),
idade tinyint(3),
peso float,
sexo char(1),
altura float,
nacionalidade varchar(20)
);
 
---------------------------------------------------------------------------------------------------------

Atalho para executar comandos Ctrl + Enter

Para apagar um banco de dados devemos criar um novo SQL FILE e depois utilizar o comando DROP DATABASE (nome do banco de dados);

----------------------------------------------------------------------------------------------------------

Para criar um banco de dados mais padronizados vamos configurar comandos após o CREATE DATABASE

create database cadastro
default character set utf8
default collate utf8_general_ci;

esses comandos são para criar um banco de dados que suportam caracteres especiais, que serão muito usados.

----------------------------------------------------------------------------------------------------------

Para criar tabelas mais estruturadas e bem mais detalhadas vamos definir algumas regras (contraits), segue o exemplo da nova tabela criada:

create table pessoas(
    nome varchar() NOT NULL,
    nascimento date,
    sexo enum('M' , 'F'),
    peso decimal (5 , 2),
    altura decimal (3 , 2),
    nacionalidade varchar(20) DEFAULT 'Brasil'
) default charset = utf8;

. Lembrando que a regra NOT NULL, força o preenchimento da linha em questão, no caso do exemplo o nome da pessoa a ser cadastrada.

. Ja no campo de SEXO o tipo primitivo ENUM força o preenchimento do campo com algum valor ja pré definido, no caso M ou F de masculino ou feminino, lembrando de sempre definir entre os parenteses os valores que serao permitidos, utilizando aspas e virgula para separar os valores.

. No campo de peso utilizamos o tipo primitivo decimal para definir com precisão o tamno do espaço que sera utilizado, no caso do 5 , 2 o primeiro numero (5) é a quantidade de casas que sera usado na memoria, já o segundo numero (2) é a quantidade de casas que ficaram após a virgula, sendo assim qualquer que peso que for colocado sera divido exatamente da forma certa, como por Exemplo: 105,12Kg , 65,29Kg ...

. No campo de nacionalidade Vamos usar a regra (constraints) DEFAULT ' ' nesse caso o DEFAULT serve para caso o campo nao seja preenchido com nenhuma informação, automaticamente ele sera preenchido com a informação que foi colocado entre as ASPAS após o DEFAULT, no caso 'Brasil'

----------------------------------------------------------------------------------------------------------

. Importante para um banco de dados criar um campo de CHAVE PRIMARIA, que consiste em criar um valor que diferencia duas ou mais pessoas, como por exemplo o CPF de uma pessoa ou uma MATRICULA de faculdade e afins, sendo que duas pessoas podem ter o mesmo nome, mas nunca terao o mesmo CPF

. Para criar uma CHAVE PRIMARIA vamos adicionar uma linha no começo da TABELA e uma no final

. No começo da tabela vamos criar o ID e na utltima linha vamos criar o PRIMARY KEY(id) segue o exemplo: 

create table pessoas(
    id int NOT NULL AUTO_INCREMENT,
    nome varchar() NOT NULL,
    nascimento date,
    sexo enum('M' , 'F'),
    peso decimal (5 , 2),
    altura decimal (3 , 2),
    nacionalidade varchar(20) DEFAULT 'Brasil',
    primary key(id)
) default charset = utf8;

. No campo de ID, vamos usar duas regras o NOT NULL para que o campo seja OBRIGATORIAMENTE preenchido e o AUTO_INCREMENT que serve para o sistema automaticamente preencher a ordem de pessoas cadastradas, como por exemplo: primeira pessoa, segunda pessoa, terceira pessoa...

. Temos tambem o caso de NOT NULL UNIQUE, que refesse a um nome que nao pode ser repetido, exatamente igual, por exemplo dois nomes 'Roberto'.

. Ja no campo PRIMARY KEY ele cria a chave primaria, que assim nao deixa cadastrar duas pessoas exatamente iguais no banco de dados

----------------------------------------------------------------------------------------------------------

. Para inserir dados no banco de dados utiliza-se o comando INSERT INTO (nome da tabela) e logo abaixo dessa linha de comando criamos uma lista com o nome dos parametros ja criados anteriormente na tabela, segue o EX:

INSERT INTO PESSOAS
(id, nome, nascimento, sexo, peso, altura, nacionalidade)

. E logo após utilisamos VALUES, segue o exemplo: 

VALUES
('1', 'Roberto', '1996-08-07', 'M', '95.50', '1.85', 'Brasil');

. As linhas do codigo ficam da seguinte forma: 

INSERT INTO PESSOAS
(id, nome, nascimento, sexo, peso, altura, nacionalidade)
VALUES
('1', 'Roberto', '1996-08-07', 'M', '95.50', '1.85', 'Brasil');

. Lembrando de sempre utilizar a virgula para separar os valores, de sempre colocar os valores na mesma ordem do que esta sendo pedido, EX: nome, colocar o nome da pessoa, nascimento, colocar a data de nascimento da pessoa...

. Caso os valores a serem inseridos na tabela, estiverem na mesma sequencia dos campos inseridos no banco, não precisa criar a lista com os nomes de cada campo, segue o exemplo: 

INSERT INTO pessoas VALUES
('1', 'Roberto', '1996-08-07', 'M', '95.50', '1.85', 'Brasil');

. Para adicionar mais de uma pessoa de uma unica vez, ao inves de utilizar o ponto e virgula no final de cada informação de pessoa, utiliza-se somente a VIRGULA, segue o exemplo da inserção de 3 pessoas ao mesmo tempo: 

INSERT INTO pessoas VALUES
(default ,'Cassia', '1995-02-28', 'F', '60.5', '1.65', 'Brasil'),
(default, 'Murilo', '2025-08-10', 'M', '12.0', '1.00', 'Brasil'),
(default, 'Roberto', '1996-08-07', 'M', '95.5', '1.85', 'Brasil');

. Lembrando que sempre pra encerrar a linha de comando utilizar o PONTO E VIRGULA (;)

. Neste caso estamos usando a regra(constraints) DEFAULT, porque quando criamos os campos de ID e NACIONALIDADE, definimos valores padrões como por exemplo na NACIONALIDADE 'Brasil', quando usamos DEFAULT o sistema preenchera automaticamente com o que ja definimos previamente na criação do campo, no caso do ID temos a regra(constraints) AUTO_INCREMENT que nesse caso ele preencherá de forma automatica a sequencia de pessoas cadastradas.

----------------------------------------------------------------------------------------------------------

. Para firmar conhecimento comandos DDL's(DATA DEFINITION LANGUAGE) são comandos de DEFINIÇÃO, que são para definir a estrutura do banco de dados, como por exemplo o CREATE DATABASE e CREATE TABLE

. Comandos DML's(DATA MANIPULATION LANGUAGE) são comandos para MANIPULAÇÕES de dados como por exemplo INSERT INTO

----------------------------------------------------------------------------------------------------------

. Temos um comando para alterar a tabela no banco de dados, e esse comando é ALTER TABLE (nome da tabela) exemplo: 

ALTER TABLE pessoas

. Em seguida para adicionar algum campo novo na tabela, usamos ADD COLUMN (nome do campo que deseja adicionar) exemplo: 

ALTER TABLE pessoas
ADD COLUMN (nome do campo para adicioar)(Tipo primitivo);

. Para excluir um campo no banco de dados, utiliza-se o comando DROP COLUMN (nome do campo) exemplo:

ALTER TABLE pessoas
DROP COLUMN (nome do campo)

. Lembrando que COLUMN refere-se ao campo da tabela, como por exemplo o campo NOME, NASCIMENTO, PESO...

----------------------------------------------------------------------------------------------------------

. Para adicionar um campo em local especifico entre os campos que ja existem na tabela utilizamos o comando AFTER, segue o exemplo: 

ALTER TABLE (nome da tabela)
ADD COLUMN (nome do campo)(tipo primitivo) AFTER (nome do campo que sera utilizado de referencia para locaçao do novo campo)

. Ja para adicionar um campo em primeira posição na tabela utilizamos o comando FIRST, segue o exemplo:

ALTER TABLE (nome da tabela)
ADD COLUMN (nome do campo)(tipo primitivo) FIRST;

. Para alterar o valor de um tipo primitivo como por exemplo o campo PROFISSAO que esta com o VARCHAR(10), utilizamos o comando MODIFY COLUMN, segue o exemplo: 

ALTER TABLE pessoas
MODIFY COLUMN profissao varchar(20)

. Para renomear um campo ou uma regra(constrants) utilizamos o codigo CHANGE COLUMN, segue o exemplo:

ALTER TABLE pessoas
CHANGE COLUMN (nome do campo que vai ser alterado) (novo nome desse campo)(tipo primitivo)

. Para renomear a tabela toda, utiliza-se o comando RENAME TO, segue o exemplo:

alter table pessoas
RENAME TO (novo nome da tabela);

----------------------------------------------------------------------------------------------------------

. Um comando muito importante que serve para ver o conteudo que tem na tabela, é o DESCRIBE ou DESC, exemplo:

desc (nome da tabela);

. Ele mostrava todos os campos que a tabela possue

----------------------------------------------------------------------------------------------------------

. Para nao correr o risco de sobreescrever uma tabela ja criada, podemos utilizar o comando IF NOT EXISTS, isso faz com que a tabela nova só seja criada, se ela nao existir ja no banco de dados, segue o exemplo:

CREATE TABLE IF NOT EXISTS (nome da tabela)()