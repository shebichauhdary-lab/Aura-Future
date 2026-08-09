import streamlit as st

# Page Configuration
st.set_page_config(page_title="Aura Future", page_icon="✨", layout="centered")

# Custom Styling (Red & Black Aura Theme)
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0b0b;
        color: #ffffff;
    }
    .main-title {
        font-size: 38px;
        font-weight: bold;
        color: #ff0033;
        text-align: center;
        text-shadow: 2px 2px 8px rgba(255, 0, 51, 0.6);
        margin-bottom: 0px;
    }
    .subtitle {
        text-align: center;
        color: #cccccc;
        font-size: 16px;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# Header Title with Red & Black Theme
st.markdown('<p class="main-title">AURA AVATAR</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Aura Future - Freelancing & AI Innovation Vision</p>', unsafe_allow_html=True)

# Company & Business Details
COMPANY_INFO = """
Aura Future ek high-end digital storefront aur innovative tech venture hai. 
Hamara vision client ko top-notch freelancing services, AI solutions, aur digital automation provide karna hai. 
Hum quality, speed, aur modern technology par focus karte hain taake har business ko future-ready banaya ja sake.
"""

# Session State for Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for Avatar / Image Upload
with st.sidebar:
    st.markdown("### 🖼️ Upload AI Avatar")
    uploaded_file = st.file_uploader("Apni Avatar pic yahan upload karein", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Aapka AI Avatar", use_column_width=True)
        st.success("Avatar successfully loaded!")

# Main Chat Room Interface
st.markdown("---")
st.subheader("💬 Chat with your AI Avatar")

# Display previous chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input Box
if user_query := st.chat_input("Aura Future ya freelancing ke baray mein kuch bhi poochein..."):
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    # Generate Smart AI Response
    query_lower = user_query.lower()
    if "vision" in query_lower or "company" in query_lower or "aura future" in query_lower:
        bot_response = f"Aura Future ke mutaliq yeh maloomat hain: {COMPANY_INFO}"
    elif "freelance" in query_lower or "services" in query_lower:
        bot_response = "Aura Future par hum professional freelancing services, web development, aur AI automation provide karte hain."
    else:
        bot_response = f"Aapne poocha: '{user_query}'. Main Aura Future ka AI Avatar hoon. {COMPANY_INFO}"

    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    
    with st.chat_message("assistant"):
        st.markdown(bot_response)
        
        # Browser Native Speech (Error-free robot voice)
        safe_response = bot_response.replace('\n', ' ').replace('"', "'")
        speech_html = f"""
        <script>
            var msg = new SpeechSynthesisUtterance("{safe_response}");
            msg.rate = 1.0;
            window.speechSynthesis.speak(msg);
        </script>
        """
        st.components.v1.html(speech_html, height=0)
