import streamlit as st
import os
import json
from datetime import datetime
from utils.session_state import get_session_state
from utils.ui_helpers import setup_page_config, render_chat_interface, render_moving_background, display_agent_complete_badge
from agents.master_agent import MasterAgent

# Gemini API key
GEMINI_API_KEY = "AIzaSyBJO45DfjO2BvOLvVTZKwyAfxLzqUycWjs"

# Setup page configuration
setup_page_config("Remiro AI - Career Guidance Platform")

# Initialize session state if needed
session_state = get_session_state()

    # Initialize Master Agent with Gemini API key
if "master_agent" not in st.session_state:
    try:
        st.session_state.master_agent = MasterAgent(api_key=GEMINI_API_KEY)
    except Exception as e:
        st.error(f"Failed to initialize the AI system: {str(e)}")
        st.info("Using fallback mode without AI capabilities. Some features may be limited.")
        st.session_state.master_agent = MasterAgent()  # Initialize without API key as fallback

# Render moving background with wine and white gradient theme
render_moving_background()

# Application title - simplified
st.markdown("# Remiro AI - Your Career Guidance Assistant")

# Main application logic
def main():
    # Create simplified sidebar
    with st.sidebar:
        st.markdown("## 🧭 Remiro AI")
        st.markdown("### Career Guidance Assistant")
        
        if "user_details" in st.session_state:
            st.markdown("---")
            st.markdown("## 👤 Your Profile")
            user_details = st.session_state.user_details
            st.markdown(f"**Name:** {user_details.get('name', 'Anonymous')}")
            st.markdown(f"**Experience:** {user_details.get('years_experience', 0)} years")
            
            # Simple progress tracking
            if hasattr(st.session_state.master_agent, 'agent_results'):
                completed_agents = len(st.session_state.master_agent.agent_results)
                total_agents = len(st.session_state.master_agent.agent_sequence)
                
                st.markdown("---")
                st.markdown("## 📊 Progress")
                st.progress(completed_agents / total_agents if total_agents > 0 else 0)
                st.markdown(f"**Completed:** {completed_agents}/{total_agents}")
            
            st.markdown("---")
            if st.button("🔄 New Session", type="secondary"):
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.rerun()
    
    # Check if user has given consent
    if "consent_given" not in st.session_state:
        st.session_state.consent_given = False
        
    if not st.session_state.consent_given:
        # Simple consent form
        st.markdown("## Privacy & Consent")
        st.markdown("""
        To provide personalized career guidance, I need to collect some information about you.
        This information will be used only for providing career advice and will be kept secure.
        """)
        
        consent = st.checkbox("I agree to provide my information for career guidance purposes.")
        
        if st.button("Start Career Analysis", type="primary"):
            if consent:
                st.session_state.consent_given = True
                st.session_state.messages = []
                st.rerun()
            else:
                st.error("Please provide consent to continue.")
    else:
        # If basic details not collected, collect them simply
        if "user_details" not in st.session_state:
            st.markdown("### Tell Me About Yourself")
            
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Your Name")
                age = st.number_input("Age", min_value=16, max_value=100, step=1, value=25)
            
            with col2:
                education_level = st.selectbox(
                    "Education Level",
                    ["High School", "Bachelor's Degree", "Master's Degree", "PhD", "Other"]
                )
                years_experience = st.slider(
                    "Years of Experience",
                    min_value=0, max_value=40, value=2, step=1
                )
            
            session_focus = st.multiselect(
                "What are your main career concerns? (Select up to 3)",
                ["Career Change", "Skill Development", "Job Search", "Advancement", 
                 "Work-Life Balance", "Purpose & Meaning", "Salary Growth"],
                max_selections=3
            )
            
            if st.button("Start My Career Analysis", type="primary"):
                if name and age:
                    # Store details
                    st.session_state.user_details = {
                        "name": name,
                        "age": age,
                        "education_level": education_level,
                        "years_experience": years_experience,
                        "session_focus": session_focus,
                        "user_id": f"{name.lower().replace(' ', '_')}_{hash(name) % 10000}"
                    }
                    st.session_state.messages = []
                    
                    # Initialize with welcome message
                    welcome_message = st.session_state.master_agent.get_welcome_message(name, "comprehensive")
                    st.session_state.messages.append({"role": "assistant", "content": welcome_message})
                    
                    st.rerun()
                else:
                    st.error("Please provide your name and age.")
        else:
            # Display the chat interface for the main interaction
            render_chat_interface(
                st.session_state.master_agent,
                st.session_state.user_details
            )

if __name__ == "__main__":
    main()