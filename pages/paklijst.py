import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
from lib.utils import change_button_height 
from streamlit_navigation_bar import st_navbar
import os

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
if "current_page" not in st.session_state:
    st.session_state['current_page'] = 'PAKLIJST'

elif "current_page" in st.session_state:
    st.session_state['current_page'] = 'PAKLIJST'

if "authenticated" not in st.session_state:
    switch_page('authenticator')
 
georgia_red = "#FF0000" 
georgia_white = "#FFFFFF"
georgia_grey = "#424242"

pages = ["HOME", "DEELNEMERS", "PAKLIJST", "ROUTE", "AGENDA", "INSPIRATIE"]
parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = './files/logo.svg'

styles = {
    "nav": {
        "background-color": georgia_grey,
        "justify-content": "middle",
    },
    "img": {    
        "text-align": "left",
    },
    "span": {
        "color": "white",
        "padding": "10px",
    },
    "active": {
        "background-color": georgia_grey,
        "color": georgia_red,
        "font-weight": "normal",
        "padding": "10px",
    }
}
options = {
    "show_menu": False,
    "show_sidebar": False,
}

page = st_navbar(
    pages,
    logo_path=logo_path,
    styles=styles,
    options=options,
)

if page == "HOME" and st.session_state['current_page'] != 'HOME':
    switch_page("HOME")

if page == "DEELNEMERS" and st.session_state['current_page'] != 'DEELNEMERS':
    switch_page("DEELNEMERS")

if page == "PAKLIJST" and st.session_state['current_page'] != 'PAKLIJST':
    switch_page("PAKLIJST")

if page == "ROUTE" and st.session_state['current_page'] != 'ROUTE':
    switch_page("ROUTE")

if page == "AGENDA" and st.session_state['current_page'] != 'AGENDA':
    switch_page("AGENDA")

if page == "INSPIRATIE" and st.session_state['current_page'] != 'INSPIRATIE':
    switch_page("INSPIRATIE")

col1, col2, col3 = st.columns([1,4,1])
list_of_paklijst = []
paklijst_ingeleverd = ''

with col2:
    with st.container(border=True):
        st.write('Dit moet je meenemen')
    
    with st.container(border=True):
        onderbroeken = st.checkbox('Onderbroeken')
        list_of_paklijst.append(onderbroeken)    

        tandenborstel = st.checkbox('Tandenborstel')
        list_of_paklijst.append(tandenborstel) 

        zwembroek = st.checkbox('Zwembroek')
        list_of_paklijst.append(zwembroek) 

        rietjes = st.checkbox('Rietjes')
        list_of_paklijst.append(rietjes) 

        kogel = st.checkbox('Kogelvrijvest')
        list_of_paklijst.append(kogel) 

        das = st.checkbox('Das')
        list_of_paklijst.append(das) 
    
        poetin = st.checkbox('Foto van Poetin')
        list_of_paklijst.append(poetin) 

        wandel = st.checkbox('Wandelschoenen')
        list_of_paklijst.append(wandel) 


        # rietjes = st.checkbox('Rietjes')
        # list_of_paklijst.append(rietjes) 

        # rietjes = st.checkbox('Rietjes')
        # list_of_paklijst.append(rietjes) 

        # rietjes = st.checkbox('Rietjes')
        # list_of_paklijst.append(rietjes) 

    alles_ingepakt = True
    for item in list_of_paklijst:
        if not item:
            alles_ingepakt = False

    if alles_ingepakt:
        paklijst_ingeleverd = st.button('Ik wil mijn paklijst graag inleveren', use_container_width=True)

    if paklijst_ingeleverd:
        with st.container(border=True):
            st.write("Grote klasse")