import streamlit as st
import numpy as np
from PIL import Image
from logo import display_logo
import glob


def show_upload_image():
    display_logo()
    st.header("Upload an Image")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image_array = np.array(image)

        st.image(image, caption='Uploaded Image', use_column_width=True)

        #Button to call the model
        recommendations_button =st.button("Get Recommendations")
        if recommendations_button:

            #TODO Pass the image to the model and return the predicted label e.g "scarf", "shirt" etc.
            predicted_label = "red_dress" #TODO: This is a mock. Please change this to an actual prediction
            st.header(f"Item predicted as {predicted_label}. Here are similar items:")
            
            #Display recommendations
            image_paths = glob.glob(f"data/{predicted_label}/*")
            count=0
            for image_path in image_paths:
                image = Image.open(image_path)
                st.image(image, caption='Item Description', use_column_width=True)
                st.button("Buy Now",key = count)
                count += 1









if __name__ == "__main__":
    show_upload_image()
