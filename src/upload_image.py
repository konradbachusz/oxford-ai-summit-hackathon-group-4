import streamlit as st
import numpy as np
from PIL import Image
from logo import display_logo
from recommendations import get_recommendations
from yolo import YoloModel
import pathlib


def show_upload_image():
    display_logo()
    st.header("Upload an Image")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image_array = np.array(image)

        st.image(image, caption='Uploaded Image', use_column_width=True)

        weight_path = pathlib.Path("..", "weights", "fashion-yolov8n-cls.pt")
        model = YoloModel(weight_path)
        predicted_label, conf = model.predict(image_array)

        get_recommendations(predicted_label)


if __name__ == "__main__":
    show_upload_image()
