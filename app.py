from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Laboratory Cooling | State Machine Workshop", page_icon="❄️", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>
#MainMenu,footer,header {visibility:hidden} .block-container {padding:0!important;max-width:100%!important}
[data-testid="stAppViewContainer"] {background:#f4f8fc}
iframe[title="streamlit.components.v1.html"] {display:block}
</style>""", unsafe_allow_html=True)
html = (Path(__file__).parent / "workshop.html").read_text(encoding="utf-8")
components.html(html, height=1500, scrolling=True)
