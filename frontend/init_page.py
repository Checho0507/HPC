import random
import threading
import streamlit as st

from backend.db import add_user, validate_user
from backend.security import init_sessions, register_user, sign_in

def init(e):
    # Configuración de la página
    st.set_page_config(page_title="Portal de Vinos", page_icon="🍇", layout="centered")

    # Título y descripción inicial
    st.title("Bienvenido al Portal de Vinos 🍇")
    st.write("Por favor, elige una opción para continuar.")
    
    init_sessions()

    # Formulario de registro
    email = st.text_input("Correo Electrónico:")
    security = st.empty()  # Campo vacío para mostrar el input de la clave después

    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("Iniciar Sesión"):
            e = sign_in(email)

    with col2:
        if st.button("Registrarse"):
            e = register_user(email)

    # Mostrar el campo de texto para la clave de seguridad después del primer clic
    if st.session_state["login_step"] == 1:
        st.session_state["key"] = security.text_input("Llave de Seguridad:", type="password")

    # Mensajes de error o éxito
    if e == 1:
        st.error("Por favor, ingrese un correo electrónico.")
    elif e == 2:
        st.error("El correo ya está registrado. Intenta con otro.")
    elif e == 3:
        st.error(f"Error al registrar usuario: {e}")
    elif e == 4: 
        st.success(f"Usuario registrado con éxito. La llave se enviará a: {email}")
        st.info("Revisa tu correo para obtener más información.")
    elif e == 5:
        st.error("Por favor, ingresa tu llave de seguridad.")
    elif e == 6:
        st.error("Credenciales incorrectas. Verifica tu correo y llave de seguridad.")
    elif e == 7:
        st.success("Inicio de sesión exitoso. ¡Bienvenido!")