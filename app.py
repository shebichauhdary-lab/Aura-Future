import streamlit as st

# Page Configuration
st.set_page_config(page_title="Aura Future - AI Avatar", page_icon="✨", layout="centered")

# Custom Styling (Red & Black Theme with Watermark Wallpaper & American Accent Layout)
st.markdown("""
    <style>
    .stApp {
        background-color: #050505;
        background-image: linear-gradient(rgba(5, 5, 5, 0.92), rgba(5, 5, 5, 0.92)), 
                          radial-gradient(circle at center, #1a0003 0%, #050505 80%);
        color: #ffffff;
    }
    
    /* Background Watermark Logo Style Text */
    .stApp::before {
        content: "AURA AI AVATAR";
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 14vw;
        font-weight: 900;
        color: rgba(255, 0, 51, 0.04);
        z-index: 0;
        white-space: nowrap;
        pointer-events: none;
    }

    .main-title {
        font-size: 42px;
        font-weight: bold;
        color: #ff0033;
        text-align: center;
        text-shadow: 0px 0px 15px rgba(255, 0, 51, 0.7);
        margin-bottom: 0px;
        z-index: 1;
    }
    .subtitle {
        text-align: center;
        color: #dddddd;
        font-size: 16px;
        margin-bottom: 25px;
        z-index: 1;
    }
    .chat-container {
        position: relative;
        z-index: 1;
    }
    </style>
""", unsafe_allow_html=True)

# Header Title with Red & Black Theme
st.markdown('<p class="main-title">AURA AI AVATAR</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Aura Future - Global Freelancing & AI Innovation</p>', unsafe_allow_html=True)

# Full Company Details Data Feed
COMPANY_DETAILS = """
Welcome to Aura Future! We are a high-end digital storefront and innovative tech venture. 
- **CEO & Founder:** Shahzaib Chaudhary
- **Team:** Over 100+ professional experts working globally, including top-tier professional video/photo editors and advanced AI developers.
- **Vision & Services:** Our mission is to deliver cutting-edge AI solutions, digital automation, high-end production, and premier freelancing services to empower businesses worldwide and make them future-ready.
"""

# Session State for Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Permanent Fixed AI Avatar for Clients (No Uploader)
with st.sidebar:
    st.markdown("### 🤖 Aura AI Representative")
    # Professional High-End AI / Joker Avatar Image URL
    st.image("https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=500&auto=format&fit=crop", caption="Aura Future Official Avatar", use_container_width=True)
    st.markdown("---")
    st.markdown("**Company Status:** Active 🚀")
    st.markdown("**CEO:** Shahzaib Chaudhary")
    st.markdown("**Workforce:** 100+ Experts")

# Main Chat Room Interface
st.markdown("---")
st.subheader("💬 Chat with Aura AI Avatar")

# Display previous chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message["role"] == "assistant":
            safe_text = message["content"].replace('\n', ' ').replace('"', "'")
            # American Accent Audio Integration via Web Speech API (en-US)
            speech_html = f"""
            <button onclick="
                var msg = new SpeechSynthesisUtterance('{safe_text}');
                msg.lang = 'en-US';
                msg.rate = 1.0;
                window.speechSynthesis.speak(msg);
            " style="background-color: #ff0033; color: white; border: none; padding: 6px 14px; border-radius: 6px; cursor: pointer; font-weight: bold; margin-top: 8px; box-shadow: 0px 0px 10px rgba(255,0,51,0.5);">
                🔊 Listen in American Accent
            </button>
            """
            st.components.v1.html(speech_html, height=50)

# User Input Box
if user_query := st.chat_input("Ask about Aura Future, services, team, or CEO..."):
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    # Smart AI Response Generation based on Details
    query_lower = user_query.lower()
    if any(word in query_lower for word in ["vision", "company", "about", "future", "aura"]):
        bot_response = f"Hello! Here is everything about us: {COMPANY_DETAILS}"
    elif any(word in query_lower for word in ["ceo", "owner", "founder", "shahzaib"]):
        bot_response = "Aura Future is led by our visionary CEO, Mr. Shahzaib Chaudhary, who directs our global operations and strategic growth."
    elif any(word in query_lower for word in ["team", "employees", "staff", "people", "developers", "editors", "100"]):
        bot_response = "Aura Future proudly operates with a robust team of over 100+ professionals, featuring expert AI developers and elite creative video editors."
    elif any(word in query_lower for word in ["service", "freelance", "offer", "work", "solution"]):
        bot_response = "We offer world-class AI solutions, digital automation, custom development, and professional creative editing services for international clients."
    else:
        bot_response = f"Thanks for your query regarding '{user_query}'. As the Aura Future AI Avatar, I'm here to assist you. {COMPANY_DETAILS}"

    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    
    with st.chat_message("assistant"):
        st.markdown(bot_response)
        safe_response = bot_response.replace('\n', ' ').replace('"', "'")
        # American Accent Audio Integration via Web Speech API (en-US)
        speech_html = f"""
        <button onclick="
            var msg = new SpeechSynthesisUtterance('{safe_response}');
            msg.lang = 'en-US';
            msg.rate = 1.0;
            window.speechSynthesis.speak(msg);
        " style="background-color: #ff0033; color: white; border: none; padding: 6px 14px; border-radius: 6px; cursor: pointer; font-weight: bold; margin-top: 8px; box-shadow: 0px 0px 10px rgba(255,0,51,0.5);">
            🔊 Listen in American Accent
        </button>
        """
        st.components.v1.html(speech_html, height=50)
