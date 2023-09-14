import streamlit as st
import openai
from PIL import Image
from streamlit_extras.buy_me_a_coffee import button

openai.api_key = st.secrets["api_key"]

# 화면 상단 여백 제거
st.write("<style>div.block-container{padding-top:2rem;}</style>", unsafe_allow_html=True)

# 제목
st.title("SketchBot AI")
st.markdown("##### Where Ideas Blossom into Art")

# 그림 주제, 크기 입력
with st.form("form"):
    subjectOfPicture = st.text_input("Please enter the subject of the picture")
    sizeOfPicture = st.selectbox("Size of picture", ["256x256", "512x512", "1024x1024"])
    submit = st.form_submit_button("Submit")

if submit and subjectOfPicture:
    gpt_prompt = [{
        "role":"system",
        "content":"Imagine the detail appearance of the input. Response it shortly around 20 words"
    }]

    gpt_prompt.append({
        "role":"user",
        "content":subjectOfPicture
    })
    
    with st.spinner("Waiting for ChatGPT..."): 
        gpt_response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo-16k",
            messages = gpt_prompt   
        )
    
    dalle_prompt = gpt_response["choices"][0]["message"]["content"]
    with st.spinner("Waiting for DALL.E..."): 
        dalli_response = openai.image.create(
            prompt = dalle_prompt,
            size = sizeOfPicture
        ) 
    
    st.image(dalli_response["data"][0]["url"])

st.write("Powered by Chat GPT and DALL.E")

# 수익화
from streamlit_extras.buy_me_a_coffee import button
button(username="jakukyr", floating=True, text="Please, buy me a coffee", font="Lato", width=320) 