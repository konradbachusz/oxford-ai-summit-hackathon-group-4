import streamlit as st
from home import show_home
from upload_image import show_upload_image
from camera_on import show_camera_on
from database import init_db, add_post, delete_post, get_all_posts
from logo import display_logo, blog_description

# Initialize the database
init_db()

def show_blog():
    display_logo()
    st.header("Let's talk about fashion")
    blog_description()

    # Add a new post
    st.subheader("Add a New Post")
    with st.form(key='add_post_form'):
        title = st.text_input("Title")
        author = st.text_input("Author")
        content = st.text_area("Content")
        submit_button = st.form_submit_button(label='Add Post')

        if submit_button:
            if title and author and content:
                add_post(title, author, content)
                st.success("Post added successfully!")
            else:
                st.error("Title, author and content are required.")

    # Display all posts
    st.subheader("All Posts")
    posts = get_all_posts()
    for post in posts:
        st.markdown(f"### {post[1]}")
        st.write(post[2])
        st.write(post[3])
        if st.button(f"Delete Post", key=f"delete_{post[0]}"):
            delete_post(post[0])
            st.success(f"Post {post[0]} deleted!")
            st.experimental_rerun()


PAGES = {
    "Home": show_home,
    "Upload Image": show_upload_image,
    "Camera On": show_camera_on,
    "Blog": show_blog,
}

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]
    page()

if __name__ == "__main__":
    main()

