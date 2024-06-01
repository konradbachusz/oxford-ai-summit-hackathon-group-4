import streamlit as st
from logo import display_logo

def show_home():
    display_logo()
    st.header("Welcome to ClothesTalk AI")
    st.subheader("Your Fashion Discovery and Styling Assistant")
    long_text_1 = """
    <strong>Discover. Style. Connect.</strong> Elevate your fashion game with ClothesTalk AI, 
    the ultimate platform that transforms how you find and interact with fashion. 
    Powered by advanced artificial intelligence, ClothesTalk AI allows you to effortlessly 
    search for clothing using just an image. Snap or upload a photo, and let our innovative 
    technology find similar items from a diverse inventory provided by leading fashion 
    companies.
    """

    long_text_2 = """
        <strong>Personalized Recommendations Just for You.</strong>
        Dive into a personalized shopping experience that caters to your style preferences. 
        ClothesTalk AI analyzes your tastes and shopping behavior to recommend outfits that 
        not only match but enhance your personal style. Whether you're prepping for a casual 
        outing or a formal event, our smart recommendations ensure you always look your best.
        """

    long_text_3 = """
            <strong>Connect with the Fashion World.</strong> 
            Join our vibrant community of fashion enthusiasts, bloggers, and industry experts. 
            ClothesTalk AI is more than just a platform; it's a network where fashion meets innovation. 
            Explore reviews from esteemed fashion bloggers, get insights from trendsetters, and interact with brands 
            and designers who set the pace in the fashion world.
            """


    # Custom HTML and CSS for the text box
    st.markdown(f"""
    <div style="border: 1px solid #e0e0e0; padding: 20px; border-radius: 10px; background-color: #f9f9f9;">
        {long_text_1}
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div style="border: 1px solid #e0e0e0; padding: 20px; border-radius: 10px; background-color: #f9f9f9;">
            {long_text_2}
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
            <div style="border: 1px solid #e0e0e0; padding: 20px; border-radius: 10px; background-color: #f9f9f9;">
                {long_text_3}
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    show_home()
