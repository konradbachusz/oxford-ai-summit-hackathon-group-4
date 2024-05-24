import streamlit as st
from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt

# Load the model and processor
processor = AutoImageProcessor.from_pretrained("harshp8l/Fashion-Product-Images")
model = AutoModelForImageClassification.from_pretrained("harshp8l/Fashion-Product-Images")

# Function to load and predict the class of an image
def classify_image(image):
    """
    Predicts the class of an image using a Hugging Face model.

    Parameters:
    - image: PIL image to be classified.
    """
    # Preprocess the image and prepare it for the model
    inputs = processor(images=image, return_tensors="pt")

    # Predict the class of the image
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()

    # Retrieve the class name using the predicted class index
    class_name = model.config.id2label[predicted_class_idx]
    return class_name

# Streamlit web app main function
def main():
    st.title("Group 4 Clothes Classifier")

    # Streamlit widget to accept user input image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Convert the file to an image
        image = Image.open(uploaded_file)
        
        # Display the image
        st.image(image, caption='Uploaded Image', use_column_width=True)
        
        # Classify the image
        if st.button('Classify'):
            # Call the classify_image function
            class_name = classify_image(image)
            st.write(f"Predicted class: {class_name}")

if __name__ == "__main__":
    main()
