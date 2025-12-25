import streamlit as st

st.set_page_config(
    page_title="GeofisicaPlanner",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="auto",
)

pages = {
    "Home": [st.Page("pages/home.py", title="Página Inicial", icon="🏠")],
    "Recursos": [
        st.Page(
            "pages/registrar_disciplinas.py",
            title="Registrar disciplinas cursadas",
            icon="📝",
        ),
        st.Page(
            "pages/informacoes_disciplinas.py",
            title="Informações das Disciplinas",
            icon="📚",
        ),
        st.Page("pages/curriculos.py", title="Ver currículos", icon="📄"),
        st.Page("pages/optativas.py", title="Disciplinas Optativas", icon="🎓"),
    ],
}

pg = st.navigation(pages, position="top")
pg.run()
