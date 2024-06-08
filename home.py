import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
from lib.utils import change_button_height 
from streamlit_navigation_bar import st_navbar
import os
import pandas as pd
import random

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'HOME'

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

col1, col2, col3 = st.columns([1,6,1])

with col2:
    with st.container(border=True):
        st.markdown(f"<p style='text-align: center; color: {georgia_grey};'>KHANDAZI</h1>", unsafe_allow_html=True)

    cola, colb = st.columns([1,1])
    
    with cola:
        with st.container(border=True):
            st.dataframe(pd.read_excel('./files/facts.xlsx'))
            
    with colb:
        with st.container(border=True):
            st.image('./files/georgia.png')

    with st.container(border=True):
        list_of_fun_fact = ['Georgië wordt ook wel het balkon van Europa genoemd', 'Tbilisi wordt ook wel het Nice van de Kaukasus genoemd', 'Jozef Stalin is geboren in Georgië', 'De laatste oorlog in Georgië was 16 jaar geleden']
        list_of_fun_fact = ['Georgië wordt ook wel het balkon van Europa genoemd', 'Tbilisi wordt ook wel het Nice van de Kaukasus genoemd', 'Jozef Stalin is geboren in Georgië', 'De laatste oorlog in Georgië was 16 jaar geleden', 'Het gerucht gaat dat wijn is uitgevonden in Georgië', 'Hét symbool van Georgië is het Gergeti klooster (included in het programma)']  
        
        fun_fact = random.choice(list_of_fun_fact)
        st.write(f"{fun_fact}")

    with st.container(border=True):
        st.write(
            """
            Georgië is een land dat ligt op het kruispunt van Oost-Europa en West-Azië, begrensd door Rusland in het noorden, Turkije en Armenië in het zuiden, Azerbeidzjan in het zuidoosten en de Zwarte Zee in het westen. Het heeft een divers landschap met bergen, valleien en een kustlijn langs de Zwarte Zee. Het klimaat varieert van subtropisch aan de kust tot continentaal in het binnenland, met alpiene omstandigheden in de Grote Kaukasus-bergketen. \n
            Historisch gezien was Georgië de thuisbasis van de oude koninkrijken Colchis en Iberia. Het land nam in het begin van de 4e eeuw het christendom aan, waardoor het een van de oudste christelijke naties ter wereld is. Tijdens de middeleeuwen beleefde het land een Gouden Eeuw onder het bewind van koning David IV en koningin Tamar in de 12e en 13e eeuw. Georgië werd in de 19e eeuw ingelijfd bij het Russische Rijk en maakte later van 1921 tot 1991 deel uit van de Sovjet-Unie, totdat het in 1991 onafhankelijk werd. \n
            De officiële taal van Georgië is Georgisch, dat een uniek schrift heeft. Het land staat bekend om zijn keuken, met gerechten zoals khachapuri, een met kaas gevuld brood, en khinkali, dumplings. Georgië heeft ook rijke tradities in polyfone zang en volksdansen. \n
            Georgië is een semi-presidentiële republiek. Het land verwierf in 1991 onafhankelijkheid van de Sovjet-Unie, maar kende in de jaren negentig en het begin van de jaren 2000 burgerlijke onrust en conflicten, waaronder de Russisch-Georgische oorlog in 2008 over de gebieden Zuid-Ossetië en Abchazië. Deze regio's riepen de onafhankelijkheid uit, maar worden door de meeste landen erkend als onderdeel van Georgië. \n
            Economisch gezien is Georgië afhankelijk van landbouw, wijnproductie, toerisme en mijnbouw. Het land trekt toeristen met zijn historische locaties, diverse landschappen en culturele erfgoed. Georgië streeft naar lidmaatschap van de Europese Unie en de NAVO, maar de betrekkingen met Rusland zijn gespannen, vooral vanwege de conflicten over Zuid-Ossetië en Abchazië. \n
            Tbilisi, de hoofdstad en grootste stad, staat bekend om zijn diverse architectuur en levendige cultuur. Batumi is een belangrijke badplaats aan de Zwarte Zee en Koetaisi is een belangrijk cultureel en historisch centrum. Georgië is een van de oudste wijnproducerende regio's ter wereld, met een geschiedenis van wijnproductie die 8.000 jaar teruggaat. Het land is de thuisbasis van verschillende UNESCO-werelderfgoedlocaties, waaronder de Historische Monumenten van Mtskheta en de Bagrati-kathedraal. \n
            De rijke geschiedenis, het culturele erfgoed en de strategische ligging van Georgië maken het tot een uniek en fascinerend land op het kruispunt van Europa en Azië.
            """
        )