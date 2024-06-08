import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
from lib.utils import change_button_height 
from streamlit_navigation_bar import st_navbar
import os

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

col1, col2, col3 = st.columns([1,1,1])

with col2:
    password = st.text_input('', type='password')
    password_button = st.button('IK WIL NAAR GEORGIE', use_container_width=True)

    if password_button and password.lower() == 'vlammen':
        if "authenticated" not in st.session_state:
            st.session_state['authenticated'] = True
            switch_page('HOME')