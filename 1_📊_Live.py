import streamlit as st
import pandas as pd
from datetime import timedelta
from streamlit_gsheets import GSheetsConnection
from PIL import Image

image = Image.open('icon.png')

st.set_page_config(page_title="Cam stream Data - Live", 
                   page_icon=image, 
                  layout="wide")

hide_streamlit_style = """
            <style>
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.sidebar.page_link(
  "1_📊_Live.py",  
  label="Live",
  icon="📊",
  help="Currently viewing the Page")
st.sidebar.page_link(
  "demo.py",
  # "pages/2_📷_Demo.py",  
  label="Demo",
  icon="📷",
  disabled=True,
  help="Page is in Development")
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

st.title("Exploring Camera Stream Data", anchor=False)
# st.text("This page allows you to delve into your Camstream data collected on various dates.")
url = "https://docs.google.com/spreadsheets/d/11o-ZoNmn4-FdCHd0gJuZMrUC-3mYFgo2EheHKIJfhvE/edit?usp=sharing"

try:
    # Create a connection object.
    conn = st.connection("gsheets", type=GSheetsConnection)
    
except Exception as e:
    
    st.error(f"An error occurred while establishing the connection: {str(e)}", icon="❌")
    st.stop()

data = conn.read(spreadsheet=url, ttl="0")

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

with st.expander("Data Preview"):
  st.info("Preview of latest 50 rows of data.", icon="ℹ")
  st.dataframe(data.iloc[-50:], use_container_width=True, hide_index=True)

st.divider()

data['time-stamp'] = pd.to_datetime(data['time-stamp'], format='%d/%m/%Y %H:%M:%S')
set_date = set(data['time-stamp'].dt.date)

min_date = data['time-stamp'].min().date()
max_date = data['time-stamp'].max().date()
selected_date = st.date_input("Date", value=None, min_value=min_date, 
                              max_value=max_date, format="DD/MM/YYYY")

if selected_date is None:
    st.info("Pick a Date", icon="ℹ")
    st.stop()

if selected_date not in set_date:
    st.warning("Data not available for the selected date, please select another date.", icon="⚠️")
    st.stop()

display_mode = st.radio('Display Mode', ['Daily', 'Weekly'])

if display_mode == 'Daily':
    result, x_label = daily(selected_date, data)
else:
    result, x_label = weekly(selected_date, data)

st.dataframe(result, use_container_width=True, hide_index=True)
st.divider()
st.bar_chart(result, x = x_label, color=[
    '#FFC0CB', 
    '#FF5733',  
    '#DC143C', 
    '#8B0000',  
])
st.markdown(
    f'<p style="text-align:center;">Graph displaying the total and individual counts of items detected for each {x_label}.</p>',
    unsafe_allow_html=True
)
st.divider()

classes = result.columns[1:]
selected_class = st.selectbox("Select an item to view its individual count", classes)
filtered_result = result[[x_label, selected_class]]  
st.bar_chart(filtered_result, x=x_label, color='#666666')
caption_text = f"Graph depicting the number of <i>{selected_class}</i> detected for each {x_label}."
st.markdown(
    f'<p style="text-align:center;">{caption_text}</p>',
    unsafe_allow_html=True
)
