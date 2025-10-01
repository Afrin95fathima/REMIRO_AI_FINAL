
import streamlit as st
import time
import json
import os
import google.generativeai as genai
from datetime import datetime
from PIL import Image
import io

# Import all specialized agents
from agents.skills_agent import SkillsAgent
from agents.values_agent import ValuesAgent
from agents.financial_agent import FinancialAgent
from agents.learning_agent import LearningAgent
from agents.personality_agent import PersonalityAgent
from agents.interests_agent import InterestsAgent
from agents.work_environment_agent import WorkEnvironmentAgent
from agents.industry_agent import IndustryAgent
from agents.career_trajectory_agent import CareerTrajectoryAgent
from agents.purpose_agent import PurposeAgent
from agents.aspirations_agent import AspirationsAgent
from agents.network_agent import NetworkAgent
from agents.role_fit_agent import RoleFitAgent
from agents.identity_agent import IdentityAgent
from agents.career_roadmap_agent import CareerRoadmapAgent
from utils.news_service import get_career_news

class MasterAgent:
    """
    Master Agent - Career Strategy Orchestrator
    Coordinates specialized agents to create holistic career guidance
    """
    
    def __init__(self, api_key=None):
        # Configure the Gemini API if key is provided
        if api_key:
            try:
                genai.configure(api_key=api_key)
                
                # Set up the model
                generation_config = {
                    "temperature": 0.8,
                    "top_p": 0.95,
                    "top_k": 64,
                    "max_output_tokens": 8192,
                }
                
                safety_settings = [
                    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                ]
                
                self.model = genai.GenerativeModel(
                    model_name="gemini-1.5-pro",
                    generation_config=generation_config,
                    safety_settings=safety_settings
                )
                self.api_initialized = True
            except Exception as e:
                print(f"Error initializing Gemini API: {str(e)}")
                self.api_initialized = False
        else:
            self.api_initialized = False
        
        # Initialize all specialized agents with comprehensive error handling
        self.agents = {}
        try:
            # Core foundational agents
            self.agents["skills"] = SkillsAgent()
            self.agents["values"] = ValuesAgent()
            self.agents["personality"] = PersonalityAgent()
            self.agents["interests"] = InterestsAgent()
            
            # Career strategy agents
            self.agents["financial"] = FinancialAgent()
            self.agents["learning"] = LearningAgent()
            self.agents["work_environment"] = WorkEnvironmentAgent()
            self.agents["industry"] = IndustryAgent()
            
            # Advanced planning agents
            self.agents["career_trajectory"] = CareerTrajectoryAgent()
            self.agents["purpose"] = PurposeAgent()
            self.agents["aspirations"] = AspirationsAgent()
            self.agents["role_fit"] = RoleFitAgent()
            
            # Integration and networking agents
            self.agents["network"] = NetworkAgent()
            self.agents["identity"] = IdentityAgent()
            self.agents["career_roadmap"] = CareerRoadmapAgent()
            
        except Exception as e:
            print(f"Error initializing agents: {str(e)}")
            # Ensure at least the core agents are available as fallback
            if "skills" not in self.agents:
                self.agents["skills"] = SkillsAgent()
            if "values" not in self.agents:
                self.agents["values"] = ValuesAgent()
            if "financial" not in self.agents:
                self.agents["financial"] = FinancialAgent()
            if "learning" not in self.agents:
                self.agents["learning"] = LearningAgent()
        
        # Define the comprehensive agent sequence (logical order for career analysis)
        self.agent_sequence = [
            # Phase 1: Self-Discovery (Foundation)
            "skills",           # What can you do?
            "values",           # What matters to you?
            "personality",      # How do you work best?
            "interests",        # What excites you?
            
            # Phase 2: Career Strategy (Direction)
            "purpose",          # Why do you work?
            "aspirations",      # Where do you want to go?
            "industry",         # Which fields align with you?
            "work_environment", # What setting suits you?
            
            # Phase 3: Practical Planning (Implementation)
            "financial",        # What are your financial needs?
            "learning",         # How will you develop?
            "career_trajectory",# What's your path?
            "role_fit",         # What roles match you?
            
            # Phase 4: Integration (Action)
            "network",          # Who will help you?
            "identity",         # How do you present yourself?
            "career_roadmap"    # What's your action plan?
        ]
        
        # Initialize agent results storage
        self.agent_results = {}
        
        # Initialize current agent index
        self.current_agent_index = 0
        
        # Context awareness and session management
        self.conversation_context = {}  # Store all user responses for context awareness
        self.session_preferences = {}  # Store user session preferences
        
        # Agent sequence based on session type
        self.full_agent_sequence = [
            "skills", "values", "personality", "interests", "purpose", "aspirations",
            "work_environment", "industry", "financial", "learning", "career_trajectory",
            "network", "role_fit", "identity", "career_roadmap"
        ]
        
        # Adjusted sequences for different session types
        self.session_sequences = {
            "quick": ["skills", "values", "financial", "career_roadmap"],
            "standard": ["skills", "values", "personality", "interests", "financial", "learning", "career_trajectory", "career_roadmap"],
            "deep": ["skills", "values", "personality", "interests", "purpose", "work_environment", "financial", "learning", "career_trajectory", "network", "career_roadmap"],
            "extended": self.full_agent_sequence
        }
        
        # Initialize conversation state
        self.conversation = []
        
        # Flag to indicate if we've moved to final integration
        self.final_integration_started = False
        
        # Flag to track final report generation
        self.final_report_generated = False
        
        # Initialize user data
        self.user_data = {}
    
    def set_session_preferences(self, user_details):
        """Set session preferences and adjust agent sequence accordingly"""
        self.session_preferences = user_details
        session_type = user_details.get("session_type", "standard")
        
        # Set agent sequence based on session type
        self.agent_sequence = self.session_sequences.get(session_type, self.session_sequences["standard"])
        
        # Store user context for agent awareness
        self.conversation_context.update({
            "user_profile": {
                "name": user_details.get("name", ""),
                "age": user_details.get("age", ""),
                "education_level": user_details.get("education_level", ""),
                "years_experience": user_details.get("years_experience", 0),
                "session_focus": user_details.get("session_focus", []),
                "session_duration": user_details.get("session_duration", "")
            }
        })
        
        # Pass context to all agents
        for agent in self.agents.values():
            if hasattr(agent, 'set_context'):
                agent.set_context(self.conversation_context)
    
    def get_welcome_message(self, name, session_type):
        """Generate a welcome message with career news"""
        news_items = get_career_news()
        news_text = ""
        
        # Include 1-2 news items depending on session type
        if news_items:
            news_text = "\n\n**📰 Recent Career News:**\n"
            news_count = 1 if session_type == "quick" else 2
            
            for i, news in enumerate(news_items[:news_count]):
                news_text += f"- **{news['title']}**: {news['summary']}\n"
        
        session_descriptions = {
            "quick": "focused assessment",
            "standard": "comprehensive analysis", 
            "deep": "in-depth exploration",
            "extended": "complete career assessment"
        }
        
        session_description = session_descriptions.get(session_type, "personalized assessment")
        
        # Get the first agent and its introduction
        first_agent = self.get_current_agent()
        if first_agent and hasattr(first_agent, 'get_introduction'):
            agent_intro = first_agent.get_introduction()
        else:
            agent_intro = "Let's begin with understanding your skills and competencies."
        
        message = f"""# Welcome to Remiro AI, {name}! 🎯

I'm your **Career Strategy Orchestrator**, and I'll guide you through a {session_description} using {len(self.agent_sequence)} specialized agents.

{news_text}

This interactive process will help you build an integrated career strategy through conversations with specialized agents focused on:

🛠️ **Skills & Competencies** - Your abilities and development areas
💎 **Values & Principles** - What matters most to you in work  
💰 **Financial Strategy** - Your compensation and benefits priorities
📚 **Learning & Development** - How you grow and learn best

We'll complete a **{session_type}** analysis that matches your available time.

---

{agent_intro}

**To get started, simply type your answer or follow the instructions I provide!**"""
        
        return message
    
    def get_introduction(self):
        """Get the master agent's introduction"""
        return f"""
        # Welcome to Remiro AI - Your Career Strategy Partner
        
        I'm your **Career Strategy Orchestrator**, and I'll guide you through a comprehensive
        career analysis using Remiro AI's advanced 16-agent system.
        
        ## 🚀 Your Comprehensive Career Journey
        
        This interactive process will help you build an integrated career strategy through 
        conversations with 16 specialized agents, each focused on a different aspect of your
        professional life and development.
        
        ### 📋 Our 4-Phase Analysis:
        
        **Phase 1: Self-Discovery** (4 agents)
        - Skills & Competencies Assessment
        - Personal Values Analysis  
        - Personality & Work Style Evaluation
        - Interests & Passion Mapping
        
        **Phase 2: Career Strategy** (4 agents)
        - Life Purpose & Meaning
        - Career Aspirations & Goals
        - Industry & Market Analysis
        - Work Environment Preferences
        
        **Phase 3: Practical Planning** (4 agents)
        - Financial Strategy & Goals
        - Learning & Development Path
        - Career Trajectory Planning
        - Role Fit & Compatibility
        
        **Phase 4: Integration** (4 agents)
        - Professional Networking Strategy
        - Identity & Personal Branding
        - Comprehensive Career Roadmap
        - Final Integration & Action Plan
        
        We'll start with understanding your foundational skills and competencies, then systematically
        work through each dimension to create your personalized career blueprint.
        
        Let's begin your comprehensive career transformation!
        """
    
    def get_current_agent(self):
        """Get the current specialized agent in the sequence"""
        if self.current_agent_index < len(self.agent_sequence):
            return self.agents[self.agent_sequence[self.current_agent_index]]
        return None
    
    def move_to_next_agent(self):
        """Move to the next specialized agent in the sequence"""
        self.current_agent_index += 1
        if self.current_agent_index < len(self.agent_sequence):
            return self.agents[self.agent_sequence[self.current_agent_index]]
        else:
            self.final_integration_started = True
            return None
    
    def process_message(self, message, user_details=None):
        """
        Process a user message using the current specialized agent
        If agent_results is provided, it means we're transitioning between agents
        """
        # First, check if this is a special request or interruption
        if user_details and self._is_interruption(message):
            response = self._handle_interruption(message)
            return response, False
        
        # If we've completed all specialized agents, generate the final integration
        if self.final_integration_started:
            # Generate final career strategy if not already done
            if not self.final_report_generated:
                final_report = self._generate_integrated_strategy()
                self.final_report_generated = True
                return final_report, True
            else:
                # Handle follow-up questions after the final report
                response = self._generate_follow_up_response(message)
                return response, True
        
        # Get current agent - if none, we should start with first question from first agent
        current_agent = self.get_current_agent()
        if not current_agent:
            return "All agents have completed their analysis. Generating your integrated career strategy...", True
        
        # For the very first message, automatically present the first question
        if len(self.conversation) == 0:
            try:
                first_question = current_agent._format_question(current_agent.questions[0])
                self.conversation.append(("user", message))
                self.conversation.append(("agent", first_question))
                return first_question, False, None
            except Exception as e:
                print(f"Error formatting first question: {str(e)}")
                # Fallback to a generic question
                fallback_question = """
                # 🛠️ Skills & Competency Assessment
                
                ## 💭 What are your strongest technical or specialized skills?
                
                **Select all that apply to you:**
                
                - Programming/Software Development
                - Data Analysis & Analytics
                - Digital Marketing & SEO
                - Project Management
                - Financial Analysis
                - Design & Creative Skills
                - Research & Analysis
                - Engineering & Technical
                - Sales & Business Development
                - Operations & Process Improvement
                
                **Or describe your own skills:**
                """
                self.conversation.append(("user", message))
                self.conversation.append(("agent", fallback_question))
                return fallback_question, False, None
        
        # Otherwise, process with the current specialized agent
        try:
            agent_response = current_agent.process_message(message)
            
            # Handle different return formats from agents
            if isinstance(agent_response, tuple):
                if len(agent_response) == 2:
                    response, is_complete = agent_response
                    results = None
                elif len(agent_response) == 3:
                    response, is_complete, results = agent_response
                else:
                    # Unexpected tuple format
                    response = str(agent_response[0]) if len(agent_response) > 0 else "Processing your response..."
                    is_complete = False
                    results = None
            else:
                # Agent returned just a string
                response = str(agent_response)
                is_complete = False
                results = None
                
        except Exception as e:
            print(f"Error processing agent response: {str(e)}")
            response = "I'm processing your response. Please continue with the next question."
            is_complete = False
            results = None
        
        # Store conversation
        self.conversation.append(("user", message))
        self.conversation.append(("agent", response))
        
        # If agent completed their analysis, store the results
        if is_complete and results:
            agent_name = self.agent_sequence[self.current_agent_index]
            self.agent_results[agent_name] = results
            
            # Save the user data if details are provided
            if user_details:
                self._save_user_data(user_details)
        
        return response, is_complete, results
    
    def _is_interruption(self, message):
        """Check if the message is an interruption or special request"""
        # Check for keywords that suggest interruption
        interruption_keywords = [
            "visa", "h1b", "news", "immigration", "salary", "industry", 
            "trends", "statistics", "unrelated", "different topic"
        ]
        
        message_lower = message.lower()
        return any(keyword in message_lower for keyword in interruption_keywords)
    
    def _handle_interruption(self, message):
        """Handle interruptions with informative responses"""
        message_lower = message.lower()
        
        if "visa" in message_lower or "h1b" in message_lower or "immigration" in message_lower:
            return """
            **H1B Visa & Immigration Information**
            
            While I'm not a legal advisor, I can share that work visas like the H1B are employer-sponsored visas for 
            specialized occupations. Requirements typically include:
            - Bachelor's degree or equivalent
            - Job offer in a specialized field
            - Employer willing to sponsor
            
            The process is competitive with an annual cap. For your specific situation, I'd recommend consulting an 
            immigration attorney.
            
            Would you like to continue with your career guidance session now?
            """
        
        elif "salary" in message_lower or "pay" in message_lower:
            return """
            **Salary Information**
            
            Salary ranges vary widely by industry, location, experience level, and specific role. 
            For accurate information, I recommend checking resources like:
            - Glassdoor.com
            - Payscale.com
            - Bureau of Labor Statistics
            
            Would you prefer to discuss salary expectations for specific roles, or shall we continue 
            with your career assessment?
            """
        
        elif "news" in message_lower or "trends" in message_lower:
            news_items = get_career_news()
            news_text = "**Recent Career & Job Market News**\n\n"
            
            if news_items:
                for i, news in enumerate(news_items[:3]):
                    news_text += f"- **{news['title']}**: {news['summary']}\n\n"
            else:
                news_text += "I don't have the latest news at the moment. For current trends, you might want to check resources like LinkedIn News or industry publications.\n\n"
                
            news_text += "Would you like to continue with your career guidance session now?"
            return news_text
        
        else:
            return """
            I notice you're asking about a topic outside our current assessment. I'm happy to help with 
            career-related questions, but to provide you with the most personalized guidance, I recommend 
            we complete your assessment first.
            
            Would you like to continue with the current assessment, or is there a specific career question 
            I can help with?
            """
    
    def _generate_integrated_strategy(self):
        """Generate an integrated career strategy based on all agent results"""
        
        # Use the basic integration approach for reliability
        return self._generate_basic_integrated_strategy()
    
    def _generate_basic_integrated_strategy(self):
        """Generate a basic integrated strategy without using Gemini API"""
        strategy = """
        # 🚀 Your Personalized Career Strategy Blueprint
        
        ## 📊 Executive Summary
        
        Based on our comprehensive assessment across 12 dimensions of your career profile, we've identified these key strategic insights:
        
        - Your unique combination of skills and values suggests you would thrive in roles that balance technical expertise with meaningful impact
        - Financial considerations and learning preferences indicate a need for structured growth with clear advancement paths
        - Your work environment preferences and purpose drivers point toward collaborative cultures with mission-driven focus
        
        ## 🧩 Your Integrated Career Profile
        
        ### 💪 Core Strengths & Values
        """
        
        # Add skills insights if available
        if "skills" in self.agent_results:
            skills_data = self.agent_results["skills"]
            strategy += "\n#### Key Skills & Competencies\n"
            for skill in skills_data.get("core_skills", ["Skills analysis not completed"])[:3]:
                strategy += f"- {skill}\n"
        
        # Add values insights if available
        if "values" in self.agent_results:
            values_data = self.agent_results["values"]
            strategy += "\n#### Core Values\n"
            for value in values_data.get("core_values", ["Values analysis not completed"])[:3]:
                strategy += f"- {value}\n"
        
        # Add purpose insights if available
        if "purpose" in self.agent_results:
            purpose_data = self.agent_results["purpose"]
            strategy += "\n#### Purpose Drivers\n"
            theme = purpose_data.get("primary_purpose_theme", "Purpose analysis not completed")
            strategy += f"- Primary Purpose Theme: {theme}\n"
            
            for activity in purpose_data.get("meaningful_activities", [])[:2]:
                strategy += f"- Finds meaning in: {activity}\n"
        
        strategy += """
        
        ## 🎯 Strategic Career Opportunities
        
        Based on your integrated profile, here are personalized career recommendations:
        """
        
        # Generate recommendations based on our 4 core agents
        if "skills" in self.agent_results:
            skills_data = self.agent_results["skills"]
            strategy += f"\n### 💼 Recommended Career Paths\n"
            strategy += f"Based on your technical skills, consider roles in:\n"
            for skill in skills_data.get("technical_skills", [])[:3]:
                strategy += f"- Positions that leverage **{skill}**\n"
        
        if "values" in self.agent_results:
            values_data = self.agent_results["values"]
            strategy += f"\n### 🌟 Values-Aligned Opportunities\n"
            strategy += f"Look for organizations and roles that offer:\n"
            for value in values_data.get("core_values", [])[:3]:
                strategy += f"- **{value}**\n"
        
        if "financial" in self.agent_results:
            financial_data = self.agent_results["financial"]
            strategy += f"\n### 💰 Financial Strategy\n"
            strategy += f"Focus on opportunities that provide:\n"
            for priority in financial_data.get("financial_priorities", [])[:3]:
                strategy += f"- **{priority}**\n"
        
        if "learning" in self.agent_results:
            learning_data = self.agent_results["learning"]
            strategy += f"\n### 📚 Development-Friendly Environments\n"
            strategy += f"Seek roles and companies that support:\n"
            for method in learning_data.get("learning_methods", [])[:3]:
                strategy += f"- **{method}**\n"
        
        # Add development roadmap
        strategy += """
        
        ## 🗺️ Your Strategic Development Roadmap
        
        To move effectively toward these high-potential opportunities, follow this customized, phased approach:
        
        ### 🚦 Immediate Next Steps (1-3 months)
        - **Network Building**: Conduct targeted networking with professionals in your target industries
        - **Skill Development**: Address key skill gaps through online courses or projects
        - **Brand Alignment**: Update your professional brand to align with your target direction
        
        ### 🌱 Near-term Focus (3-12 months)
        - **Credential Building**: Pursue specific certifications or credentials relevant to your target roles
        - **Experience Acquisition**: Seek projects or responsibilities that build relevant experience
        - **Mentorship**: Develop relationships with potential mentors in your target field
        
        ### 🌟 Long-term Investments (1-3 years)
        - **Strategic Positioning**: Position for role transitions aligned with your career path
        - **Thought Leadership**: Build recognition in your area of expertise
        - **Continuous Refinement**: Evaluate progress and refine direction based on new insights
        
        ## 🧰 Implementation Toolkit
        
        ### 🔍 Decision Framework
        When evaluating new career opportunities, prioritize alignment with:
        1. **Purpose & Values**: Your core values and purpose drivers
        2. **Environment Fit**: Your preferred work environment characteristics
        3. **Practical Requirements**: Your financial and learning requirements
        4. **Long-term Vision**: Your long-term career trajectory goals
        
        ### 📚 Resource Recommendations
        - **Professional Communities**: Join industry associations in your target field
        - **Learning Platforms**: Utilize skill development platforms aligned with your learning style
        - **Connection Strategies**: Implement networking approaches suited to your personality
        
        ### 🔄 Continuous Adaptation Strategy
        - **Quarterly Check-ins**: Assess progress against key milestones
        - **Annual Review**: Conduct deeper evaluation of career direction
        - **Feedback Integration**: Regularly incorporate new insights from mentors and peers
        
        This personalized career strategy represents an intelligent starting point based on comprehensive analysis of your unique profile. As you gain new experiences and insights, continue refining this living plan to ensure ongoing alignment with your evolving professional aspirations.
        """
        
        return strategy
    
    def _generate_follow_up_response(self, question):
        """Generate responses to follow-up questions after the final report"""
        
        # If we don't have a Gemini model configured, return a basic response
        if not hasattr(self, 'model'):
            return self._generate_basic_follow_up_response(question), True
        
        # Create a prompt that includes the context of all agent results
        prompt = f"""
        You are a Career Strategy Orchestrator who has synthesized insights from 11 specialized career agents
        into a cohesive strategy for a client. The client has a follow-up question about their career strategy.
        
        The specialized agents covered these career dimensions:
        - Skills and competencies
        - Core values
        - Financial considerations
        - Learning and development
        - Industry insights
        - Networking and relationships
        - Role fit analysis
        - Work environment preferences
        - Personal identity and branding
        - Purpose and meaning
        - Career trajectory planning
        
        Below is a summary of key insights from each agent:
        """
        
        # Add condensed results from each agent
        for agent_name, results in self.agent_results.items():
            # Extract 3-5 key points from each agent's results
            prompt += f"\n## {agent_name.upper()} INSIGHTS\n"
            
            if agent_name == "skills":
                prompt += f"- Core skills: {', '.join(results.get('core_skills', ['Not specified'])[:3])}\n"
                prompt += f"- Skill gaps: {', '.join(results.get('skill_gaps', ['Not specified'])[:3])}\n"
                prompt += f"- Development recommendations: {', '.join(results.get('development_recommendations', ['Not specified'])[:3])}\n"
            
            elif agent_name == "values":
                prompt += f"- Core values: {', '.join(results.get('core_values', ['Not specified'])[:3])}\n"
                prompt += f"- Value conflicts: {', '.join(results.get('value_conflicts', ['Not specified'])[:3])}\n"
                prompt += f"- Career implications: {', '.join(results.get('career_implications', ['Not specified'])[:3])}\n"
            
            elif agent_name == "financial":
                prompt += f"- Financial priorities: {', '.join(results.get('financial_priorities', ['Not specified'])[:3])}\n"
                prompt += f"- Compensation factors: {', '.join(results.get('compensation_factors', ['Not specified'])[:3])}\n"
            
            elif agent_name == "learning":
                prompt += f"- Learning preferences: {', '.join(results.get('learning_preferences', ['Not specified'])[:3])}\n"
                prompt += f"- Growth areas: {', '.join(results.get('growth_areas', ['Not specified'])[:3])}\n"
            
            elif agent_name == "industry":
                prompt += f"- Industry interests: {', '.join(results.get('industry_interests', ['Not specified'])[:3])}\n"
                prompt += f"- Industry recommendations: {', '.join(results.get('industry_recommendations', ['Not specified'])[:3])}\n"
            
            elif agent_name == "network":
                prompt += f"- Networking style: {', '.join(results.get('networking_style', ['Not specified'])[:3])}\n"
                prompt += f"- Relationship priorities: {', '.join(results.get('relationship_priorities', ['Not specified'])[:3])}\n"
            
            elif agent_name == "role_fit":
                prompt += f"- Role preferences: {', '.join(results.get('role_preferences', ['Not specified'])[:3])}\n"
                prompt += f"- Role recommendations: {', '.join(results.get('role_recommendations', ['Not specified'])[:3])}\n"
            
            elif agent_name == "work_environment":
                prompt += f"- Environment preferences: {', '.join(results.get('physical_preferences', ['Not specified'])[:3])}\n"
                prompt += f"- Culture preferences: {', '.join(results.get('culture_preferences', ['Not specified'])[:3])}\n"
                prompt += f"- Top environment match: {results.get('top_environment_match', 'Not specified')}\n"
            
            elif agent_name == "identity":
                prompt += f"- Identity elements: {', '.join(results.get('current_identity', ['Not specified'])[:3])}\n"
                prompt += f"- Brand differentiators: {', '.join(results.get('differentiators', ['Not specified'])[:3])}\n"
                prompt += f"- Primary archetype: {results.get('primary_archetype', 'Not specified')}\n"
            
            elif agent_name == "purpose":
                prompt += f"- Meaningful activities: {', '.join(results.get('meaningful_activities', ['Not specified'])[:3])}\n"
                prompt += f"- Problem areas: {', '.join(results.get('problem_areas', ['Not specified'])[:3])}\n"
                prompt += f"- Primary purpose theme: {results.get('primary_purpose_theme', 'Not specified')}\n"
            
            elif agent_name == "career_trajectory":
                prompt += f"- Short term goals: {', '.join(results.get('short_term_goals', ['Not specified'])[:3])}\n"
                prompt += f"- Long term goals: {', '.join(results.get('long_term_goals', ['Not specified'])[:3])}\n"
                prompt += f"- Primary career path: {results.get('primary_path', 'Not specified')}\n"
        
        # Add the client's question
        prompt += f"""
        
        The client has the following follow-up question:
        "{question}"
        
        Provide a thoughtful, specific response that draws on the integrated insights from all agents.
        Make your response practical and actionable, not just theoretical. Connect different dimensions
        when relevant to provide a holistic perspective. Format your answer in clean Markdown.
        """
        
        # Generate the response using Gemini
        try:
            response = self.model.generate_content(prompt)
            return response.text, True
        except Exception as e:
            # Fall back to basic response if Gemini fails
            print(f"Error generating follow-up response with Gemini: {e}")
            return self._generate_basic_follow_up_response(question), True
    
    def _generate_basic_follow_up_response(self, question):
        """Generate a basic response to follow-up questions without using Gemini API"""
        question_lower = question.lower()
        
        if "skill" in question_lower or "competenc" in question_lower:
            response = """
            ## Skills Development Recommendations
            
            Based on your skill profile, here are some recommendations:
            
            1. **Leverage your existing strengths** in your identified core competencies while working on any gaps
            
            2. **Consider skill adjacencies** - look for opportunities to apply your existing skills in new contexts
            
            3. **Prioritize skill development** based on:
               - Alignment with your career goals
               - Market demand in your target industries
               - Your natural learning preferences
            
            4. **Create a structured learning plan** with specific milestones and timelines
            
            Would you like more specific guidance on any particular skill area?
            """
        
        elif "value" in question_lower or "purpose" in question_lower or "meaning" in question_lower:
            response = """
            ## Values & Purpose Integration
            
            Aligning your work with your core values and sense of purpose is crucial for long-term satisfaction.
            Consider these approaches:
            
            1. **Identify roles where your values are central** to the work, not peripheral
            
            2. **Look beyond job titles** to understand how specific organizations express values in practice
            
            3. **Consider multiple expressions of purpose** - you can find meaning through:
               - The work itself
               - The impact of your work
               - The people you work with
               - The skills you develop
            
            4. **Regular alignment check-ins** - schedule quarterly reflection on how your work aligns with your values
            
            What specific aspect of values or purpose alignment would you like to explore further?
            """
        
        elif "industry" in question_lower or "role" in question_lower or "job" in question_lower:
            response = """
            ## Industry & Role Selection
            
            When evaluating specific industries and roles, consider this framework:
            
            1. **Alignment Assessment**:
               - How well does the industry culture align with your values?
               - Does the role leverage your core strengths?
               - Will the work environment support your preferences?
            
            2. **Growth Potential**:
               - Are there clear progression paths that align with your goals?
               - Does the industry offer long-term sustainability?
               - Will you develop transferable skills?
            
            3. **Practical Considerations**:
               - Does the compensation structure meet your financial requirements?
               - Is the work-life balance compatible with your needs?
               - What entry barriers exist and how can you address them?
            
            Would you like to discuss specific industries or roles in more detail?
            """
        
        elif "network" in question_lower or "connect" in question_lower or "relationship" in question_lower:
            response = """
            ## Networking & Relationship Building
            
            Based on your networking preferences, consider these strategies:
            
            1. **Authentic Connection Approach**:
               - Focus on genuine relationship building rather than transactional networking
               - Lead with curiosity and how you might help others
               - Connect around shared interests and values
            
            2. **Strategic Relationship Development**:
               - Identify key relationships that align with your career goals
               - Develop relationships at multiple levels: peers, mentors, and sponsors
               - Create a system for maintaining connections over time
            
            3. **Networking Practices**:
               - Schedule regular networking activities aligned with your preferences
               - Prepare thoughtful questions before conversations
               - Follow up meaningfully after initial connections
            
            How can I help you develop more specific networking strategies?
            """
        
        else:
            response = """
            ## Career Strategy Guidance
            
            Thank you for your question. To provide you with the most relevant guidance, I'd recommend focusing on these key areas:
            
            1. **Integrated Decision-Making**:
               - Weigh decisions against your full profile of skills, values, and preferences
               - Consider both immediate fit and long-term development potential
               - Evaluate opportunities holistically rather than on single dimensions
            
            2. **Balanced Implementation**:
               - Create action plans that address multiple dimensions simultaneously
               - Balance immediate needs with long-term strategic development
               - Regularly reassess and adjust your approach as you gather new information
            
            3. **Continuous Learning**:
               - Treat career development as an ongoing experiment and learning process
               - Gather feedback from multiple sources to refine your approach
               - Develop reflection practices to extract maximum learning from experiences
            
            Can you share more specific details about what aspect of your career strategy you'd like to explore?
            """
        
        return response
    
    def _save_user_data(self, user_details):
        """Save the user data for future sessions"""
        user_id = user_details.get("user_id", "anonymous_user")
        
        # Combine all data
        complete_data = {
            "user_details": user_details,
            "agent_results": self.agent_results,
            "current_agent_index": self.current_agent_index,
            "final_integration_started": self.final_integration_started,
            "final_report_generated": self.final_report_generated,
            "last_session": datetime.now().isoformat()
        }
        
        # Create data directory if it doesn't exist
        os.makedirs("data", exist_ok=True)
        
        # Save to JSON file
        try:
            with open(f"data/{user_id}.json", "w") as f:
                json.dump(complete_data, f, indent=4)
        except Exception as e:
            print(f"Error saving user data: {e}")
    
    def load_user_data(self, user_id):
        """Load user data from a previous session"""
        try:
            with open(f"data/{user_id}.json", "r") as f:
                data = json.load(f)
                
                self.user_data = data.get("user_details", {})
                self.agent_results = data.get("agent_results", {})
                self.current_agent_index = data.get("current_agent_index", 0)
                self.final_integration_started = data.get("final_integration_started", False)
                self.final_report_generated = data.get("final_report_generated", False)
                
                return True
        except (FileNotFoundError, json.JSONDecodeError):
            return False