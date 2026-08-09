import streamlit as st
import gtts
import os
from PIL import Image

st.set_page_config(page_title="Aura Future - AI Avatar", page_icon="⚡", layout="centered")

# Custom CSS for Red & Black Theme and Background Logo Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0b0b;
        color: #ffffff;
        background-image: linear-gradient(rgba(11,11,11,0.9), rgba(11,11,11,0.9)), 
                          radial-gradient(circle at center, #ff1a1a 0%, transparent 70%);
        background-size: cover;
        background-attachment: fixed;
    }
    h1, h2, h3 {
        color: #ff1a1a !important;
        text-shadow: 0px 0px 10px rgba(255, 26, 26, 0.5);
    }
    .stChatMessage {
        background-color: #1a1a1a !important;
        border: 1px solid #ff1a1a33;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>⚡ Aura Future - AI Avatar</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #ff4d4d;'>Aapka apna custom digital clone aur AI system.</p>", unsafe_allow_html=True)

# Upload Your Avatar (Steps removed)
st.markdown("### 🖼️ Upload Your Avatar")
uploaded_file = st.file_uploader("Apni picture upload karein", type=["jpg", "png", "jpeg"])

avatar_img = None
if uploaded_file is not None:
    avatar_img = Image.open(uploaded_file)
    st.image(avatar_img, caption="Aura Avatar Visual Set", width=200)
    st.success("Avatar loaded successfully!")

# Chat with Aura Avatar (Steps removed)
st.markdown("### 💬 Chat with Aura Avatar")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    avatar_icon = avatar_img if (message["role"] == "user" and avatar_img) else ("🔴" if message["role"] == "user" else "⚡")
    with st.chat_message(message["role"], avatar=avatar_icon):
        st.markdown(message["content"])

# Accept user input & Smart AI responses
if prompt := st.chat_input("Apne clone se kuch poochein..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    user_icon = avatar_img if avatar_img else "🔴"
    with st.chat_message("user", avatar=user_icon):
        st.markdown(prompt)

    # Smart AI Response Logic
    prompt_lower = prompt.lower()
    if "pakistan" in prompt_lower:
        response_text = "Pakistan 14 August 1947 ko duniya ke nakshay par wajood mein aaya tha."
    elif "kaise ho" in prompt_lower or "kese ho" in prompt_lower:
        response_text = "Main bilkul theek hoon! Aap batayein, Aura Future ke liye aaj kya plan hai?"
    elif "naam" in prompt_lower:
        response_text = "Mera naam Aura Future AI Avatar hai, aur main aapka digital clone hoon."
    else:
        response_text = f"Aapne bohot achha sawal pucha hai '{prompt}'. Aura Future system is par mukammal taur par kaam kar raha hai aur aapko behtareen nataij faraham karega!"
    
    with st.chat_message("assistant", avatar="⚡"):
        st.markdown(response_text)
        
        # Text-to-Speech Voice Generation (Bolne wala system)
        try:
            tts = gtts.gTTS(text=response_text, lang='ur')
            audio_file = "temp_voice.mp3"
            tts.save(audio_file)
            st.audio(audio_file, format='audio/mp3', autoplay=True)
        except Exception as e:
            pass

    st.session_state.messages.append({"role": "assistant", "content": response_text})
