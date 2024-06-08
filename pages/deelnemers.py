import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
from lib.utils import change_button_height 
from streamlit_navigation_bar import st_navbar
import os
import random

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
if "current_page" not in st.session_state:
    st.session_state['current_page'] = 'DEELNEMERS'

elif "current_page" in st.session_state:
    st.session_state['current_page'] = 'DEELNEMERS'

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
    col1, col2= st.columns([1,4])
    list_of_dict_deelnemers = [
        {'arthur' : 'Arthur is enkel aanwezig als hij eerst Turkije overleeft. Dedicated IT hotline tijdens de reis, tevens ingehuurd door de Georgische overheid voor cybersecurity tegen Rusland'},
        {'stijn' : 'Stijn heeft zo weinig te doen dat hij de hele Lonely Planet uit zijn hoofd heeft geleerd en is hard onderweg om zijn diploma native Georgisch te halen. '},
        {'lucas' : 'Lucas staat er om bekend om nooit om tijd ergens aanwezig te zijn, dit gold ook voor de reiscommissie vergaderingen. Maar geen zorgen de walking tours zijn tot in de puntjes georganiseerd.'},
        {'dion' : 'Dion is een crispy Bourgondiër die erg gretig was om de wijn tour te organiseren, dit kan niet goed gaan.'},
        {'dylan' : 'Dylan heeft ooit beloofd een track te maken voor onze Georgië tour, we hebben hem nog niet gezien in de Spotify hot one hundred. Staan natuurlijk open voor een live performance op het Vrijheidsplein in Georgië, midden tussen de demonstranten.'},
        {'martijn' : 'Martijn aan het stuur, zelfs de Georgische road rage krijgt hem niet te pakken. Maar speciaal voor hem een detour door Zuid-Ossetië, om zijn rijskills op de proef te stellen.'},
        {'mas' : 'Mas staat op alle dagen geregistreerd als emergency contact, dan wordt er gegarandeerd binnen twee seconde gereageerd. Neemt waarschijnlijk een zwerfkat mee op de terugweg.'},
        {'iyer' : 'Iyer staat in het Guinness World Book of Records als deelnemer met allerslechtste vertrekvlucht. Hebben via via vernomen dat hij ergens een kind verwekt heeft, maar dit nog niet aan Luuk durft te vertellen.'},
        {'tonie' : 'Tonie staat in het Guinness World Book of Records als deelnemer met allerslechtste aankomstvlucht. Waarschijnlijk daardoro permanent salty,'},
        {'jeroen' : 'Jeroen, ook wel Project Leader Jer genoemd op de straat, heeft de bottleservice in Tblisi al gereserveerd. Streeft Toine voorbij met more money than all of us combined, bakken are on him tonight.'},
        {'luuk' : 'Luuk wordt misschien wel de eerste man die tien rietbakken moet gaan trekken in de hoofdstad van Georgie. Het Georgische woord voor rietbak is ლერწმის ყუთი oftewel lerts’mis q’uti, dan weet je alvast hoe je het aan de politie moet gaan uitleggen.'},
        {'kevin' : 'Kevin gaat zeer waarschijnlijk last-minute cancelen vanwege een drukke periode bij McKinsey. Erg jammer want Kevbal is een nationale sport in Georgië.'},  
    ]
    list_of_dict_deelnemers_shuffled = list_of_dict_deelnemers[:]
    random.shuffle(list_of_dict_deelnemers_shuffled)
    directory = './files/images/'
    list_of_files = os.listdir(directory)
    for deelnemer_dict in list_of_dict_deelnemers_shuffled:
        
        temp_list = [filename for filename in list_of_files if str((next(iter(deelnemer_dict)))) in str(filename)]
        random_image = random.choice(temp_list)

        with col1:
            with st.container(border=True, height=160):
                st.image(directory+random_image)
        with col2:
            with st.container(border=True, height=160):
                st.write(deelnemer_dict[next(iter(deelnemer_dict))])