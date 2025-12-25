import pandas as pd
import streamlit as st

st.title("Informações das Disciplinas")


df = pd.read_excel(
    "src/data/Disciplinas.xlsx",
    sheet_name=["50.01.005", "50.01.004"],
    names=["Nome", "Periodo", "Prerequisitos", "Prende", "Descricao", "CargaHoraria"],
)

curriculo = st.selectbox("Currículo", ["50.01.005", "50.01.004"])


df_curriculo = df[curriculo]

disciplina = st.selectbox("Selecione a disciplina:", df_curriculo["Nome"].unique())
info_disciplina = df_curriculo[df_curriculo["Nome"] == disciplina].iloc[0]

if info_disciplina["Periodo"] == 0:
    periodo = "Todos os Períodos"
elif info_disciplina["Periodo"] == 1:
    periodo = "1º Período"
elif info_disciplina["Periodo"] == 2:
    periodo = "2º Período"

st.subheader(
    f"{disciplina}",
    help=(
        None
        if not disciplina.startswith("P.C.")
        else "P.C. indica que é uma Prática de Campo"
    ),
)
st.markdown("**Período**", help="Período em que a disciplina é ofertada.")
st.markdown(f"{periodo}")
st.markdown(
    "**Carga Horária**",
    help="Total de horas dedicadas à disciplina.",
)
st.markdown(f"{info_disciplina['CargaHoraria']} horas")
st.markdown(
    "**Pré-requisitos**",
    help="Disciplinas que devem ser cursadas antes desta disciplina.",
)
st.markdown(info_disciplina["Prerequisitos"])
st.markdown(
    "**Pós-requisitos**",
    help="Disciplinas que dependem desta disciplina como pré-requisito.",
)
st.markdown(f"{info_disciplina['Prende']}")
st.markdown(
    f"""**Descrição**  
    {info_disciplina['Descricao'] if pd.notna(info_disciplina['Descricao']) else 'Descrição não disponível.'}""",
)
st.markdown("---")
st.markdown(
    "Para mais informações sobre as disciplinas, consulte o site oficial da instituição ou a matriz curricular do curso."
)
