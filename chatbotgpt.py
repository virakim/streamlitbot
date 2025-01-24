import streamlit as st
from openai import OpenAI

st.title("ChatGPT-like clone")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Set a default model (using selectbox for user choice)
model_choice = st.selectbox(
    "Choose GPT Model",
    ["gpt-3.5-turbo", "gpt-3.5-turbo-instruct", "gpt-3.5-turbo-1106", "gpt-3.5-turbo-0125"]
)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = model_choice

# Set a slider for max tokens (from 0 to 500)
max_tokens = st.slider("Max Tokens", min_value=0, max_value=500, value=200)

# Store max_tokens in session state
if "max_tokens" not in st.session_state:
    st.session_state["max_tokens"] = max_tokens

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Say something..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
