import streamlit as st
import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

PERIODO = "20252"

st.title("GeofisicaPlanner")

st.markdown(
    """
    Bem-vindo ao GeofisicaPlanner! Esta aplicação foi desenvolvida para ajudar estudantes de Geofísica a planejar suas disciplinas acadêmicas de forma eficiente.
    ### Funcionalidades:
    - **Registrar Disciplinas Cursadas**: Mantenha um registro das disciplinas que você já completou.
    - **Informações das Disciplinas**: Acesse detalhes sobre cada disciplina,
        incluindo pré-requisitos, carga horária e descrições.
    - **Ver Currículos**: Consulte os currículos disponíveis para o curso de Geofísica.
    """
)

st.subheader("Informações Nerds Extras")

cols = st.columns(3, border=True)
with cols[0]:
    with st.spinner("Carregando CR médio..."):
        url = "https://app.uff.br/transparencia/cr_medio_por_curso"
        res = requests.get(url)
        if res.status_code != 200:
            st.error(f"Erro ao acessar {res.status_code}")
        else:
            tbls = pd.read_html(res.text)
            df = tbls[0]
            crs = "Geofísica"
            df_flt = df[df.iloc[:, 1].str.contains(crs, case=False, na=False)]
            if df_flt.empty:
                st.write("Curso não encontrado")
            else:
                cr = df_flt.iloc[0, 2]
                st.metric(f"CR médio de Geofísica", f"{cr}")
with cols[1]:
    with st.spinner("Carregando reprovações..."):
        url = f"https://app.uff.br/transparencia/disciplinas_que_mais_reprovam?curso=50&periodo={PERIODO}"
        res = requests.get(url)
        if res.status_code != 200:
            st.error(f"Falha ao acessar: {res.status_code}")
        else:
            soup = BeautifulSoup(res.text, "html.parser")
            tbl = soup.find("table", id="table_disciplinas")
            df = pd.read_html(str(tbl))[0]
            cod = df.iloc[0, 0]
            nm = df.iloc[0, 1].title()
            rep = df.iloc[0, 2]
            periodo_formatado = f"{PERIODO[:4]}.{PERIODO[4]}"
            st.metric(
                f"Mais reprovações ({periodo_formatado})",
                f"{nm}",
                f"{rep} reprovações",
                help=f"{nm} é a disciplina com mais reprovações.",
                delta_color="inverse",
            )
with cols[2]:
    with st.spinner("Carregando total de alunos..."):
        url = "https://app.uff.br/transparencia/perfil_graduando?curso=50"
        res = requests.get(url)
        if res.status_code != 200:
            st.error(f"Erro ao acessar o total de alunos: {res.status_code}")
        else:
            soup = BeautifulSoup(res.text, "html.parser")
            tot = soup.find("tfoot").find("td", class_="center").get_text(strip=True)
            st.metric(
                label="Total de Alunos Inscritos",
                value=tot,
                help="Número total de alunos inscritos. Não reflete o número de alunos ativos.",
            )

with st.spinner("Carregando dados de formandos..."):
    df_formandos = pd.read_csv("src/data/formandos_por_professor.csv")
    # Remove a última coluna se ela se chama "Total"
    if "Total" in df_formandos.columns:
        df_formandos = df_formandos.drop(columns=["Total"])
    # Cada coluna é um ano, eu quero um gráfico com cada ano e a quantidade total de formandos (soma da coluna)
    df_formandos_totais = df_formandos.set_index("Orientador").sum().reset_index()
    df_formandos_totais.columns = ["Ano", "Total de Formandos"]
    total_formandos = df_formandos_totais["Total de Formandos"].sum()
    st.subheader(
        "Formandos por Ano", help="Dados podem estar incompletos para anos recentes."
    )
    st.metric(
        "Total de Formandos",
        total_formandos,
        help="Soma total de formandos registrados no período.",
        border=True,
    )
    st.bar_chart(df_formandos_totais, x="Ano", y="Total de Formandos", color="#1077bc")
st.markdown(
    """
    ---
    Desenvolvido por André Albano.  
    Dados obtidos do Portal de Transparência da UFF e do site da Geofísica UFF.
    """
)
