import streamlit as st

st.set_page_config(
    page_title = "Meu App de Estudo",
    page_icon = "📚",
    layout = "wide"
)

st.markdown(
    """
    <style>
    body {
        background-color: #f6f8fa;
    }
    .main {
        background-color: #f6f8fa;
    }
    .stButton>button {
        background-color: #4caf50;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 8px 16px;
    }
    .stMetric {
        background-color: #e3f2fd;
        border-radius: 8px;
        padding: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📚 Meu App de Estudo")
st.subheader("✨ Organize seus estudos de forma eficiente")

with st.expander("💡 Dicas de Estudo"):
    st.markdown("""
    - ⏰ Estude em blocos de 25 a 50 minutos e faça pequenas pausas.
    - 🔄 Revise o conteúdo regularmente para fixar melhor.
    - 📝 Pratique exercícios para testar seu conhecimento.
    - 📅 Organize um cronograma de estudos.
    - 🚫 Mantenha o ambiente livre de distrações.
    """)

st.markdown("---")

with st.sidebar:
    st.header("🎯 Registro Diário")
    horas = st.slider("Quantas horas estudou hoje?", min_value=0, max_value=12, step=1)
    pausas = st.slider("Quantas pausas fez?", min_value=0, max_value=10, step=1)
    atividade = st.selectbox("Tipo de estudo realizado:", ["Literatura", "Exercícios", "Revisão"])
    col_reg, col_limpar = st.columns(2)
    with col_reg:
        registrar = st.button("Registrar")
    with col_limpar:
        limpar = st.button("Limpar")
    mostrar_info = st.toggle("Mostrar informações do registro", value=True)

if registrar:
    st.session_state["horas"] = horas
    st.session_state["pausas"] = pausas
    st.session_state["atividade"] = atividade
    st.session_state["registrado"] = True

if limpar:
    for key in ["horas", "pausas", "atividade", "registrado"]:
        if key in st.session_state:
            del st.session_state[key]
    st.success("Registros limpos com sucesso!")

if st.session_state.get("registrado") and mostrar_info:
    horas = st.session_state["horas"]
    pausas = st.session_state["pausas"]
    atividade = st.session_state["atividade"]

    with st.container():
        st.header("Área de Registro")
        st.markdown("## 📊 Métricas do seu estudo de hoje:")
        st.metric("Horas estudadas", f"{horas} ⏳")
        st.metric("Pausas realizadas", f"{pausas} 💤")
        st.metric("Tipo de atividade", f"{atividade} 📖" if atividade == "Literatura" else ("Exercícios📝" if atividade == "Exercícios" else "Revisão🔄"))

        st.markdown("---")

        col1, col2, col3 = st.columns(3)

        with col1:
            if horas >= 4:
                st.success("✅ Tempo de estudo excelente!")
            elif horas >= 2:
                st.info("🟡 Tempo de estudo bom. Mas pode melhorar!")
            elif horas < 2 and horas > 0:
                st.warning("⚠️ Poucas horas de estudo. Tente aumentar!")
            elif horas == 0:
                st.warning("⚠️ Nenhum estudo registrado. Vamos começar a estudar!")

        with col2:
            pausas_necessarias = horas // 2
            if pausas >= pausas_necessarias and pausas_necessarias > 0:
                st.success("🛌 Pausas adequadas para o tempo de estudo!")
            elif pausas < pausas_necessarias and pausas_necessarias > 0:
                st.warning(f"⚠️ Você estudou {horas} horas. Recomenda-se pelo menos {pausas_necessarias} pausa(s)!")
            elif pausas == 0 and horas == 0:
                st.warning("⚠️ Nenhum estudo registrado.")
            else:
                st.info("💤 Pausas registradas.")

        with col3:
            if atividade == "Literatura" and horas > 0:
                st.success("📖 Você está lendo. Ótimo para absorver conteúdo!")
            elif atividade == "Exercícios" and horas > 0:
                st.success("📝 Praticando exercícios! Excelente para fixar.")
            elif atividade == "Revisão" and horas > 0:
                st.success("🔄 Revisando. Importante para consolidar o conhecimento!")
            elif atividade and horas == 0:
                st.warning("⚠️ Nenhum estudo registrado. Vamos começar a estudar!")


st.markdown(
    """
    <hr style="border:1px solid #bbb;">
    <div style='text-align: center; color: gray; font-size: 14px;'>
        © 2025 Meu App de Estudo | Desenvolvido por Aluno Manhã
    </div>
    """,
    unsafe_allow_html=True
)