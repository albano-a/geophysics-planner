import streamlit as st
import pandas as pd


st.title("Disciplinas Optativas")

st.info(
    "Página em construção. Em breve, você poderá registrar suas disciplinas optativas cursadas aqui!",
    icon="🚧",
)

st.header("Lista de Disciplinas Optativas")

st.write(
    """
    Algumas disciplinas optativas estão listadas aqui apenas por registro histórico.
    Elas podem não estar mais sendo ofertadas, já que, quando abertas, não tiveram procura.
    Portanto, não considere que todas as disciplinas listadas ainda existam ou sejam ofertadas atualmente.
    """
)

data = [
    ["GAG00047", "Processamento Digital de Imagens", 60, ["GAG00069"]],
    ["GBG00060", "Biomodelagem", 40, ["TCC00325"]],
    ["GEO00006", "Micropaleontologia Marinha", 30, ["GGO00014"]],
    ["GGE00026", "Variabilidade Climática", 60, ["GGO00013"]],
    ["GGE00186", "Geografia das Regiões Polares", 60, ["GGO00012"]],
    ["GGE00202", "Geopolítica do Clima", 60, []],
    ["GGO00001", "Geofísica Aplicada à Engenharia Submarina", 72, ["GGO00088"]],
    ["GGO00033", "Geofísica Nuclear", 72, ["GGO00023"]],
    ["GGO00035", "Geotermia", 72, ["GGO00016"]],
    ["GGO00045", "Análise de Bacias", 72, ["GGO00016", "GGO00078"]],
    ["GGO00048", "Geologia do Petróleo", 72, ["GGO00016", "GGO00078"]],
    ["GGO00051", "Hidrogeologia", 72, ["GGO00013"]],
    ["GGO00052", "Neotectônica (Desativada)", 72, ["GGO00016"]],
    ["GGO00054", "Sedimentação Marinha", 72, ["GGO00021", "GGO00014"]],
    ["GGO00056", "Geofísica Aplicada à Prospecção Mineral (Desativada)", 72, []],
    ["GGO00058", "Perfilagem Geofísica de Poço", 72, ["GGO00078"]],
    ["GGO00059", "Petrofísica", 72, ["GGO00015"]],
    ["GGO00060", "Processamento Sísmico", 72, ["GGO00088"]],
    ["GGO00062", "Avaliação de Impacto Ambiental (Desativada)", 72, ["GGO00014"]],
    ["GGO00074", "Aquisição Sísmica", 72, ["GGO00088"]],
    ["GGO00075", "Estratigrafia de Sequências (Desativada)", 72, ["GGO00078"]],
    ["GGO00076", "Interpretação Sísmica 3D", 72, ["GGO00078"]],
    ["GGO00082", "Geofísica do Petróleo", 72, ["GGO00023"]],
    [
        "GGO00083",
        "Geologia e Geofísica Aplicada a Problemas Ambientais",
        72,
        ["GGO00014"],
    ],
    ["GGO00087", "Poluição Ambiental", 72, ["GGO00014"]],
    ["GGO00104", "Prática de Campo – Aquisição Sísmica Multicanal", 72, ["GGO00037"]],
    ["GGO00105", "Caracterização de Reservatório", 60, ["GGO00086"]],
    ["GGO00108", "Prospecção de Recursos Minerais", 72, ["GGO00023", "GGO00015"]],
    [
        "GGO00109",
        "Recursos Petrolíferos Não Convencionais (Desativada)",
        72,
        ["GGO00048"],
    ],
    ["GGO00110", "Fundamentos de Tomografia Sísmica", 72, ["GGO00086"]],
    [
        "GGO00112",
        "Análise de Projetos de Caracterização e Simulação de Reservatórios",
        72,
        ["GGO00088"],
    ],
    ["GGO00113", "Análise de Projetos Exploratórios de Petróleo", 72, ["GGO00078"]],
    ["GGO00114", "Linguagem Python Aplicada à Geofísica", 72, ["GGO00124"]],
    [
        "GGO00116",
        "Inversão Não Linear Aplicada a Dados Geofísicos (Desativada)",
        72,
        ["GGO00086"],
    ],
    ["GGO00118", "Interpretação Exploratória", 72, ["GGO00078", "GGO00088"]],
    ["GGO00120", "Atributos Sísmicos e Classificação de Sismofácies", 60, ["GGO00028"]],
    ["GGO00121", "Introdução ao Método Magnetotelúrico (Desativada)", 72, ["GFI00159"]],
    ["GGO00122", "Empreendedorismo e Inovação em Geociências", 60, ["GGO00100"]],
    ["GGO00123", "Integração de Métodos Geofísicos", 60, ["GGO00077", "GGO00088"]],
    ["GGO00125", "Operações Geológicas e Geofísicas de Poços", 60, ["GGO00078"]],
    ["GGO00129", "Aprendizado de Máquina em Geociências", 60, ["GET00116", "GGO00086"]],
    ["GGO00130", "Métodos Sísmicos", 60, ["GGO00088"]],
    [
        "GGO00133",
        "Técnicas e Habilidades de Comunicação Científica e Profissional",
        60,
        [],
    ],
    ["GLC00292", "LIBRAS I", 30, []],
    ["TCC00307", "Programação Científica", 64, []],
]

st.markdown(
    """Algumas optativas podem ter pré-requisitos. Consulte quais acessando o 
    [quadro de horários](https://app.uff.br/graduacao/quadrodehorarios/) da UFF, e 
    colando o código da disciplina na busca.
    """
)

df = pd.DataFrame(data, columns=["codigo", "nome", "ch_total", "pre_requisitos"])

st.dataframe(
    df,
    hide_index=True,
    placeholder="Carregando lista de disciplinas optativas...",
    height=600,
)
