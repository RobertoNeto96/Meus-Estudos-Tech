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
* ✏️ **[Campo pratico de StreamLit (app.py)](./Pratica/app.py)** - Arquivo pratico das aplicações do curso

# 🎈 Minhas Anotações de Streamlit (`st`)


### 📝 Exibindo Textos (Os substitutos do `print`)

*   **`st.write()`** ➔ O canivete suíço do Streamlit. Faz o papel do `print()`, mas exibe textos, tabelas, gráficos e até fórmulas formatadas na tela.
*   **`st.title()`** ➔ Cria o título principal da página com fontes destacadas e tamanho grande.
*   **`st.subheader()`** ➔ Cria subtítulos menores para organizar as seções da tela.

### 📥 Entradas de Dados (Os substitutos do `input`)

*   **`st.text_input()`** ➔ Caixa de texto simples. É o substituto direto do `input()` do Python (ideal para capturar strings, como o nome de um jogo).
*   **`st.number_input()`** ➔ Caixa para o usuário digitar ou selecionar números. Permite definir valores mínimos, máximos e casas decimais (perfeito para preços ou durações).

### 🔘 Ações e Botões

*   **`st.button()`** ➔ Cria um botão clicável na tela. Ele retorna um valor booleano (`True`) no momento exato em que é clicado, servindo de gatilho para executar blocos de código Python.

### 📊 Exibição de Tabelas e Dados

*   **`st.dataframe()`** ➔ Exibe tabelas inteiras vindas do banco de dados de forma bonita e interativa, permitindo que o usuário ordene as colunas diretamente no navegador.

---

## ⚡ Atalho de Produtividade: Modo "Always Rerun"

Para não precisar reiniciar o terminal a cada modificação no código:
1. Deixe o terminal rodando com o comando `streamlit run app.py`.
2. Altere o código no VS Code e salve o arquivo (`Ctrl + S`).
3. Na página do navegador, clique na opção **"Always rerun"** que aparecerá no canto superior direito. 
4. A partir disso, a tela se atualizará sozinha a cada novo salvamento!