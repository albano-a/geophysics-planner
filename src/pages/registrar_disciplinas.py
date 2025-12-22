import streamlit as st
import pandas as pd

st.title("Registrar disciplinas")

curriculo = st.selectbox(
    "Currículo",
    [
        "50.01.005",
        # "50.01.004"
    ],
)

df = pd.read_excel(
    "src/data/Disciplinas.xlsx",
    sheet_name=curriculo,
    names=[
        "Nome",
        "Periodo",
        "Prerequisitos",
        "Prende",
        "Descricao",
        "CargaHoraria",
        "PeriodoRecomendado",
    ],
)

CARGA_TOTAL = 3600
CARGA_OBRIGATORIA = 2740
CARGA_OPTATIVA = 816
CARGA_ATIVIDADE = 44

if "checked_disciplinas" not in st.session_state:
    st.session_state.checked_disciplinas = set()

checked = []
carga_cursada = 0

periodos = sorted(df["PeriodoRecomendado"].dropna().unique())
# Agrupa períodos em pares para exibir em duas colunas
for i in range(0, len(periodos), 3):
    cols = st.columns(
        3,
        border=True,
    )
    for j in range(3):
        if i + j < len(periodos):
            periodo = periodos[i + j]
            with cols[j]:
                st.markdown(f"### {int(periodo)}º Período")
                disciplinas_periodo = df[df["PeriodoRecomendado"] == periodo][
                    "Nome"
                ].tolist()
                for disciplina in disciplinas_periodo:
                    checked_box = st.checkbox(
                        disciplina,
                        key=f"{disciplina}_{periodo}",
                        value=disciplina in st.session_state.checked_disciplinas,
                    )
                    if checked_box:
                        checked.append(disciplina)
                        st.session_state.checked_disciplinas.add(disciplina)
                        carga_cursada += float(
                            df[df["Nome"] == disciplina]["CargaHoraria"].values[0]
                        )
                    else:
                        st.session_state.checked_disciplinas.discard(disciplina)

st.divider()

# Optativas - inputs por carga horária
st.header("Optativas", divider="orange")
st.markdown("Informe quantas optativas de cada carga horária você já cursou:")

optativas_60 = st.number_input(
    "60h - Quantas optativas?", min_value=0, step=1, key="opt_60"
)
optativas_72 = st.number_input(
    "72h - Quantas optativas?", min_value=0, step=1, key="opt_72"
)
optativas_30 = st.number_input(
    "30h - Quantas optativas?", min_value=0, step=1, key="opt_30"
)

carga_optativas = optativas_60 * 60 + optativas_72 * 72 + optativas_30 * 30

if carga_optativas > CARGA_OPTATIVA:
    st.error(
        f"Você excedeu a carga horária de optativas ({carga_optativas}h de {CARGA_OPTATIVA}h)."
    )
elif carga_optativas < CARGA_OPTATIVA:
    st.warning(
        f"Faltam {CARGA_OPTATIVA - carga_optativas}h de optativas para completar o mínimo obrigatório."
    )
else:
    st.success("Carga horária de optativas completa!")

# Soma a carga de optativas à carga total cursada
carga_cursada += carga_optativas

st.divider()
atv = []
if st.checkbox("Atividades Complementares"):
    atv.append("Atividades Complementares")
    carga_cursada += CARGA_ATIVIDADE

# Barra de progresso baseada na carga horária
percentual = min(carga_cursada / CARGA_TOTAL, 1.0)
st.progress(percentual)
st.write(f"{carga_cursada:.0f}h de {CARGA_TOTAL}h concluídas ({percentual*100:.1f}%)")
