import streamlit as st
import numpy as np
from PIL import Image
from logo import display_logo


def show_upload_image():
    display_logo()
    st.header("Upload an Image")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image_array = np.array(image)

        st.image(image, caption='Uploaded Image', use_column_width=True)
        st.write("Image Shape:", image_array.shape)

if __name__ == "__main__":
    show_upload_image()
