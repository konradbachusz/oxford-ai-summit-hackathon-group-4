import streamlit as st

def main():
    st.title("Group 4 Clothes Classifier")


    picture = st.camera_input("Take a picture")

    if picture:
        st.image(picture)

if __name__ == "__main__":
    main()
