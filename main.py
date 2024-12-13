import streamlit as st

from backend.db import init_db
from frontend.init_page import init

if "page" not in st.session_state:
    st.session_state["page"] = "init"
    #Inicializar base de datos
    init_db()
    
if st.session_state["page"] == "init":
    init(0)