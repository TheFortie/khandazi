import streamlit as st
# from streamlit_extras.switch_page_button import switch_page
# # import streamlit.components.v1 as components
# from lib.utils import change_button_height 
from streamlit_navigation_bar import st_navbar

# st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# pages = ["KHANDZARI"]
page = st_navbar(["Home", "Documentation", "Examples", "Community", "About"])
st.write(page)

# georgia_red = "#FF0000" 
# georgia_white = "#FFFFFF"
# georgia_grey = "#424242"

# styles = {
#     "nav": {
#         "background-color": georgia_grey, 
#         "justify-content": 'left',
#     },
    
#     "hover":{ "color": georgia_red,
#     }
# }

# options = {
#     "show_menu": False,
#     "show_sidebar": False,
# }

# navigation_bar = st_navbar(
#     pages=pages,
#     styles=styles,
#     options=options,
# )

# col1, col2, col3 = st.columns ([1,1,1])

# with col1:
#     st.write("")
#     button_deelnemers =  st.button("DEELNEMERS", use_container_width=True)
#     if button_deelnemers: 
#         switch_page("DEELNEMERS")
#     change_button_height("DEELNEMERS", 160)

#     st.write("")
#     button_wereldkaart = st.button("WERELDKAART", use_container_width=True)
#     if button_wereldkaart: 
#         switch_page("MERELDKAART")
#         change_button_height("WERELDKAART", 160)

#     st.write("")

#     button_planning =st.button("PLANNING", use_container_width=True)
#     if button_planning: 
#         switch_page("PLANNING")
#     change_button_height("PLANNING", 160)

#     st.write("")

#     button_paklijst = st.button('PAKLIJST', use_container_width=True)
#     if button_paklijst: 
#         switch_page("PAKLIJST")
#         change_button_height("PAKLIJST", 160)

#     st.write("")
#     button_vibes = st.button('VIBES', use_container_width=True)
#     if button_vibes:
#         switch_page("VIBES")
#     change_button_height("VIBES", 160)