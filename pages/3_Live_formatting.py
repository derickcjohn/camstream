import streamlit as st
import altair as alt
import pandas as pd
from datetime import timedelta
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
  st.info("New data is constantly added. Click 'R' to refresh and view it.", icon="ℹ")
  st.dataframe(data, use_container_width=True, hide_index=True)

st.divider()

data['time-stamp'] = pd.to_datetime(data['time-stamp'], format='%d/%m/%Y %H:%M:%S')
set_date = set(data['time-stamp'].dt.date)

min_date = data['time-stamp'].min().date()
max_date = data['time-stamp'].max().date()
selected_date = st.date_input("Select Date", value=None, min_value=min_date, 
                              max_value=max_date, format="DD/MM/YYYY")

if selected_date is None:
    st.info("Select a Date", icon="ℹ")
    st.stop()

if selected_date not in set_date:
    st.warning("Selected date is not available, please select another date.", icon="⚠️")
    st.stop()

display_mode = st.radio('Select Display Mode', ['Daily', 'Weekly'])

if display_mode == 'Daily':
    result, x_label = daily(selected_date, data)
else:
    result, x_label = weekly(selected_date, data)

st.divider()
st.dataframe(result, use_container_width=True, hide_index=True)
st.divider()
# st.dataframe(result.set_index(result.columns[0]), use_container_width=True, hide_index=True)
st.bar_chart(result, x = x_label, color=[
    '#FFC0CB',  # Light Red (Pink)
    # '#FF6347',  # Tomato
    '#FF5733',  # Medium Red
    # '#FF2400',  # Scarlet
    '#DC143C',  # Crimson
    # '#CD5C5C',  # Indian Red
    '#8B0000',  # Dark Red (Maroon)
    # '#800000'   # Dark Red (Maroon)
])
# c = alt.Chart(result).mark_bar().encode(
#     x='Hour',
# )
# st.altair_chart(c, use_container_width=True)

classes = result.columns[1:]
selected_class = st.selectbox("Select an object from the list", classes)
if display_mode == 'Daily':
    filtered_result = result[[x_label, selected_class]]  
    st.dataframe(filtered_result, use_container_width=True, hide_index=True)
    st.bar_chart(filtered_result, x = x_label, color='#666666')
    # st.bar_chart(result.set_index(x_label)[selected_class], color='#666666')
else:
    filtered_result = result[[x_label, selected_class]]  
    st.bar_chart(filtered_result, x = x_label, color='#666666')
