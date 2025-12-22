import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as cmp

st.set_page_config(
    page_title="Disciplinas | GeofisicaPlanner",
    page_icon="🎈",
    layout="centered",
    initial_sidebar_state="auto",
)


st.title("Disciplinas")


cur = st.selectbox("Currículo", ["50.01.005", "50.01.004"], index=0)

pth = Path(f"src/data/{cur}.pdf")
pdf = pth.read_bytes()
b64 = base64.b64encode(pdf).decode()

cmp.html(
    f"""
    <iframe
        src="data:application/pdf;base64,{b64}"
        width="100%"
        height="800"
        style="border:none;"
    ></iframe>
    """,
    height=800,
)

st.download_button(
    "Download PDF", data=pdf, file_name=f"{cur}.pdf", mime="application/pdf"
)
