import requests
import streamlit as st 
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from PIL import Image
st.set_page_config(page_title='Revotize',layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()    

#CSS file call
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css('style/style.css')
#Logo Image 
img_logo = Image.open("images/img3.png")
logo = img_logo.resize ((138,128))

#footer
  
# Loading lottie files
lottie1= load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_nfoB9wNpDK.json")
lottie2=load_lottieurl("https://lottie.host/0aaecf16-714c-4079-89e5-8d9553879e52/nrjh4rfR9I.json")
lottie3=load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_pig3salw.json")
lottie4=load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_eqg7s83h.json")
with st.container():
    st.image(logo)    
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("Transform Your Business into a Digital Powerhouse.")
        st.subheader("The Strategies of Revotize are to Maximize Your Online Potential and Boost Your Bottom Line with Data-Driven Strategies, Innovative Technology and Creative Ideas to Drive Business Growth.")
    with right_column:
        st_lottie(lottie1, height=360, key="digitalMarketing")
with st.container():
    st.write("---")
    left_column, right_column =st.columns(2)
    with left_column:
        st.header("What We Do")
        st.subheader("Revotize is a digital marketing platform that helps businesses improve their online presence, engage with customers, and grow their revenue.")
        st.write('''Digital Marketing strategies that Revotize can use to transform customers' businesses online.
        ''')
        st.write("Social media marketing: Revotize can help businesses build a strong social media presence on platforms like Facebook, Instagram, and Twitter. They can create engaging content, run targeted ads, and monitor customer feedback to help businesses increase their brand awareness and customer engagement")
        st_lottie(lottie3, height=330, key="DM")
        st.write("Content marketing: Content marketing involves creating and distributing valuable and relevant content to attract and engage a specific target audience. Revotize can help businesses create high-quality content that resonates with their audience, such as blog posts, infographics, and videos, and distribute them through various channels like social media, email, and their website.")
        st.write("Customer engagement: Revotize can help businesses engage with their customers by offering loyalty programs, creating engaging content, and encouraging customer feedback. By keeping customers engaged, businesses can build stronger relationships with them and increase their loyalty.")

        st.write("Web design and development: Revotize can help businesses create a user-friendly and visually appealing website that represents their brand and provides an excellent user experience. A well-designed website can help businesses build trust with their customers and increase their chances of converting visitors into customers.")
        

    with right_column:
        st_lottie(lottie2, height=350, key="digitalMarketin")    
        st.write("Email marketing: Email marketing is a powerful way to reach out to customers and keep them informed about your business. Revotize can help businesses create effective email campaigns that target specific customer groups and deliver personalized messages.")
        st.write("Search engine optimization (SEO): Revotize can help businesses improve their website's SEO, making it more visible to search engines and increasing its organic traffic. They can conduct keyword research, optimize website content, and build high-quality backlinks to improve website ranking and increase online visibility.")
        st.write("Pay-per-click (PPC) advertising: PPC advertising is a way of placing ads on search engines and social media platforms that charge businesses based on the number of clicks their ads receive. Revotize can help businesses create and manage effective PPC campaigns that target specific keywords and customer groups, increasing the chances of converting clicks into customers.")
        st_lottie(lottie4, height=300, key="data")
with st.container():
    st.write("---")
    st.header("Connect With Us!")
    st.write("##")
    contact_form = """
            <form action="https://formsubmit.co/311724b541bce2c5ee47a45341602a85" method="POST">
                <input type="hidden" name="_captcha" value='false'>
                <input type="text" name="name" placeholder="Your Name"required>
                <input type="email" name="email" placeholder="Your Email Address" required>
                <textarea type="text" namme="message" placeholder="Let's Connect" required></textarea>
                <button type="submit">Send</button>
            </form>
            """
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)    

