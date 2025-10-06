import pandas as pd
import streamlit as st

st.title('Catálogo de Filmes')

upload = st.file_uploader('Carregar arquivo CSV', type='csv')

if upload:
    df = pd.read_csv(upload)
    st.subheader('Dados carregados:')
    st.dataframe(df)

    st.subheader('Estatísticas descritivas:')
    st.write(df.describe())

    st.subheader('Média de avaliação por categoria:')
    media_categoria = df.groupby('Categoria')['Avaliação'].mean().reset_index()
    st.dataframe(media_categoria)

    st.subheader('Gráfico: Média de avaliação por categoria')
    st.bar_chart(media_categoria.set_index('Categoria')['Avaliação'])

    st.subheader('Quantidade de filmes por ano:')
    filmes_ano = df['Ano'].value_counts().sort_index()
    st.bar_chart(filmes_ano)