import streamlit as st

st.set_page_config(
    page_title='Projeto de estilização streamlit',
    page_icon="",
    layout="wide"
)
st.title('Projeto estilização streamlit')
st.subheader("Exemplo de Como organizar e estilizar um app")

st.sidebar.header('Filtros')
st.sidebar.checkbox('Ativar Tema escuro')
st.sidebar.slider('Selecionar valor', 0, 100, 25)

st.metric('Vendas', 'R$50.000', '+5%')
st.metric("Usuários", "1.200", '-2%')

col1, col2, col3 = st.columns(3)

with col1:
    st.header('Coluna 1')
    st.button('CLICA AI BETINHA')
    st.success('BETA DO CARALHO')

with col2:
    st.header('Coluna 2')
    st.warning('atenção')
    st.radio('Escolha opções', ['Opção A', "Opção B", 'Opção C'])

with col3:
    st.header('Coluna 3')
    st.info('atenção')
    st.selectbox('Escolha um item', ['Item 1', "Item 2", 'Item 3'])

    with st.expander('Clique para ver detalhes'):
        st.write('Detalhes ocultos')
        st.checkbox('Marcar como lido')
        st.text_input('Digite algo legal')

    st.markdown(
        """
        <div style='background-color: #f9f9f9; padding: 10px; border-radius: 10px'>
        <h4 style='color: #F57333;'>Texto colorido com estilo personalizado</h4>
        </div>
        """,
        unsafe_allow_html=True
    )

# Rodapé
st.markdown("---")
st.markdown("🔅 Exemplo simples de estilização no Streamlit sem lógica complexa")
st.markdown("🔅 Exemplo simples de estilização no Streamlit sem lógica complexa")