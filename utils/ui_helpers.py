import streamlit as st
import base64
import re
import time
import random
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.shared import OxmlElement, qn
import io
import os

def convert_markdown_to_html(text):
    """Convert markdown formatting to clean HTML for display"""
    if not text:
        return ""
        
    # Convert headers with proper styling
    text = re.sub(r'^### (.*)', r'<h3 style="color: #5a6fd8; font-size: 18px; margin-top: 25px; margin-bottom: 10px;">\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.*)', r'<h2 style="color: #4c63d2; font-size: 22px; margin-top: 30px; margin-bottom: 15px; border-left: 4px solid #667eea; padding-left: 15px;">\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^# (.*)', r'<h1 style="color: #667eea; font-size: 28px; text-align: center; margin-bottom: 30px; border-bottom: 3px solid #667eea; padding-bottom: 15px;">\1</h1>', text, flags=re.MULTILINE)
    
    # Convert bold text
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong style="color: #4c63d2; font-weight: bold;">\1</strong>', text)
    
    # Convert italic text
    text = re.sub(r'\*(.*?)\*', r'<em style="color: #5a6fd8; font-style: italic;">\1</em>', text)
    
    # Convert bullet points with better styling
    text = re.sub(r'^- (.*)', r'<li style="margin: 8px 0; line-height: 1.6;">\1</li>', text, flags=re.MULTILINE)
    
    # Wrap consecutive list items in styled ul tags
    def replace_list(match):
        return f'<ul style="margin: 15px 0; padding-left: 25px;">\n{match.group(0)}</ul>\n'
    
    text = re.sub(r'(<li[^>]*>.*?</li>\s*)+', replace_list, text, flags=re.DOTALL)
    
    # Convert numbered lists
    text = re.sub(r'^(\d+)\. (.*)', r'<li style="margin: 8px 0; line-height: 1.6;">\2</li>', text, flags=re.MULTILINE)
    
    # Convert line breaks to proper spacing
    text = text.replace('\n\n', '</p><p style="margin: 15px 0; line-height: 1.8;">')
    text = text.replace('\n', '<br>')
    
    # Wrap content in paragraph tags
    if not text.startswith('<'):
        text = f'<p style="margin: 15px 0; line-height: 1.8;">{text}</p>'
    
    # Clean up extra br tags around headers and lists
    text = re.sub(r'<br>\s*(<h[1-3])', r'\1', text)
    text = re.sub(r'(<h[1-3][^>]*>.*?</h[1-3]>)\s*<br>', r'\1', text)
    text = re.sub(r'<br>\s*(<ul)', r'\1', text)
    text = re.sub(r'(</ul>)\s*<br>', r'\1', text)
    
    # Wrap everything in a styled container
    styled_content = f"""
    <div style="
        font-family: 'Times New Roman', Times, serif;
        line-height: 1.8;
        color: #333;
        background-color: #fdfdfd;
        padding: 30px;
        border-radius: 8px;
        border: 1px solid #f0f0f0;
        margin: 20px 0;
    ">
        {text}
    </div>
    """
    
    return styled_content

def simulate_typing_delay(text_length):
    """Simulate natural typing delay based on text length"""
    # Base delay of 2-4 seconds + additional time based on text length
    base_delay = random.uniform(2.0, 4.0)
    length_delay = min(text_length / 50, 6.0)  # Max 6 seconds additional
    total_delay = base_delay + length_delay
    
    # Show typing indicator
    typing_placeholder = st.empty()
    typing_placeholder.markdown("🤔 *Thinking...*")
    time.sleep(total_delay)
    typing_placeholder.empty()

def render_multiple_choice_question(question, options, key):
    """Render a multiple choice question with checkboxes"""
    st.markdown(f"**{question}**")
    
    selected_options = []
    for i, option in enumerate(options):
        if st.checkbox(option, key=f"{key}_{i}"):
            selected_options.append(option)
    
    return selected_options

def format_final_report_display(text):
    """Specifically format final career reports for optimal display"""
    if not text:
        return "No report content available."
    
    # Ensure text is a string
    if isinstance(text, tuple):
        text = str(text[0]) if text else ""
    elif not isinstance(text, str):
        text = str(text)
    
    # Convert markdown to styled HTML with enhanced styling for reports
    formatted_html = convert_markdown_to_html(text)
    
    # Add a special wrapper for final reports
    final_report_html = f"""
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2px;
        border-radius: 12px;
        margin: 20px 0;
    ">
        <div style="
            background: white;
            border-radius: 10px;
            overflow: hidden;
        ">
            <div style="
                background: linear-gradient(90deg, #667eea, #764ba2);
                color: white;
                text-align: center;
                padding: 15px;
                margin-bottom: 0;
            ">
                <h2 style="
                    margin: 0;
                    font-family: 'Times New Roman', serif;
                    font-size: 24px;
                    font-weight: bold;
                ">🚀 Your Career Strategy Report</h2>
            </div>
            {formatted_html}
        </div>
    </div>
    """
    
    return final_report_html

def format_report_for_display(text):
    """Format report text for better display in Streamlit"""
    if not text:
        return ""
        
    # Convert to HTML format for better display
    return convert_markdown_to_html(text)

def generate_pdf_report(report_text, user_details):
    """Generate PDF report"""
    try:
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=1*Inches, bottomMargin=1*Inches)
        
        # Define styles
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            textColor=HexColor('#667eea'),
            alignment=1  # Center alignment
        )
        
        header_style = ParagraphStyle(
            'CustomHeader',
            parent=styles['Heading2'],
            fontSize=16,
            spaceAfter=12,
            spaceBefore=20,
            textColor=HexColor('#4c63d2'),
            leftIndent=0
        )
        
        subheader_style = ParagraphStyle(
            'CustomSubHeader',
            parent=styles['Heading3'],
            fontSize=14,
            spaceAfter=10,
            spaceBefore=15,
            textColor=HexColor('#5a6fd8')
        )
        
        normal_style = ParagraphStyle(
            'CustomNormal',
            parent=styles['Normal'],
            fontSize=12,
            spaceAfter=6,
            fontName='Times-Roman'
        )
        
        # Build the story
        story = []
        
        # Title
        story.append(Paragraph("🚀 Your Personalized Career Strategy Blueprint", title_style))
        story.append(Spacer(1, 12))
        
        # User info
        story.append(Paragraph(f"<b>Prepared for:</b> {user_details.get('name', 'User')}", normal_style))
        story.append(Paragraph(f"<b>Generated by:</b> Remiro AI Career Guidance Assistant", normal_style))
        story.append(Spacer(1, 20))
        
        # Process the report content
        lines = report_text.split('\n')
        for line in lines:
            line = line.strip()
            if not line:
                story.append(Spacer(1, 6))
                continue
                
            if line.startswith('### '):
                story.append(Paragraph(line[4:], subheader_style))
            elif line.startswith('## '):
                story.append(Paragraph(line[3:], header_style))
            elif line.startswith('# '):
                story.append(Paragraph(line[2:], title_style))
            elif line.startswith('- '):
                story.append(Paragraph(f"• {line[2:]}", normal_style))
            else:
                # Clean up any remaining markdown
                clean_line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
                clean_line = re.sub(r'\*(.*?)\*', r'<i>\1</i>', clean_line)
                story.append(Paragraph(clean_line, normal_style))
        
        doc.build(story)
        buffer.seek(0)
        return buffer.getvalue()
        
    except Exception as e:
        st.error(f"Error generating PDF: {str(e)}")
        return None

def generate_docx_report(report_text, user_details):
    """Generate DOCX report"""
    try:
        doc = Document()
        
        # Add title
        title = doc.add_heading('🚀 Your Personalized Career Strategy Blueprint', 0)
        title.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        # Add user info
        doc.add_paragraph()
        user_info = doc.add_paragraph()
        user_info.add_run(f"Prepared for: ").bold = True
        user_info.add_run(user_details.get('name', 'User'))
        
        gen_info = doc.add_paragraph()
        gen_info.add_run("Generated by: ").bold = True
        gen_info.add_run("Remiro AI Career Guidance Assistant")
        
        doc.add_paragraph()
        
        # Process the report content
        lines = report_text.split('\n')
        for line in lines:
            line = line.strip()
            if not line:
                doc.add_paragraph()
                continue
                
            if line.startswith('### '):
                heading = doc.add_heading(line[4:], level=3)
            elif line.startswith('## '):
                heading = doc.add_heading(line[3:], level=2)
            elif line.startswith('# '):
                heading = doc.add_heading(line[2:], level=1)
            elif line.startswith('- '):
                p = doc.add_paragraph()
                p.style = 'List Bullet'
                # Clean up markdown formatting
                clean_text = re.sub(r'\*\*(.*?)\*\*', r'\1', line[2:])
                clean_text = re.sub(r'\*(.*?)\*', r'\1', clean_text)
                p.add_run(clean_text)
            else:
                p = doc.add_paragraph()
                # Clean up markdown formatting and add styled text
                parts = re.split(r'(\*\*.*?\*\*|\*.*?\*)', line)
                for part in parts:
                    if part.startswith('**') and part.endswith('**'):
                        run = p.add_run(part[2:-2])
                        run.bold = True
                    elif part.startswith('*') and part.endswith('*'):
                        run = p.add_run(part[1:-1])
                        run.italic = True
                    else:
                        p.add_run(part)
        
        # Save to buffer
        buffer = io.BytesIO()
        doc.save(buffer)
        buffer.seek(0)
        return buffer.getvalue()
        
    except Exception as e:
        st.error(f"Error generating DOCX: {str(e)}")
        return None
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
            
            # Show typing indicator and simulate natural delay
            typing_placeholder = st.empty()
            typing_placeholder.markdown("🤔 *Analyzing your response...*")
            
            # Process the message with natural timing
            try:
                # Process the message through the master agent
                response_data = master_agent.process_message(prompt, user_details)
                
                # Simulate natural thinking time (5-10 seconds)
                thinking_time = random.uniform(5.0, 10.0)
                time.sleep(thinking_time)
                
                # Clear typing indicator
                typing_placeholder.empty()
                
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
                typing_placeholder.empty()
                st.error(f"An error occurred: {str(e)}")
                response = "I apologize for the error. Please try rephrasing your response."
                is_complete = False
                results = None
                
                # Display the response with proper formatting
                if master_agent.final_report_generated:
                    # This is the final report - display as formatted HTML
                    formatted_html = format_final_report_display(response)
                    response_placeholder.markdown(formatted_html, unsafe_allow_html=True)
                else:
                    # Regular agent responses - display as markdown
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
    
    # Convert markdown to clean HTML
    formatted_content = convert_markdown_to_html(report_text)
    
    report_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Career Guidance Report</title>
        <style>
            body {{
                font-family: "Times New Roman", Times, serif;
                line-height: 1.8;
                color: #333;
                max-width: 900px;
                margin: 0 auto;
                padding: 40px;
                background-color: #fff;
            }}
            
            h1 {{
                color: #667eea;
                font-size: 28px;
                text-align: center;
                margin-bottom: 30px;
                border-bottom: 3px solid #667eea;
                padding-bottom: 15px;
            }}
            
            h2 {{
                color: #4c63d2;
                font-size: 22px;
                margin-top: 30px;
                margin-bottom: 15px;
                border-left: 4px solid #667eea;
                padding-left: 15px;
            }}
            
            h3 {{
                color: #5a6fd8;
                font-size: 18px;
                margin-top: 25px;
                margin-bottom: 10px;
            }}
            
            ul {{
                margin: 15px 0;
                padding-left: 25px;
            }}
            
            li {{
                margin: 8px 0;
                line-height: 1.6;
            }}
            
            .header-info {{
                text-align: center;
                background-color: #f8f9ff;
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 30px;
                border: 1px solid #e0e6ff;
            }}
            
            .footer {{
                text-align: center;
                margin-top: 40px;
                padding-top: 20px;
                border-top: 2px solid #e0e6ff;
                font-style: italic;
                color: #666;
            }}
            
            strong {{
                color: #4c63d2;
                font-weight: bold;
            }}
            
            em {{
                color: #5a6fd8;
                font-style: italic;
            }}
            
            .content {{
                background-color: #fdfdfd;
                padding: 30px;
                border-radius: 8px;
                border: 1px solid #f0f0f0;
            }}
        </style>
    </head>
    <body>
        <div class="header-info">
            <h1>🚀 Your Personalized Career Strategy Blueprint</h1>
            <p><strong>Prepared for:</strong> {user_details.get('name', 'User')}</p>
            <p><strong>Date:</strong> {st.session_state.get('current_date', 'Today')}</p>
        </div>
        
        <div class="content">
            {formatted_content}
        </div>
        
        <div class="footer">
            <p><em>Generated by Remiro AI Career Guidance Assistant</em></p>
            <p><em>Your AI-Powered Career Companion</em></p>
        </div>
    </body>
    </html>
    """
    
    # Create download buttons for multiple formats
    st.markdown("---")
    st.markdown("### 📥 Download Your Career Report")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # HTML Download
        b64_html = base64.b64encode(report_html.encode()).decode()
        href_html = f'<a href="data:text/html;base64,{b64_html}" download="career_report.html" style="text-decoration: none;"><div style="background-color: #667eea; color: white; padding: 10px 20px; border-radius: 5px; text-align: center; margin: 5px;">📄 HTML Report</div></a>'
        st.markdown(href_html, unsafe_allow_html=True)
    
    with col2:
        # PDF Download
        pdf_data = generate_pdf_report(report_text, user_details)
        if pdf_data:
            b64_pdf = base64.b64encode(pdf_data).decode()
            href_pdf = f'<a href="data:application/pdf;base64,{b64_pdf}" download="career_report.pdf" style="text-decoration: none;"><div style="background-color: #dc3545; color: white; padding: 10px 20px; border-radius: 5px; text-align: center; margin: 5px;">� PDF Report</div></a>'
            st.markdown(href_pdf, unsafe_allow_html=True)
        else:
            st.error("PDF generation failed")
    
    with col3:
        # DOCX Download
        docx_data = generate_docx_report(report_text, user_details)
        if docx_data:
            b64_docx = base64.b64encode(docx_data).decode()
            href_docx = f'<a href="data:application/vnd.openxmlformats-officedocument.wordprocessingml.document;base64,{b64_docx}" download="career_report.docx" style="text-decoration: none;"><div style="background-color: #28a745; color: white; padding: 10px 20px; border-radius: 5px; text-align: center; margin: 5px;">📝 Word Document</div></a>'
            st.markdown(href_docx, unsafe_allow_html=True)
        else:
            st.error("DOCX generation failed")
    
    st.markdown("Choose your preferred format to download your personalized career report!")

def display_agent_complete_badge(agent_name):
    """Display completion badge for an agent"""
    st.markdown(f"✅ **{agent_name} Analysis Complete**")