import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
from lib.utils import change_button_height 
from streamlit_navigation_bar import st_navbar
from streamlit_calendar import calendar
import os

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

if "current_page" not in st.session_state:
    st.session_state['current_page'] = 'AGENDA'

elif "current_page" in st.session_state:
    st.session_state['current_page'] = 'AGENDA'

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

col1, col2, col3 = st.columns([1, 4, 1])

calendar_options = {
    'editable': True,
    'selectable': True,
    'headerToolbar': {
        'left': 'today',
        'center': '',
        'right': 'prev,next',
    },
    'slotMinTime': "07:00:00",
    'slotMaxTime': '23:00:00',
    'initialView': "timeGridWeek",
    'allDaySlot' : False
}

calendar_events = [
    {
        "title": "VLUCHT AMSTERDAM-TBLISI",
        "start": "2024-06-29T10:40:00",
        "end": "2024-06-29T17:50:00",
        "resourceId": "random",
    },

    {
        "title": "INCHECKEN CARAVAN VILLA",
        "start": "2024-06-29T18:00:00",
        "end": "2024-06-29T19:00:00",
        "resourceId": "random",
    },

    {
        "title": "DINNER SHAVI LOMI",
        "start": "2024-06-29T19:00:00",
        "end": "2024-06-29T21:00:00",
        "resourceId": "random",
    },

    {
        "title": "PARTY CLUB SECRET",
        "start": "2024-06-29T21:00:00",
        "end": "2024-06-29T24:00:00",
        "resourceId": "random",
    },

    {
        "title": "WALKING TOUR TBLISIS LH SPECIAL",
        "start": "2024-06-30T11:00:00",
        "end": "2024-06-29T16:00:00",
        "resourceId": "random",
    },

    {
        "title": "DINNER HIDE TBLISI",
        "start": "2024-06-30T19:00:00",
        "end": "2024-06-30T21:00:00",
        "resourceId": "random",
    },

    {
        "title": "PUBCRAWL KEVUUK",
        "start": "2024-06-30T21:00:00",
        "end": "2024-06-30T00:00:00",
        "resourceId": "random",
    },

    {
        "title": "START ROADTRIP",
        "start": "2024-07-01T10:00:00",
        "end": "2024-07-01T11:00:00",
        "resourceId": "random",
    },

    {
        "title": "WINETOUR MONASTERY TYPE BEAT DION",
        "start": "2024-07-01T11:30:00",
        "end": "2024-07-01T17:00:00",
        "resourceId": "random",
    },

    {
        "title": "DINNER NEKRESI ESTATE",
        "start": "2024-07-01T19:00:00",
        "end": "2024-07-01T21:00:00",
        "resourceId": "random",
    },

    {
        "title": "STIJN SECRET KAUKHETI DAY",
        "start": "2024-07-02T09:00:00",
        "end": "2024-07-02T21:00:00",
        "resourceId": "random",
    },    

    {
        "title": "DRIVE ROADTRIP KAZBEGI",
        "start": "2024-07-03T09:00:00",
        "end": "2024-07-03T13:00:00",
        "resourceId": "random",
    },   

    {
        "title": "ADVENTUROUS OPTIONAL WARMDRAAI HIKE",
        "start": "2024-07-03T14:00:00",
        "end": "2024-07-03T17:00:00",
        "resourceId": "random",
    },  


    {
        "title": "BIG BOY HIKE ONLY BIG PEEPEE",
        "start": "2024-07-04T09:00:00",
        "end": "2024-07-04T18:00:00",
        "resourceId": "random",
    },


    {
        "title": "RECOVERY DINER PANORAMA KAZBEGI",
        "start": "2024-07-04T19:00:00",
        "end": "2024-07-04T21:00:00",
        "resourceId": "random",
    },

    {
        "title": "BIG BOY DRIVE INCLUDING LUNCH",
        "start": "2024-07-05T09:00:00",
        "end": "2024-07-05T15:00:00",
        "resourceId": "random",
    },

    {
        "title": "CHECK IN DOUBLE HOUSE KILL",
        "start": "2024-07-05T15:00:00",
        "end": "2024-07-05T17:00:00",
        "resourceId": "random",
    },

    {
        "title": "WALKING DINNER TOMA WINE CELLAR",
        "start": "2024-07-05T17:00:00",
        "end": "2024-07-05T21:00:00",
        "resourceId": "random",
    },

    {
        "title": "KUTAISI TIJD OM TE VLAMMEN",
        "start": "2024-07-05T21:00:00",
        "end": "2024-07-05T00:00:00",
        "resourceId": "random",
    },

    {
        "title": "SENATORIUM GROT SPA",
        "start": "2024-07-06T09:00:00",
        "end": "2024-07-06T17:00:00",
        "resourceId": "random",
    },

    {
        "title": "DINNER HACKER PSCHORRI",
        "start": "2024-07-06T19:00:00",
        "end": "2024-07-06T21:00:00",
        "resourceId": "random",
    },

    {
        "title": "GELATTI MONASTERY PRAY",
        "start": "2024-07-07T10:00:00",
        "end": "2024-07-07T11:00:00",
        "resourceId": "random",
    },

    {
        "title": "TOUGH DRIVE TBLISI",
        "start": "2024-07-07T11:00:00",
        "end": "2024-07-07T14:30:00",
        "resourceId": "random",
    },

    {
        "title": "CHECK IN ELIA BOUTIQUE HOSTEL",
        "start": "2024-07-07T15:00:00",
        "end": "2024-07-07T15:30:00",
        "resourceId": "random",
    },

    {
        "title": "REFLECT ON LIFE",
        "start": "2024-07-07T15:30:00",
        "end": "2024-07-07T18:30:00",
        "resourceId": "random",
    },


    {
        "title": "FLIGHT TBLISI - AMSTERDAM",
        "start": "2024-07-08T04:30:00",
        "end": "2024-07-08T09:40:00",
        "resourceId": "random",
    },


]

col1, col2, col3 = st.columns([1,6,1])

with col2:
    calendar = calendar(events=calendar_events, options=calendar_options)
