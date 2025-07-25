import streamlit as st
import base64
from openai import OpenAI

st.title("Fortune Teller with Palm Analysis")
enable = st.checkbox("Enable camera")
img = st.camera_input("Take a picture", disabled = not enable)

# Function to encode the image
def encode_image(image):
    return base64.b64encode(image).decode("utf-8")

api_key = st.sidebar.text_input("OpenAI API Key", type = "password")

if img:

    client = OpenAI(api_key = api_key)

    img = img.getvalue()
    base64_image = encode_image(img)

    response = client.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "user",
                "content": [
                    { "type": "input_text", "text": "You are now a fortune teller. Please help me read this person’s palm and tell me about his traits and personality. Then, give me advice on what kind of career suits him, as well as insights into his destiny, health, wealth, love life, and family. This person is male." },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{base64_image}",
                    },
                ],
            }
        ],
    )

    st.header("Response")
    st.write(response.output_text)