# Python, MySQL & Streamlit: Sistema de Gerenciamento de Jogos

Neste repositório, documento os meus estudos práticos sobre a integração entre bancos de dados relacionais (MySQL), scripts de automação em Python e a criação de interfaces web modernas com o Streamlit.

---

## Sumário de Conteúdos

1. [Primeiros Passos: Instalação e Ambiente](#primeiros-passos-instalação-e-ambiente)
2. [Conexão Básica com o MySQL](#conexão-básica-com-o-mysql)
3. [Módulos do Sistema (CRUD no Terminal)](#módulos-do-sistema-crud-no-terminal)
4. [Interface Web com Streamlit](#interface-web-com-streamlit)

---

## Primeiros Passos: Instalação e Ambiente

Para fazer o Python conversar com o MySQL e gerar a nossa interface web, precisamos instalar os seguintes conectores e bibliotecas no terminal:

```bash
# Instalação do driver oficial do banco de dados
pip install mysql-connector-python

# Instalação do framework web para a interface visual
pip install streamlit

```

---

## 🔌 Conexão Básica com o MySQL

O ponto de partida do projeto foi entender como abrir uma porta de comunicação entre o Python e o banco.

Para ler o guia passo a passo da primeira conexão, entender o funcionamento do `cursor`, do método `fetchone()` e de como criar tabelas direto via código (utilizando estruturas de segurança como `try/except/finally`), consulte a documentação detalhada no nosso arquivo de criação:
👉 **[Guia de Criação de Tabelas e Conexão (CriandoTabela.py)](CriandoTabela.py)**

---

## 📂 Módulos do Sistema (CRUD no Terminal)

O coração do nosso backend foi estruturado de forma modular (funções separadas em arquivos específicos) para facilitar a manutenção do sistema. Cada arquivo abaixo possui comentários detalhados linha por linha explicando sua respectiva lógica:

* **[📥 Inserção de Dados (InserçãoDados.py)](https://www.google.com/search?q=./Pratica/Inser%C3%A7%C3%A3oDados.py)**: Responsável por capturar novos jogos e gravá-los no MySQL de forma dinâmica.
* **[🔍 Consulta Completa (ConsultaCompleta.py)](https://www.google.com/search?q=./Pratica/ConsultaCompleta.py)**: Faz uma busca geral na tabela e exibe todos os jogos cadastrados.
* **[🆔 Consulta Única por ID (ConsultaUnica.py)](https://www.google.com/search?q=./Pratica/ConsultaUnica.py)**: Permite ao sistema filtrar e exibir detalhes de apenas um jogo através do seu identificador único.
* **[✏️ Alteração de Dados (AlterarDados.py)](https://www.google.com/search?q=./Pratica/AlterarDados.py)**: Atualiza de forma cirúrgica o preço de um jogo específico no banco.
* **[🎛️ Menu Principal Interativo (main.py)](https://www.google.com/search?q=./Pratica/main.py)**: Nosso controlador central no terminal. Utiliza um laço `while True`, estruturas de decisão (`if/elif`) e tratamento de erros com `try/except ValueError` para garantir que o usuário navegue por todas as funções acima de forma amigável e segura.

---

## 🖥️ Interface Web com Streamlit

*(Esta seção documenta a evolução do nosso sistema saindo do terminal e indo direto para o navegador!)*

Para colocar a aplicação web para rodar localmente no seu computador, utilize o comando:

```bash
streamlit run Pratica/app.py

```

### Minhas Anotações de Streamlit:

* **`import streamlit as st`**: Biblioteca principal que importamos no topo para gerar os elementos visuais.
* **`st.title()`**: Define o título principal da nossa página web com fontes destacadas.
* **`st.write()`**: Funciona como o nosso `print()`, servindo para exibir textos formatados na tela.



```

```




    
