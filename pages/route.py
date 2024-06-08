import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
from lib.utils import change_button_height 
from streamlit_navigation_bar import st_navbar
import os
import folium
from folium.plugins import MeasureControl
from folium.plugins import Draw

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.session_state['current_page'] = 'ROUTE'

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
    pages=pages,
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

col1, col2, col3 = st.columns([1,8,1])


georgie_map = folium.Map(location=[42.016667, 43.783333], zoom_start=8)
# folium.tile_layer("osm-bright").add_to(georgie_map)
folium.plugins.MeasureControl(position="bottomright").add_to(georgie_map)
folium.LayerControl(position="bottomright").add_to(georgie_map)
folium.plugins.Draw().add_to(georgie_map)
folium.Marker(location=[41.716667, 44.783333], popup='TBLISI',).add_to(georgie_map)
folium.Marker(location=[41.9584, 45.7946], popup='KAKHETI',).add_to(georgie_map)
folium.Marker(location=[42.65705, 44.64502], popup='KAZBEGI',).add_to(georgie_map)
folium.Marker(location=[42.26898, 42.70296], popup='KUTAISI',).add_to(georgie_map)
folium.Marker(location=[41.716667, 44.783333], popup='TBLISI',).add_to(georgie_map)

list_of_coordinates = []
with open('./files/coordinates.txt', 'r') as file:
    for line in file:  
            items = [float(x) for x in line.strip().split(',')]
            if len(items) == 2:
                list_of_coordinates.append(list(reversed(items)))


folium.PolyLine(list_of_coordinates, color="red", weight=2.5, opacity=1).add_to(georgie_map)

georgie_map.save("./files/georgie_map.html")
file = open("./files/georgie_map.html", "r", encoding="utf-8")

read_file = file.read()

with col2:
    components.html(read_file, width=None, height=600)