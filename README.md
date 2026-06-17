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

. Ja no campo PRIMARY KEY ele cria a chave primaria, que assim nao deixa cadastrar duas pessoas exatamente iguais no banco de dados