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

data = conn.read(spreadsheet=url, usecols=[0, 1,2,3])

def daily(date, data):
    df = pd.DataFrame(data)
    df['Hour'] = pd.to_datetime(df['time-stamp']).dt.hour

    filtered_df = df[df['time-stamp'].dt.date == pd.to_datetime(date).date()].drop(columns=["time-stamp"])

    daily_df = filtered_df.groupby('Hour', as_index=True).agg('sum')
    daily_df.reset_index(inplace=True)

    return daily_df, 'Hour'

def weekly(start_date, data):
    df = pd.DataFrame(data)
    df['time-stamp'] = pd.to_datetime(df['time-stamp'])
    df['Date'] = df['time-stamp'].dt.date
    filtered_df = df.loc[(df['Date'] >= pd.to_datetime(start_date).date()) & (df['Date'] < pd.to_datetime(start_date).date() + timedelta(days=7))].drop(columns=["time-stamp"])
    
    weekly_df = filtered_df.groupby('Date', as_index=True).agg('sum')
    weekly_df.reset_index(inplace=True)

    return weekly_df, 'Date'
