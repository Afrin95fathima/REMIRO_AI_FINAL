import streamlit as st
import base64
import json

def setup_page_config(title):
    """Setup page configuration"""
    st.set_page_config(
        page_title=title,
        page_icon="🧭",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Apply simple, clean CSS with Times New Roman font
    st.markdown("""
        <style>
            /* Main app styling */
            .stApp {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
                font-family: "Times New Roman", Times, serif !important;
            }
            
            /* Main content area - simplified */
            .main .block-container {
                background-color: #ffffff !important;
                border-radius: 15px !important;
                padding: 2rem !important;
                margin: 1rem !important;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1) !important;
            }
            
            /* Headers */
            h1, h2, h3, h4, h5, h6 {
                font-family: "Times New Roman", Times, serif !important;
                color: #2d3748 !important;
                font-weight: 600 !important;
                margin: 1rem 0 !important;
            }
            
            h1 {
                text-align: center !important;
                color: #667eea !important;
                font-size: 2.5rem !important;
            }
            
            /* All text elements */
            .stApp *, p, div, span, label, input, select, textarea {
                font-family: "Times New Roman", Times, serif !important;
                color: #2d3748 !important;
            }
            
            /* Form elements - simple and clean */
            .stTextInput input, .stSelectbox select, .stNumberInput input, .stTextArea textarea {
                background-color: #ffffff !important;
                border: 2px solid #e2e8f0 !important;
                border-radius: 8px !important;
                padding: 12px !important;
                color: #2d3748 !important;
                font-size: 16px !important;
                font-family: "Times New Roman", Times, serif !important;
            }
            
            .stTextInput input:focus, .stSelectbox select:focus, .stNumberInput input:focus, .stTextArea textarea:focus {
                border-color: #667eea !important;
                box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2) !important;
                outline: none !important;
            }
            
            /* Buttons */
            .stButton button {
                background-color: #667eea !important;
                color: white !important;
                border: none !important;
                border-radius: 8px !important;
                padding: 12px 24px !important;
                font-family: "Times New Roman", Times, serif !important;
                font-weight: 600 !important;
                font-size: 16px !important;
            }
            
            .stButton button:hover {
                background-color: #5a67d8 !important;
            }
            
            /* Slider styling */
            .stSlider > div {
                padding: 1rem 0 !important;
            }
            
            .stSlider [data-testid="stThumbValue"] {
                background-color: #667eea !important;
                border-color: #667eea !important;
                color: white !important;
                font-family: "Times New Roman", Times, serif !important;
            }
            
            /* Chat messages */
            .stChatMessage {
                background-color: #f7fafc !important;
                border-radius: 10px !important;
                padding: 1rem !important;
                margin: 1rem 0 !important;
                border-left: 4px solid #667eea !important;
            }
            
            /* Sidebar */
            .css-1d391kg {
                background: linear-gradient(135deg, #667eea, #764ba2) !important;
                color: white !important;
                padding: 1rem !important;
            }
            
            .css-1d391kg h1, .css-1d391kg h2, .css-1d391kg h3 {
                color: white !important;
                font-family: "Times New Roman", Times, serif !important;
            }
            
            .css-1d391kg p, .css-1d391kg div {
                color: white !important;
                font-family: "Times New Roman", Times, serif !important;
            }
            
            /* Remove extra styling for simplicity */
            .stMarkdown {
                font-family: "Times New Roman", Times, serif !important;
            }
            
            /* Ensure all elements use Times New Roman */
            * {
                font-family: "Times New Roman", Times, serif !important;
            }
        </style>
    """, unsafe_allow_html=True)

def render_moving_background():
    """Simple background - no complex animations"""
    pass

def render_chat_interface(master_agent, user_details):
    """Render the simplified chat interface"""
    
    # Initialize current agent state if not present
    if "current_agent_name" not in st.session_state:
        current_agent = master_agent.get_current_agent()
        if current_agent:
            st.session_state.current_agent_name = master_agent.agent_sequence[master_agent.current_agent_index]
        else:
            st.session_state.current_agent_name = "master"
    
    # Show current agent indicator - simplified
    current_agent_name = st.session_state.current_agent_name.replace("_", " ").title()
    
    if master_agent.final_integration_started:
        st.markdown("### 🧠 **Creating Your Career Strategy**")
    else:
        st.markdown(f"### 👤 **Current Focus:** {current_agent_name} Analysis")
    
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # React to user input
    if prompt := st.chat_input("Type your response here..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            
            # Process the message with a spinner
            with st.spinner("Analyzing your response..."):
                try:
                    # Process the message through the master agent
                    response_data = master_agent.process_message(prompt, user_details)
                    
                    # Check response structure
                    if isinstance(response_data, tuple):
                        if len(response_data) == 2:
                            response, is_complete = response_data
                            results = None
                        elif len(response_data) == 3:
                            response, is_complete, results = response_data
                        else:
                            response = str(response_data)
                            is_complete = False
                            results = None
                    else:
                        response = str(response_data)
                        is_complete = False
                        results = None
                        
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
                    response = "I apologize for the error. Please try rephrasing your response."
                    is_complete = False
                    results = None
                
                # Display the response
                response_placeholder.markdown(response)
                
                # Add response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})
                
                # If agent has completed its part, move to the next agent
                if is_complete:
                    if results and not master_agent.final_integration_started:
                        # Move to next agent
                        next_agent = master_agent.move_to_next_agent()
                        
                        if next_agent:
                            # Update current agent name
                            st.session_state.current_agent_name = master_agent.agent_sequence[master_agent.current_agent_index]
                            
                            # Add transition message
                            transition_msg = f"Great! Now let's move to the **{st.session_state.current_agent_name.replace('_', ' ').title()}** analysis."
                            
                            # Add the transition message
                            st.markdown(transition_msg)
                            st.session_state.messages.append({"role": "assistant", "content": transition_msg})
                            
                        else:
                            # We've gone through all agents, moving to final integration
                            st.session_state.current_agent_name = "master"
                            st.markdown("Now I'll create your personalized career guidance report.")
                    
                    # If this is the final response, display download button
                    if master_agent.final_report_generated:
                        # Ensure response is a string for the download function
                        if isinstance(response, tuple):
                            report_text = str(response[0]) if response else "No report generated"
                        else:
                            report_text = str(response) if response else "No report generated"
                        offer_report_download(report_text, user_details)

def offer_report_download(report_text, user_details):
    """Offer a download button for the career report"""
    
    # Ensure report_text is a string
    if isinstance(report_text, tuple):
        report_text = str(report_text[0]) if report_text else "No report generated"
    elif not isinstance(report_text, str):
        report_text = str(report_text) if report_text else "No report generated"
    
    report_html = f"""
    <html>
    <head>
        <title>Career Guidance Report</title>
        <style>
            body {{
                font-family: "Times New Roman", Times, serif;
                line-height: 1.6;
                color: #333;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
            }}
            h1, h2, h3 {{
                color: #667eea;
                font-family: "Times New Roman", Times, serif;
            }}
        </style>
    </head>
    <body>
        <h1>Your Personalized Career Guidance Report</h1>
        <p><strong>For:</strong> {user_details.get('name', 'User')}</p>
        <div>{report_text.replace('\n', '<br>')}</div>
        <footer>
            <p><em>Remiro AI Career Guidance Assistant</em></p>
        </footer>
    </body>
    </html>
    """
    
    # Create download button for HTML report
    b64_report = base64.b64encode(report_html.encode()).decode()
    href = f'<a href="data:text/html;base64,{b64_report}" download="career_report.html">📄 Download Your Career Report</a>'
    st.markdown(href, unsafe_allow_html=True)

def display_agent_complete_badge(agent_name):
    """Display completion badge for an agent"""
    st.markdown(f"✅ **{agent_name} Analysis Complete**")