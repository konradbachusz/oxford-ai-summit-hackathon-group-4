import streamlit as st

def main():
    st.title("Hello, World!")


    picture = st.camera_input("Take a picture")

    if picture:
        st.image(picture)

if __name__ == "__main__":
    main()
