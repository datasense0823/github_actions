import streamlit as st
import subprocess
import sys
import time
import webbrowser
import os

# Function to launch Streamlit only once
def launch_streamlit():
    """Launch Streamlit server if not already running and open browser once."""
    url = "http://localhost:8501"

    # Check if Streamlit is already running by looking at active processes
    process_output = subprocess.run(["pgrep", "-f", "streamlit"], capture_output=True, text=True)
    
    if not process_output.stdout.strip():  # If no Streamlit process is found
        subprocess.Popen(
            [sys.executable, "-m", "streamlit", "run", sys.argv[0]], 
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        time.sleep(3)  # Wait for Streamlit to fully start

        # Open the browser only once
        webbrowser.open(url)

# Ensure Streamlit starts only once when running the script
if __name__ == "__main__":
    if "streamlit" not in sys.argv[0]:  # Prevent relaunching inside Streamlit process
        launch_streamlit()

    # Streamlit UI
    st.set_page_config(page_title="Chatbot", page_icon="💬", layout="wide")

    st.title("🤖 Chatbot Interface")
    st.write("Ask me anything!")

    # Maintain chat history in session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        role = "🧑‍💻 You:" if message["role"] == "user" else "🤖 Bot:"
        with st.chat_message(message["role"]):
            st.markdown(f"**{role}** {message['content']}")

    # User input field
    user_input = st.chat_input("Type your message...")

    if user_input:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Dummy chatbot response (Replace this with an AI model)
        bot_response = f"Hello! You said: {user_input}"

        # Add bot response to chat history
        st.session_state.messages.append({"role": "bot", "content": bot_response})

        # Refresh page to show new messages
        st.rerun()
