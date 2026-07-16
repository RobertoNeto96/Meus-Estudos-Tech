# Para começarmos importamos a biblioteca do STREAMLIT e apelidamos de ST para que os codigos fiquem mais legiveis e um codigo mais organizado

import streamlit as st

# Após importarmos o StreamLit temos entao a biblioteca com varias funções, ondem chamamos a partir do .(ponto) como por exemplo st.write que é semelhante ao PRINT em python, ele retorna informação na tela para o usuario, ao decorrer veremos outras funçôes do streamLit

"""
🧠 Guia de Consulta Rápida: 
Streamlit (st)📝 Exibindo Textos (Os substitutos do print)

st.write() --> O canivete suíço. Faz o papel do print(), mas exibe textos, tabelas, gráficos e até fórmulas formatadas na tela.

st.title() --> Cria o título principal da página (com uma fonte bem grandona e destaque).

st.subheader() --> Cria subtítulos menores para organizar as seções da sua tela.📥 Entradas de Dados (Os substitutos do input)

st.text_input() --> Caixa de texto simples. É o substituto direto do input() do Python (ótimo para digitar nomes de jogos).

st.number_input() --> Caixa para o usuário digitar números. Você consegue definir valor mínimo, máximo e casas decimais (perfeito para o preço do jogo!).

🔘 Ações e Botões

st.button() --> Cria um botão clicável na tela. Ele retorna True (verdadeiro) quando é clicado, o que aciona o seu código Python.

📊 Tabelas (O pesadelo do terminal que virou sonho)

st.dataframe() --> Exibe tabelas inteiras do seu banco de dados de um jeito lindo, interativo, onde você consegue ordenar as colunas clicando nelas. """