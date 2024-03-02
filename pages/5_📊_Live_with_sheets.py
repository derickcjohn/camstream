import streamlit as st
from streamlit_gsheets import GSheetsConnection
from PIL import Image

image = Image.open('icon.png')

st.set_page_config(page_title="Cam stream Data - Live", 
                   page_icon=image, 
                   initial_sidebar_state="expanded",
                  layout="wide")

# hide_streamlit_style = """
#             <style>
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.sidebar.success("Select a page from above")

st.markdown("""
<style>
[data-testid="stDateInput"] [data-baseweb="input"]:before {
    content: url(https://i.imgur.com/pIZPHar.jpg) !important;
    padding-top: 8px !important;
    padding-left: 7px !important;
}
</style>
""", unsafe_allow_html=True)

st.header("Exploring Camera Stream Data")
# st.text("This page allows you to delve into your Camstream data collected on various dates.")
url = "https://docs.google.com/spreadsheets/d/11o-ZoNmn4-FdCHd0gJuZMrUC-3mYFgo2EheHKIJfhvE/edit?usp=sharing"
# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(spreadsheet=url, usecols=[0, 1,2,3])
st.dataframe(df)
