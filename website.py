from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#---Load Assets---
lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_w51pcehl.json")
img_contract_form = Image.open("images/R (1).png")
img_lottie_animation = Image.open("images/R.png")

#header emoji cheat sheet: https://www.webfx.com/tools/emoji-cheat-sheet/

st.subheader("Hi, I am Kev :wave:")
st.title("A Data Analyst")
st.write(" Learning how to make websites on Python.")
st.write("[Learn More >](https://www.fiverr.com/users/kevinmoreno342/seller_dashboard)")

# ---What I do---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I am a student at North Carolina Wesleyan University and I am currently a fourth year student I look to: 
            - Expand my knowledge on computer information systems
            - Gain more hands on experience and apply what I know into the real world 
            - Getting a Tesla Model 3 Long Range 
            If this sounds interesting to you, consider checking out Tesla's Webpage
            """
        )
        st.write("[Tesla Website >](https://www.tesla.com/)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
#---Projects---
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st. subheader("Why Tesla is the Best Car of 2022 ")
        st.write(
            """
            Learn how to use Lottie Files in Streamlit
            Animations make our web app engaging and fun, and Lottie files are the easiest way to do so
            I will implement animations based on the topic 
            """
        )
        st.markdown("[Tesla Model 3 long range...](https://www.tesla.com/model3/design#overview)")
    #---Contact---
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        contact_form = """
        <form action="https://formsubmit.co/morenokevin65@gmail.com" method="POST">
             <input type="hidden" name= "_captcha" value="false"> 
             <input type="text" name="name" placeholder="Your name" required>
             <input type="email" name="email" placeholder="Your email" required>
             <textarea name="message" placeholder= "Your message here" required></textarea>
             <button type="submit">Send</button>
        </form>
        """
        left_column,right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()