# 📌 Meus Estudos Tech

Repositório dedicado ao registro da minha jornada de estudos em tecnologia, centralizando anotações, exercícios e projetos práticos baseados no curso de MySQL do Curso em Vídeo (Prof. Gustavo Guanabara).

---

## 🗺️ Sumário
* [1. Tipos Primitivos no SQL](#1-tipos-primitivos-no-sql)
* [2. Conceitos Básicos de Estrutura](#2-conceitos-básicos-de-estrutura)
* [3. Dicas e Comandos de Ambiente](#3-dicas-e-comandos-de-ambiente)
* [4. Padronização e Internacionalização (Charset)](#4-padronização-e-internacionalização-charset)
* [5. Restrições de Colunas (Constraints)](#5-restrições-de-colunas-constraints)
* [6. A Importância da Chave Primária (Primary Key)](#6-a-importância-da-chave-primária-primary-key)
* [7. Manipulação de Dados: Inserção (Insert Into)](#7-manipulação-de-dados-inserção-insert-into)
* [8. Conceitos Complementares: DDL vs DML](#8-conceitos-complementares-ddl-vs-dml)
* [9. Modificando a Estrutura das Tabelas (Alter Table)](#9-modificando-a-estrutura-das-tabelas-alter-table)
* [10. Modificando e Excluindo Registros (Update e Delete)](#10-modificando-e-excluindo-registros-update-e-delete)
* [11. Gerenciamento e Segurança (Backup e Restauração)](#11-gerenciamento-e-segurança-backup-e-restauração)
* [12. Ambientes de Gerenciamento Gráfico (phpMyAdmin)](#12-ambientes-de-gerenciamento-gráfico-phpmyadmin)
* [13. A Arte da Consulta de Dados (Comandos Select)](#13-a-arte-da-consulta-de-dados-comandos-select)
* [14. Modelo Relacional](#14-modelo-relacional)
* [15. Explicando o Join](#15-explicando-o-join)

---

## 1. Tipos Primitivos no SQL

Ao criar campos em uma tabela, precisamos definir a natureza dos dados que eles irão receber. Os principais tipos primitivos são:

* **Numéricos:**
  * **Inteiros:** Usados para contagens e números sem casas decimais (Ex: `TINYINT`, `INT`, `BIGINT`).
  * **Reais:** Usados para valores com casas decimais (Ex: `FLOAT`, `DOUBLE`, `DECIMAL`).
  * **Lógicos:** Usados para estados verdadeiro/falso (Ex: `BOOLEAN`, representado internamente como `TINYINT`).

* **Data/Tempo:** Usados para armazenar registros cronológicos (Ex: `DATE` para datas YYYY-MM-DD, `TIME` para horas, `DATETIME` e `TIMESTAMP` para data e hora, `YEAR` para anos).

* **Literais (Textos):**
  * **Caracteres:** `CHAR` (tamanho fixo, ideal para siglas como sexo ou estados) e `VARCHAR` (tamanho variável, economiza memória).
  * **Textos Longos:** `TEXT` e `LONGTEXT` (para descrições e grandes blocos de texto).
  * **Binários:** `BLOB` e `LONGBLOB` (para arquivos, imagens ou mídias armazenadas no banco).
  * **Coleções:** `ENUM` (lista fechada de opções pré-definidas) e `SET`.

* **Espaciais:** Usados para dados geográficos e de geolocalização (Ex: `GEOMETRY`, `POINT`, `POLYGON`).

[Subir para o Sumário](#sumário)

---

## 2. Conceitos Básicos de Estrutura

Para começar, entende-se a hierarquia de um banco de dados relacional da seguinte forma: um **BANCO DE DADOS** possui **TABELAS**, que por sua vez possuem **REGISTROS** (linhas ou tuplas), e esses **REGISTROS** são compostos por **CAMPOS** (colunas ou atributos).

Para criar um novo banco de dados, utiliza-se o comando:
```sql
CREATE DATABASE nome_do_banco;

```

Para criar tabelas, utiliza-se o comando:

```sql
CREATE TABLE nome_da_tabela ( ... );

```

* **Regra dos parênteses:** Dentro dos parênteses do comando `CREATE TABLE`, colocamos os nomes e tipos dos campos a serem utilizados, **SEMPRE SEPARADOS POR VÍRGULA**. Apenas o último campo da lista **NÃO** leva vírgula antes do fechamento dos parênteses.
* Na frente de cada campo, é obrigatório identificar o seu tipo primitivo e tamanho (quando necessário), conforme o exemplo abaixo:

```sql
nome varchar(30),
idade tinyint(3),
peso float,
sexo char(1),
altura float,
nacionalidade varchar(20)

```

[Subir para o Sumário](#sumário)

---

## 3. Dicas e Comandos de Ambiente

* **Atalho essencial:** No MySQL Workbench, o atalho para executar a linha de comando atual (onde o cursor está posicionado) é `Ctrl + Enter`.
* Para apagar um banco de dados completo e todos os seus dados permanentemente, utiliza-se o comando:

```sql
DROP DATABASE nome_do_banco;

```

[Subir para o Sumário](#sumário)

---

## 4. Padronização e Internacionalização (Charset)

Para criar um banco de dados robusto e preparado para o idioma português, configuramos parâmetros de codificação de caracteres logo após o `CREATE DATABASE`. Isso garante o suporte correto a acentos, cedilhas e caracteres especiais:

```sql
CREATE DATABASE cadastro
DEFAULT CHARACTER SET utf8mb4
DEFAULT COLLATE utf8mb4_general_ci;

```

*(Nota: O uso de `utf8mb4` é o padrão moderno recomendado para o MySQL, pois além de caracteres latinos, oferece suporte completo até para emojis).*

[Subir para o Sumário](#sumário)

---

## 5. Restrições de Colunas (Constraints)

Para criar tabelas mais estruturadas, seguras e detalhadas, definimos regras de comportamento para as colunas (chamadas de *constraints*). Veja o exemplo de uma tabela estruturada:

```sql
CREATE TABLE pessoas (
    nome varchar(30) NOT NULL,
    nascimento date,
    sexo enum('M', 'F'),
    peso decimal(5, 2),
    altura decimal(3, 2),
    nacionalidade varchar(20) DEFAULT 'Brasil'
) DEFAULT CHARSET = utf8mb4;

```

* A restrição `NOT NULL` força o preenchimento obrigatório daquele campo. No exemplo acima, o banco rejeitará qualquer tentativa de cadastro que deixe o "nome" em branco.
* O tipo primitivo `ENUM` funciona como uma restrição de lista fechada. No campo "sexo", o banco só aceitará os valores explicitamente definidos entre aspas e separados por vírgula (`'M'` ou `'F'`). Qualquer outro valor inserido causará um erro.
* No campo "peso" e "altura", utilizamos o tipo `DECIMAL` para obter precisão numérica exata (evitando os arredondamentos incorretos do tipo `FLOAT`). Na configuração `decimal(5, 2)`, o primeiro número (5) representa o total de dígitos que a memória irá guardar, enquanto o segundo número (2) indica quantos desses dígitos serão após a vírgula. Exemplos válidos: 105.12, 65.29, 7.50.
* A restrição `DEFAULT` serve para definir um valor padrão. No campo "nacionalidade", se o usuário omitir essa informação durante o cadastro, o MySQL preencherá o campo de forma automática com o texto `'Brasil'`.

[Subir para o Sumário](#sumário)

---

## 6. A Importância da Chave Primária (Primary Key)

* Em um banco de dados profissional, todo registro precisa de uma identidade única que o diferencie dos demais. Duas pessoas podem ter exatamente o mesmo nome, peso e altura, mas precisam ter identificadores diferentes (como o CPF no mundo real, ou uma Matrícula). Essa é a função da Chave Primária (`PRIMARY KEY`).
* Para implementar uma Chave Primária com numeração automática, adicionamos a coluna correspondente no início e a regra no encerramento da tabela:

```sql
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

```

* A propriedade `AUTO_INCREMENT` faz com que o próprio MySQL gerencie a numeração sequencial dos registros (1, 2, 3, 4...). O desenvolvedor não precisa se preocupar em adivinhar qual é o próximo número.
* Existe também a restrição `UNIQUE`. Enquanto a Chave Primária é o identificador principal da linha, a constraint `UNIQUE` garante que uma coluna secundária não possua valores repetidos no banco de dados (muito utilizada para colunas de E-mail, CPF ou Título de Eleitor).

[Subir para o Sumário](#sumário)

---

## 7. Manipulação de Dados: Inserção (Insert Into)

* Para alimentar a tabela com dados, utilizamos o comando DML chamado `INSERT INTO`, especificando o nome da tabela, a lista de colunas desejadas e, em seguida, a cláusula `VALUES` com os respectivos registros:

```sql
INSERT INTO pessoas (id, nome, nascimento, sexo, peso, altura, nacionalidade)
VALUES (DEFAULT, 'Roberto', '1996-08-07', 'M', 95.50, 1.85, 'Brasil');

```

* **Atenção às regras:** Os valores textuais e datas devem ficar entre aspas simples (`' '`), os números decimais utilizam ponto (`.`) como separador, e todos os valores devem seguir rigorosamente a mesma ordem das colunas declaradas.
* **Atalho de inserção:** Se você for preencher **TODOS** os campos da tabela e possuir os dados na ordem exata em que as colunas foram criadas, a declaração inicial das colunas pode ser omitida:

```sql
INSERT INTO pessoas VALUES (DEFAULT, 'Roberto', '1996-08-07', 'M', 95.50, 1.85, 'Brasil');

```

* **Inserção múltipla:** Para cadastrar vários registros de uma única vez (otimizando a performance do banco), separamos os blocos de dados por **VÍRGULA** e inserimos o **PONTO E VÍRGULA** (`;`) apenas no final do último bloco:

```sql
INSERT INTO pessoas VALUES
(DEFAULT, 'Cassia', '1995-02-28', 'F', 60.5, 1.65, 'Brasil'),
(DEFAULT, 'Murilo', '2025-08-10', 'M', 12.0, 1.00, 'Brasil'),
(DEFAULT, 'Roberto', '1996-08-07', 'M', 95.5, 1.85, 'Brasil');

```

* O uso do `DEFAULT` no campo ID aciona o mecanismo do `AUTO_INCREMENT`, instruindo o banco a calcular e preencher o próximo número da sequência de forma automática.

[Subir para o Sumário](#sumário)

---

## 8. Conceitos Complementares: DDL vs DML

As instruções SQL são divididas em subgrupos de acordo com o seu objetivo no banco de dados:

* **Comandos DDL (Data Definition Language):** São comandos de **DEFINIÇÃO** de estrutura. Eles manipulam os objetos do banco de dados, ou seja, criam, alteram ou destroem as tabelas e colunas em si (Exemplos: `CREATE DATABASE`, `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`, `RENAME TABLE`).
* **Comandos DML (Data Manipulation Language):** São comandos de **MANIPULAÇÃO** de dados. Eles interagem diretamente com as informações salvas dentro das linhas das tabelas (Exemplos: `INSERT INTO`, `UPDATE`, `DELETE`).

[Subir para o Sumário](#sumário)

---

## 9. Modificando a Estrutura das Tabelas (Alter Table)

Quando precisamos realizar manutenções ou evoluções na estrutura de uma tabela já existente, utilizamos comandos DDL iniciando com a instrução `ALTER TABLE`:

* Para adicionar uma nova coluna comum ao final da tabela:
```sql
ALTER TABLE pessoas ADD COLUMN profissao varchar(20);

```


* Para adicionar uma nova coluna em uma posição específica (logo após uma coluna de referência):
```sql
ALTER TABLE pessoas ADD COLUMN profissao varchar(20) AFTER nome;

```


* Para adicionar uma nova coluna na primeiríssima posição da tabela:
```sql
ALTER TABLE pessoas ADD COLUMN profissao varchar(20) FIRST;

```


* Para modificar as propriedades internas de uma coluna (como alterar o seu tipo primitivo ou adicionar `NOT NULL`):
```sql
ALTER TABLE pessoas MODIFY COLUMN profissao varchar(30) NOT NULL;

```


* Para renomear o nome de uma coluna e alterar suas propriedades ao mesmo tempo:
```sql
ALTER TABLE pessoas CHANGE COLUMN profissao cargo varchar(30);

```


* Para excluir permanentemente uma coluna e todos os dados armazenados nela:
```sql
ALTER TABLE pessoas DROP COLUMN cargo;

```


* Para renomear o nome da tabela inteira:
```sql
ALTER TABLE pessoas RENAME TO gafanhotos;

```


* Para definir uma Chave Primária em uma tabela que foi criada sem ela:
```sql
ALTER TABLE cursos ADD PRIMARY KEY (idcurso);

```


* Para excluir uma tabela inteira do banco de dados:
```sql
DROP TABLE nome_da_tabela;

```


* Para verificar detalhadamente a estrutura atual de uma tabela (nomes, tipos, restrições e chaves):
```sql
DESCRIBE pessoas; -- (ou simplesmente: DESC pessoas;)

```


* **Boas práticas de criação:** Para evitar que o script falhe tentando criar uma tabela que já existe no sistema, adicionamos a cláusula de verificação `IF NOT EXISTS`:
```sql
CREATE TABLE IF NOT EXISTS nome_da_tabela ( ... );

```



[Subir para o Sumário](#sumário)

---

## 10. Modificando e Excluindo Registros (Update e Delete)

Para alterar ou remover dados que já estão salvos nas linhas das tabelas, utilizamos comandos DML combinados com filtros de seleção:

* O comando `UPDATE` altera informações armazenadas. A cláusula `SET` especifica a coluna e o novo valor, enquanto a cláusula `WHERE` cria a condição de filtro (geralmente apontando para o ID do registro) para determinar qual linha exata será modificada.
```sql
UPDATE cursos
SET nome = 'HTML5'
WHERE idcurso = 1;

```


* Para atualizar múltiplos campos de uma mesma linha simultaneamente, separamos as atribuições na cláusula `SET` por vírgula:
```sql
UPDATE cursos
SET nome = 'PHP', ano = '2015'
WHERE idcurso = 4;

```


* ⚠️ **Trava de segurança essencial (LIMIT):** O comando `UPDATE` é extremamente perigoso. Se a cláusula `WHERE` for omitida ou escrita incorretamente, o banco atualizará **TODAS** as linhas da tabela. Como boa prática de segurança em ambientes de desenvolvimento, utilizamos o comando `LIMIT 1` no final do bloco para garantir que, mesmo em caso de erro no filtro, apenas uma única linha seja afetada:
```sql
UPDATE cursos
SET nome = 'Java', carga = 40, ano = '2015'
WHERE idcurso = 5
LIMIT 1;

```


* Para excluir linhas específicas de uma tabela, utilizamos o comando `DELETE FROM` associado obrigatoriamente a uma condition de filtro `WHERE`:
```sql
DELETE FROM cursos
WHERE idcurso = 8;

```


* Para esvaziar completamente uma tabela, apagando todas as suas linhas de forma ultra rápida e reiniciando o contador do `AUTO_INCREMENT` de volta para o número 1, utiliza-se o comando DDL:
```sql
TRUNCATE TABLE nome_da_tabela;

```



[Subir para o Sumário](#sumário)

---

## 11. Gerenciamento e Segurança (Backup e Restauração)

* No ecossistema de bancos de dados, o termo técnico utilizado para se referir à cópia de segurança e exportação dos dados é **DUMP**.
* **Passo a passo para gerar um Backup (Export) no MySQL Workbench:**
Menu superior `SERVER` >> `DATA EXPORT` >> Selecione o banco de dados desejado >> Selecione as tabelas envolvidas >> Escolha o tipo de Dump no menu suspenso (Selecione *"Dump Structure and Data"* para fazer a cópia completa da estrutura das tabelas e dos registros) >> Marque a opção *"Export to Self-Contained File"* (Arquivo Único) >> Defina a pasta de destino no seu computador >> Ative a caixa de seleção **INCLUDE CREATE SCHEMA** (isso fará com que o arquivo inclua as instruções de criação do banco de dados automaticamente, eliminando a necessidade de criá-lo manualmente na máquina de destino) >> Clique no botão `START EXPORT` (insira a senha do banco caso seja solicitada). Por padrão, se não alterado, o arquivo será salvo na pasta Documentos/Dump do Windows.
* **Passo a passo para restaurar um Backup (Import) no MySQL Workbench:**
Menu superior `SERVER` >> `DATA IMPORT` >> Selecione a opção correspondente ao seu modelo de exportação (Pasta ou Arquivo único) >> Localize o arquivo do DUMP no computador >> Clique no botão `START IMPORT`.

[Subir para o Sumário](#sumário)

---

## 12. Ambientes de Gerenciamento Gráfico (phpMyAdmin)

O **phpMyAdmin** é uma ferramenta de código aberto baseada na web projetada para lidar com a administração do MySQL. Nele, a criação de bancos de dados, tabelas, chaves e restrições pode ser feita de forma visual, automatizada e intuitiva através de telas e formulários, poupando o desenvolvedor de escrever códigos DDL manualmente para operações rotineiras.

[Subir para o Sumário](#sumário)

---

## 13. A Arte da Consulta de Dados (Comandos Select)

O comando `SELECT` é a ferramenta do grupo **DQL (Data Query Language)** utilizada para filtrar, extrair e exibir as informações salvas no banco de dados.

* O caractere asterisco (`*`) funciona como um caractere curinga, instruindo o banco a selecionar **TODAS** as colunas disponíveis na tabela:
```sql
SELECT * FROM nome_da_tabela;

```


* A cláusula `ORDER BY` organiza a exibição das linhas com base em uma coluna informada. Por padrão, a ordenação ocorre de forma ascendente (Ordem alfabética de A-Z ou numérica do menor para o maior).
* Para inverter a ordenação e exibir os dados de forma decrescente (Z-A ou do maior para o menor), adicionamos a palavra-chave `DESC` (Descendente) logo após o nome da coluna:
```sql
SELECT * FROM cursos ORDER BY nome DESC;

```


* Para otimizar o tráfego de dados e exibir apenas colunas específicas no painel de resultados, removemos o asterisco e listamos os campos desejados separados por vírgula:
```sql
SELECT nome, profissao, nascimento FROM pessoas;

```


* Para extrair registros específicos aplicando critérios de filtragem nas linhas, acoplamos a cláusula `WHERE` à consulta:
```sql
SELECT * FROM cursos
WHERE ano = 2016
ORDER BY nome;

```


* **Operadores relacionais permitidos na cláusula WHERE:**
* `=` (Igual)
* `>` (Maior que)
* `<` (Menor que)
* `>=` (Maior ou igual a)
* `<=` (Menor ou igual a)
* `!=` ou `<>` (Diferente de)


* **Seleção por intervalo integrado (BETWEEN):** Permite buscar registros que estejam compreendidos dentro de uma faixa de valores mínima e máxima (inclusive). Exige a utilização do operador lógico `AND` para conectar os limites:
```sql
SELECT nome, ano FROM cursos
WHERE ano BETWEEN 2014 AND 2016;

```


* **Seleção por lista de correspondência (IN):** Permite filtrar registros que correspondam exatamente aos valores específicos declarados dentro dos parênteses, funcionando de maneira diferente do `BETWEEN`:
```sql
SELECT nome, descricao, ano FROM cursos
WHERE ano IN (2014, 2015);

```


* **Sofisticação de filtros:** Operadores lógicos avançados como `AND` (E), `OR` (OU) e `NOT` (NÃO) podem ser combinados livremente na cláusula `WHERE` para estruturar consultas com critérios cirúrgicos de filtragem.
* Para filtrarmos os campos de acordo com alguma palavra específica, utilizamos o comando `LIKE`. Veja o exemplo:
```sql
SELECT * FROM nomes
WHERE nome LIKE 'P%';

```


* Nesse comando, ele filtrará todos os nomes que **COMEÇAM** com a letra 'P'.
* O símbolo de **porcento (%)** significa que é um curinga, substituindo nenhum ou múltiplos caracteres. **Lembrando que a posição do porcento importa:** colocar o sinal `%` antes da letra filtra tudo que **termina** com a letra em questão; colocar o sinal após a letra filtra tudo que **começa** com ela; e para filtrar a letra em qualquer posição, utiliza-se o sinal de `%` antes e depois (`%letra%`).


* Para fazer o filtro de um campo que **não** contenha uma letra específica, utilizamos o `NOT LIKE`:
```sql
SELECT * FROM nomes
WHERE nome NOT LIKE 'P%';

```


* Nesse caso, ele filtrará tudo o que **NÃO** contém a letra 'P' no início.
* Enquanto o símbolo `%` aceita qualquer quantidade de caracteres (ou nenhum), o símbolo de **underline (_)** exige que haja **exatamente um caractere** naquela posição específica do filtro.


* Com o comando `DISTINCT`, o filtro puxará somente um valor de cada campo. Se houver vários registros com o mesmo valor (como a nacionalidade de várias pessoas), ele trará a lista sem repetições, ignorando valores duplicados.
* Para contar a quantidade de registros de um campo, utiliza-se `COUNT()`, onde podemos definir o campo específico ou contar todas as linhas usando o asterisco (`*`):
```sql
SELECT COUNT(*) FROM cursos;

```


* Para filtrarmos o maior valor de um campo, utilizamos o comando `MAX`:
```sql
SELECT MAX(carga) FROM cursos;

```


* Neste caso, ele filtra o curso com a maior carga horária.


* Usando o mesmo conceito, podemos utilizar o comando `MIN`, que pega o menor valor de um campo.
* Podemos usar o comando `SUM` para somar o conteúdo numérico de um campo, por exemplo, o total de aulas combinadas de todos os cursos:
```sql
SELECT SUM(totaulas) FROM cursos;

```


* Para tirar a média de algum valor, usamos o comando `AVG`:
```sql
SELECT AVG(totaulas) FROM cursos;

```


* Para agruparmos valores através de um filtro, utilizamos o comando `GROUP BY`:
```sql
SELECT carga FROM cursos
GROUP BY carga;

```


* Podemos filtrar o agrupamento e mostrar quantos cursos contêm cada carga horária utilizando funções de agregação junto com o agrupamento:
```sql
SELECT carga, COUNT(*) FROM cursos
GROUP BY carga;

```


* O comando `HAVING` funciona de forma similar ao `WHERE`, porém ele é aplicado especificamente para filtrar os resultados que já foram agrupados pelo `GROUP BY`.

[Subir para o Sumário](#sumário)

---

## 14. Modelo Relacional

* No conceito de modelos relacionais, temos alguns tipos de cardinalidades, como: **Muitos para Muitos (N:N)**, **Um para Um (1:1)** e **Um para Muitos (1:N)**.
* **No modelo Muitos para Muitos (N:N):** As duas tabelas se relacionam de forma que um dado de uma tabela pode estar relacionado com vários registros da outra, e vice-versa.
* **No modelo Um para Um (1:1):** Trata-se do cenário onde um registro de uma tabela pode se relacionar com apenas um único registro da outra tabela.
* **No modelo Um para Muitos (1:N):** Trata-se do cenário onde um registro de uma tabela (lado 1) pode se relacionar com vários registros da outra tabela (lado N), mas os registros do lado N podem se relacionar com apenas um único registro do lado 1.
* Lembrando que nem sempre um registro precisa obrigatoriamente se relacionar com outro.
* Uma **Chave Estrangeira (FOREIGN KEY - FK)** é a Chave Primária de uma tabela que é inserida em outra tabela para criar o relacionamento entre elas.
* **Relacionamento Um para Um (1:1):** Antes de criar, decidimos conceitualmente qual tabela é a "superior" (ou principal), e então jogamos a Chave Primária da outra tabela para dentro dela, configurando-a como Chave Estrangeira.
* **Relacionamento Um para Muitos (1:N):** **SEMPRE** pegamos a Chave Primária da tabela que representa o lado "UM" e a inserimos na tabela que representa o lado "MUITOS", cadastrando-a como Chave Estrangeira.
* **Relacionamento Muitos para Muitos (N:N):** **CRIAMOS UMA NOVA TABELA (tabela intermediária/pivô)** para mapear o relacionamento. Essa nova tabela conterá, no mínimo, as Chaves Primárias de ambas as tabelas originais, transformando-as em Chaves Estrangeiras, além de poder conter atributos próprios do relacionamento.
* Antes de definirmos a Chave Estrangeira, precisamos criar a coluna física que receberá esse valor:
```sql
ALTER TABLE gafanhotos
ADD COLUMN cursopreferido int;

```


* Para transformar essa coluna em uma **Chave Estrangeira**, utilizamos a restrição `ADD FOREIGN KEY`:
```sql
ALTER TABLE gafanhotos
ADD FOREIGN KEY (cursopreferido)
REFERENCES cursos(idcurso);

```


* **Explicando a estrutura:** `ALTER TABLE` inicia a alteração na tabela que vai receber o vínculo; `ADD FOREIGN KEY (coluna_local)` define qual coluna interna guardará a referência; e `REFERENCES tabela_destino(coluna_destino)` indica de onde essa informação está vindo (geralmente a Chave Primária da tabela referenciada).


* Para vincular os registros na prática (ex: associar o curso preferido a um aluno), usamos o comando DML `UPDATE`:
```sql
UPDATE gafanhotos 
SET cursopreferido = '6'
WHERE id = '1';

```


* No comando acima, atualizamos a tabela `gafanhotos`, definindo o valor `'6'` na coluna `cursopreferido` especificamente para o registro onde o `id` é igual a `'1'`.



[Subir para o Sumário](#sumário)

---

## 15. Explicando o Join

O comando `JOIN` é utilizado para fazer a relação entre duas tabelas, e temos alguns tipos dele no SQL.

### 1. INNER JOIN

Este comando só retornará um dado ou informação caso **ambas** as tabelas relacionadas contenham informações correspondentes com base na chave de ligação. Do contrário, ele ignora a linha e não mostra nada.

Para exemplificar, imagine duas tabelas: `CLIENTES` e `PRESENTES`.

#### Tabelas Originais:

**PRESENTES**

| id_pedido | id_cliente | produto |
| --- | --- | --- |
| 101 | 1 | Notebook |
| 102 | 2 | Celular |
| 103 | 99 | Mouse |

**CLIENTES**

| id_cliente | nome |
| --- | --- |
| 1 | Ana |
| 2 | Bruno |
| 3 | Carlos |

#### O Comportamento do INNER JOIN:

Analisando as tabelas acima, quando utilizamos o `INNER JOIN`, ele só retornará as informações que possuem par correspondente em ambas:

| nome | produto |
| --- | --- |
| Ana | Notebook |
| Bruno | Celular |

* **Por que os outros foram ignorados?**
* O cliente **Carlos** não aparece porque ele não possui nenhum registro de pedido na tabela `PRESENTES`.
* O produto **Mouse** não aparece porque o `id_cliente 99` não existe na tabela `CLIENTES`.



### 2. LEFT JOIN (ou LEFT OUTER JOIN)

Este comando prioriza totalmente a tabela posicionada à **esquerda** da cláusula `JOIN`. Ele retornará **todos** os registros dessa tabela da esquerda, independentemente de haver ou não uma informação correspondente na tabela da direita.

Se não houver correspondência, o SQL traz os dados da esquerda e preenche os campos da direita com `NULL` (vazio).

#### O Comportamento do LEFT JOIN (Considerando CLIENTES à esquerda):

```sql
SELECT clientes.nome, presentes.produto 
FROM clientes LEFT JOIN presentes 
ON clientes.id_cliente = presentes.id_cliente;

```

| nome | produto |
| --- | --- |
| Ana | Notebook |
| Bruno | Celular |
| Carlos | NULL |

* **Por que esse resultado?**
* **Ana** e **Bruno** possuem correspondência na tabela de presentes, então seus produtos aparecem normalmente.
* **Carlos** não comprou nada, mas como ele está na tabela da esquerda, ele **é obrigado a aparecer**. Como não há produto para ele, o banco preenche com `NULL`.
* O **Mouse** é completamente ignorado porque pertence à tabela da direita (`PRESENTES`) e não tem nenhum cliente correspondente na esquerda.



### 3. RIGHT JOIN (ou RIGHT OUTER JOIN)

Este comando funciona exatamente da mesma forma que o `LEFT JOIN`, mas com o lado invertido: ele prioriza totalmente a tabela posicionada à **direita** da cláusula `JOIN`. Ele retornará **todos** os registros da tabela da direita, mesmo que não haja correspondência na tabela da esquerda.

[Subir para o Sumário](https://www.google.com/search?q=%23%EF%B8%8F-sum%C3%A1rio)

```

```
