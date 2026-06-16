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
