from streamlit_webrtc import webrtc_streamer, WebRtcMode, VideoProcessorBase
from sample_utils.turn import get_ice_servers
# from sample_utils.tracker import *
import av
import cv2
import streamlit as st
from PIL import Image
import yolov5
import numpy as np

# Load the image
image = Image.open('icon.png')

st.set_page_config(page_title="Cam stream Data - Demo", 
                   page_icon=image, 
                   initial_sidebar_state="expanded",
                   layout="wide")

# st.set_page_config(page_title="Cam stream Data - Demo", 
#                    page_icon=image,
#                    layout="wide")


# hide_streamlit_style = """
#             <style>
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.sidebar.page_link(
  "https://camstream.streamlit.app/Demo",  
  label="Demo",
  icon="📷",
  disabled=True)

st.header("Webstream for Live Object Detection")
st.info("This is a Demo of simple Object Detection.", icon="ℹ️")
with st.container(border=True):
  st.caption("Click on START to view a simple object detection using YOLOv5.")

@st.cache_resource
def load_model():
  model_load =  yolov5.load('../yolov5s.pt')
  return model_load

model = load_model()

class callback(VideoProcessorBase):
   def __init__(self, model):
        self.model = model
   def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
      img = frame.to_ndarray(format="bgr24")
      # img = cv2.resize(img, (640, 640))
      results = model(img)
      img = np.squeeze(results.render())
      
      return av.VideoFrame.from_ndarray(img, format="bgr24")

webrtc_streamer(
        key="LiveFaceRecognition",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration={
        "iceServers": get_ice_servers()},
        media_stream_constraints={"video": {"width": 1280, "height": 720}, "audio": False},
        video_processor_factory=lambda: callback(model),
        async_processing=True,
    )
