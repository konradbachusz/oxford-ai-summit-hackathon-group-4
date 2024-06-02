import streamlit as st
import numpy as np
from PIL import Image
from logo import display_logo
from recommendations import get_recommendations



def show_camera_on():

    display_logo()
    img_file_buffer = st.camera_input("'Capture from Camera'")

    if img_file_buffer is not None:
        # To read image file buffer as a PIL Image:
        image = Image.open(img_file_buffer)

        # To convert PIL Image to numpy array:
        img_array = np.array(image)

        st.image(image, caption='Uploaded Image', use_column_width=True)

        
        #TODO Pass the image to the model and return the predicted label e.g "scarf", "shirt" etc.
        predicted_label = "Shirts" #TODO: This is a mock. Please change this to an actual prediction

        get_recommendations(predicted_label)



if __name__ == "__main__":
    show_camera_on()

