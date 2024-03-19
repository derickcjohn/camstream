import streamlit as st
import socket
import pickle
import struct
from PIL import Image

# Set up the Streamlit app layout
st.title("Video Streaming with Streamlit")
video_placeholder = st.empty()

# Socket connection
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = "61.3.150.20"  # Replace with the actual IP where your client.py is running
port = 9999
socket_address = (host_ip, port)

# Connect to the server
client_socket.connect(socket_address)

# Receiving video frames and displaying them
while True:
    try:
        data = b""
        payload_size = struct.calcsize("Q")

        while len(data) < payload_size:
            packet = client_socket.recv(4 * 1024)  # 4K buffer size
            if not packet:
                break
            data += packet

        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]

        while len(data) < msg_size:
            data += client_socket.recv(4 * 1024)

        frame_data = data[:msg_size]
        data = data[msg_size:]

        frame = pickle.loads(frame_data)
        image = Image.fromarray(frame)

        # Display the video frame in Streamlit
        video_placeholder.image(image, channels="BGR")

    except Exception as e:
        print(e)
        break
