import streamlit as st
import cv2
import numpy as np

st.title("AI Candlestick Buy/Sell Detector")

uploaded_file = st.file_uploader("Upload Chart Image", type=["png","jpg","jpeg"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes,1)

    st.image(image, channels="BGR")
    st.write("Chart uploaded successfully")
