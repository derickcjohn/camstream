import cv2
import streamlit as st
from PIL import Image
import socket, pickle, struct

# Load the image
image = Image.open('icon.png')

st.set_page_config(page_title="Cam stream Data - Demo", 
                   page_icon=image, 
                   initial_sidebar_state="expanded",
                   layout="wide")

# hide_streamlit_style = """
#             <style>
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.header("Hosting a server")
st.info("This is to get and display the server IP address.", icon="ℹ️")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
st.write('HOST IP:', host_ip)
port = 8501
socket_address = (host_ip, port)

# Socket Bind
server_socket.bind(socket_address)

# Socket Listen
server_socket.listen(5)
st.write("LISTENING AT:", socket_address)

placeholder = st.empty()

# Socket Accept
while True:
    client_socket, addr = server_socket.accept()
    st.write('GOT CONNECTION FROM:', addr)
    if client_socket:
        # Receive frame from client
        data = b""
        payload_size = struct.calcsize("Q")
        while True:
            while len(data) < payload_size:
                packet = client_socket.recv(4 * 1024)  # 4K
                if not packet: break
                data += packet
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("Q", packed_msg_size)[0]

            while len(data) < msg_size:
                data += client_socket.recv(4 * 1024)
            frame_data = data[:msg_size]
            data = data[msg_size:]
            frame = pickle.loads(frame_data)

            # Process frame using YOLO model (as in the original server code)
            # results = model(frame)
            # frame = np.squeeze(results.render())

            # Display the processed frame
            # cv2.imshow('RECEIVING AND PROCESSING VIDEO', frame)
            placeholder.image(frame, channels="BGR", width = None)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break

        client_socket.close()
