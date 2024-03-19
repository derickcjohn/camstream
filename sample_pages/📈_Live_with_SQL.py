import streamlit as st
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

try:
    conn = st.connection('mysql', type='sql')
    
except Exception as e:
    
    st.error(f"An error occurred while establishing the connection: {str(e)}", icon="❌")
    st.stop()
try:
    data = conn.query('SELECT * FROM count_result ORDER BY 1 DESC LIMIT 50;', ttl=10)
    
except Exception as e:
    
    st.error(f"An error occurred while establishing the connection: {str(e)}", icon="❌")
    st.stop()

def daily(date):
    query = ("SELECT DATE_FORMAT(time_stamp, '%H') AS Hour, "
             "SUM(can) AS Cans, "
             "SUM(milk_jug) AS 'Milk Jug', "
             "SUM(non_white_jug) AS 'Non white jug', "
             "SUM(plastic_bottle) AS 'Plastic bottles' "
             "FROM count_result "
             "WHERE DATE(time_stamp) = '" + date.strftime('%Y-%m-%d') + "' "  
             "GROUP BY Hour;")
    
    # Execute the query with the date parameter
    df = conn.query(query, ttl=10)
    return df, 'Hour'

def weekly(date):
    query = (
        "SELECT DATE(time_stamp) AS Date, "
        "SUM(can) AS Cans, "
        "SUM(milk_jug) AS 'Milk Jug', "
        "SUM(non_white_jug) AS 'Non white jug', "
        "SUM(plastic_bottle) AS 'Plastic bottles' "
        "FROM count_result "
        "WHERE time_stamp >= '{start_date}' "
        "AND time_stamp < DATE_ADD('{start_date}', INTERVAL 7 DAY) "
        "GROUP BY Date;"
    ).format(start_date=date.strftime('%Y-%m-%d'))
    
    # Execute the query with the date parameter
    df = conn.query(query, ttl=10)
    return df, 'Date'

with st.expander("Data Preview"):
  st.info("New data is constantly added. Click 'R' to refresh and view it.", icon="ℹ")
  st.dataframe(data, use_container_width=True, hide_index=True)

min_date_df = conn.query('SELECT MIN(DATE(time_stamp)) AS min_date FROM count_result;')
max_date_df = conn.query('SELECT MAX(DATE(time_stamp)) AS max_date FROM count_result;')

min_date = min_date_df.iloc[0, 0] if not min_date_df.empty else None
max_date = max_date_df.iloc[0, 0] if not max_date_df.empty else None

selected_date = st.date_input("Select Date", value=None, min_value=min_date, 
                              max_value=max_date, format="DD/MM/YYYY")

if selected_date is None:
   st.info("Select a Date", icon="ℹ")
   st.stop()

display_mode = st.radio('Select Display Mode', ['Daily', 'Weekly'])

if display_mode == 'Daily':
    result, x_label = daily(selected_date)
    
else:
    result, x_label = weekly(selected_date)
    
st.divider()
st.dataframe(result, use_container_width=True, hide_index=True)
st.divider()
st.bar_chart(result.set_index(result.columns[0]), color=[
    '#FFC0CB',  # Light Red (Pink)
    # '#FF6347',  # Tomato
    '#FF5733',  # Medium Red
    # '#FF2400',  # Scarlet
    '#DC143C',  # Crimson
    # '#CD5C5C',  # Indian Red
    '#8B0000',  # Dark Red (Maroon)
    # '#800000'   # Dark Red (Maroon)
])


classes = result.columns[1:]
selected_class = st.selectbox("Select an object from the list", classes)
if display_mode == 'Daily':
    st.bar_chart(result.set_index(x_label)[selected_class], color='#666666')
else:
    st.bar_chart(result.set_index('Date')[selected_class], color='#666666')
    
