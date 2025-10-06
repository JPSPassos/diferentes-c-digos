import pandas as pd
import streamlit as st

st.title('Site simples')

upload = st.file_uploader('Carregar arquivo CSV', type='csv')

if upload:
    df = pd.read_csv(upload)
    st.subheader('Dados carregados:')
    st.dataframe(df)

    st.subheader('Estatísticas descritivas:')
    st.write(df.describe())

    df['Total'] = df['Preço'] * df['Quantidade']
    st.subheader('Total de vendas por produto:')
    st.dataframe(df[['Produto', 'Total']])

    st.subheader('Gráfico de vendas por produto:')
    st.bar_chart(df.set_index('Produto')['Total'])