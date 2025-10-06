import streamlit as st

st.set_page_config(
    page_title="App teste de streamlit",
    page_icon="😎",
    layout="wide"
)

# Inicializa o estado dos botões
if "show_nada" not in st.session_state:
    st.session_state.show_nada = False
if "show_tudo" not in st.session_state:
    st.session_state.show_tudo = False

# Banner com fonte maior
st.markdown(
    """
    <style>
    .custom-title {
        font-size: 60px;
        font-weight: bold;
        color: white;
        text-align: center;
        margin-bottom: 0;
    }
    .stButton button {
        font-size: 32px !important;
        height: 70px !important;
    }
    .big-success {
        font-size: 32px !important;
        font-weight: bold;
    }
    .big-error {
        font-size: 32px !important;
        font-weight: bold;
    }
    .footer {
        font-size: 22px;
    }
    </style>
    <div style="background-color:#4B8BBE;padding:20px;border-radius:10px">
        <h1 class="custom-title">O que sobra para o betinha? 🤔</h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")  # Espaço

# Colunas para os botões
col1, col2 = st.columns(2)

with col1:
    if st.button("NADA 💀", use_container_width=True, key="btn_nada"):
        st.session_state.show_nada = not st.session_state.show_nada
    if st.session_state.show_nada:
        st.markdown('<div class="big-success">NADA SOBRA AOS BETAS 😢</div>', unsafe_allow_html=True)
        st.image('C:\\Users\\Aluno Manhã\\Pictures\\tadinho-de-betinha-v0-7kcha4nu7shf1.webp', width=600)        

with col2:
    if st.button("TUDO 🤑", use_container_width=True, key="btn_tudo"):
        st.session_state.show_tudo = not st.session_state.show_tudo
    if st.session_state.show_tudo:
        st.markdown('<div class="big-error">NUNCA NADA SOBRARÁ AOS BETAS 🚫</div>', unsafe_allow_html=True)
        st.image(
            "C:\\Users\\Aluno Manhã\\Pictures\\oque-oque-sobra-pro-betinha-v0-73vxnx9t5acf1.webp",
            width=600
        )

# Rodapé
st.markdown(
    """
    <hr>
    <p class="footer" style="text-align:center;color:gray;">
        Feito com Streamlit | <a href="https://streamlit.io" target="_blank">Saiba mais</a>
    </p>
    """,
    unsafe_allow_html=True
)
