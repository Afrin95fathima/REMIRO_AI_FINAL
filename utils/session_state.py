import streamlit as st

def get_session_state():
    """Initialize and return session state variables"""
    
    # Initialize messages if they don't exist
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    return st.session_state