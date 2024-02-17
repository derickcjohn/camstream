import mysql.connector
from datetime import datetime

def append_to_mysql(data_dict):
    current_timestamp = datetime.now().strftime("%d-%m-%Y %H:%M")
    data_dict_with_timestamp = {'time-stamp': current_timestamp, **data_dict}
    values = ', '.join(['%s'] * len(data_dict_with_timestamp))
    query = f"INSERT INTO count_result VALUES ({values})"
    cursor.execute(query, tuple(data_dict_with_timestamp.values()))
    conn.commit()

try:
    conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="camstream"
    )
    cursor = conn.cursor()
    print("✔ Connection to MySQL database established successfully!")

    data_dict = {0: 7, 1: 9, 2: 3, 3: 4}
    append_to_mysql(data_dict)
except mysql.connector.Error as e:
    print(f"❌ An error occurred while establishing the connection: {str(e)}")

