import streamlit as st
import numpy as np
from PIL import Image
import cv2
from logo import display_logo


def show_camera_on():
    display_logo()
    st.header("Camera On")
    capture = st.button('Capture from Camera')

    if capture:
        # Open the camera
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            st.error("Could not open camera.")
        else:
            ret, frame = cap.read()
            cap.release()  # Release the camera immediately after capturing

            if ret:
                # Convert the frame to RGB (cv2 captures in BGR)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Convert the frame to PIL image
                img = Image.fromarray(frame)

                # Convert the PIL image to numpy array
                img_array = np.array(img)

                st.image(img, caption='Captured Image', use_column_width=True)
            else:
                st.error("Failed to capture image.")


if __name__ == "__main__":
    show_camera_on()

