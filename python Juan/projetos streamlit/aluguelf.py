import datetime as dt
from datetime import timedelta as td
import streamlit as st

st.title('Empréstimo de Livros')

livros_lista = ['O Alquimista', 'Dom Casmurro', '1984', 'O Pequeno Príncipe', 'A Revolução dos Bichos']
livro_escolhido = st.selectbox('Escolha um livro para alugar:', livros_lista)

hoje = dt.date.today()
devolucao = hoje + td(days=7)

data_str = st.text_input('Digite a data de hoje (dd/mm/aaaa): ')

if data_str.strip():
    try:
        data_devolvida = dt.datetime.strptime(data_str, '%d/%m/%Y').date()

        if data_devolvida < devolucao:
            st.write('Falta(m) {} dia(s) para a devolução do livro'.format((devolucao - data_devolvida).days))
        elif data_devolvida > devolucao:
            st.write('O livro está atrasado por {} dia(s)'.format((data_devolvida - devolucao).days))
        else:
            st.write('O livro deve ser devolvido hoje!')

        informacao_produto = {
            'nome': livro_escolhido,
            'data_retirada': data_str,
            'data_devolucao': devolucao.strftime('%d/%m/%Y')
        }

        botao_aluguel = st.button('Alugar Livro')
        if botao_aluguel:
            st.write('Você alugou o livro "{}".'.format(informacao_produto['nome']))
            st.write('Data de retirada: {}'.format(informacao_produto['data_retirada']))
            st.write('Data de devolução: {}'.format(informacao_produto['data_devolucao']))

    except ValueError:
        st.error("Data inválida! Use o formato DD/MM/AAAA.")
else:
    st.warning("Por favor, insira a data no formato DD/MM/AAAA.")
