import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
from lib.utils import change_button_height 
from streamlit_navigation_bar import st_navbar
import os

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.session_state['current_page'] = 'INSPIRATIE'

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

directory = './files/inspiratie'
list_of_inspiratie_names = []
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    list_of_inspiratie_names.append(filename)

col1, col2, col3 = st.columns([0.5,60,0.5])

with col2:
    grid_width = 5
    grid_width_list = [1] + ([1] * grid_width) + [1]
    cols = st.columns(grid_width_list)

    for index, image in enumerate(list_of_inspiratie_names):
        if (index % grid_width) == 0:
            cols[0].write("")
            cols[len(grid_width_list) - 1].write("")

        cols[(index % grid_width) + 1].image(f'./files/inspiratie/{image}')