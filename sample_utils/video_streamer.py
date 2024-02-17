import streamlit as st
import os
import cv2

video_path = 'waste.mp4'

capture = cv2.VideoCapture(video_path)
placeholder = st.empty()
placeholder.write("Loading video")

while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        placeholder.image(frame, channels="BGR", width = 800)
    else:
        break
capture.release()
placeholder.empty()
placeholder.write("Video has ended")
