import streamlit as st
from PIL import Image

def display_logo():
    logo = Image.open("src\Logo-without text.png")  # Update with the correct path to your logo image
    st.image(logo, use_column_width=False, width=150)


def blog_description():
    long_text_1 = """
            Welcome to our dedicated space for fashion enthusiasts to share 
            their passion and creativity. Our platform is designed to empower fashion bloggers 
            and boutique retailers, offering them a unique opportunity to express themselves, 
            share their insights, and connect with a like-minded community. 
            Because fashion is more than just trends.
            """
    # Custom HTML and CSS for the text box
    st.markdown(f"""
            <div style="border: 1px solid #e0e0e0; padding: 20px; border-radius: 10px; background-color: #f9f9f9;">
                {long_text_1}
            </div>
            """, unsafe_allow_html=True)
