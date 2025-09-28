import streamlit as st

class SkillsAgent:
    """
    Skills Agent - Skills & Competency Architect
    Analyzes skill portfolios and creates strategic skill acquisition plans
    """
    
    def __init__(self):
        self.name = "Skills & Competency Architect"
        self.description = "Talent Development Advisor focusing on strategic skill development"
        self.questions = [
            {
                "question": "What are your strongest technical or specialized skills?",
                "type": "multiple_choice",
                "options": [
                    "Programming/Software Development",
                    "Data Analysis & Analytics",
                    "Digital Marketing & SEO",
                    "Project Management",
                    "Financial Analysis",
                    "Design & Creative Skills",
                    "Research & Analysis",
                    "Engineering & Technical",
                    "Sales & Business Development",
                    "Operations & Process Improvement"
                ]
            },
            {
                "question": "Which transferable skills do you excel at?",
                "type": "multiple_choice", 
                "options": [
                    "Communication & Presentation",
                    "Leadership & Team Management",
                    "Problem Solving & Critical Thinking",
                    "Time Management & Organization",
                    "Adaptability & Flexibility",
                    "Negotiation & Persuasion",
                    "Customer Service & Relationship Building",
                    "Training & Mentoring",
                    "Strategic Planning",
                    "Decision Making"
                ]
            },
            {
                "question": "What skills would you like to develop or improve?",
                "type": "multiple_choice",
                "options": [
                    "AI & Machine Learning",
                    "Advanced Data Analysis",
                    "Public Speaking & Presentation",
                    "Leadership & Management",
                    "Digital Marketing",
                    "Programming & Coding",
                    "Financial Modeling",
                    "Strategic Thinking",
                    "Networking & Relationship Building",
                    "Innovation & Creativity"
                ]
            }
        ]
        self.current_question_index = 0
        self.responses = []
        self.analysis_complete = False
    
    def get_introduction(self):
        """Get the introduction message for this agent"""
        return """# 🛠️ Skills & Competency Assessment
        
Welcome! I'm your **Skills & Competency Architect**. I'm here to help you:

✅ **Identify your strongest skills and competencies**  
✅ **Discover skill gaps and development opportunities**  
✅ **Create a strategic skill development plan**  
✅ **Align your skills with career opportunities**  

Let's start by understanding your current skill portfolio. I'll ask you a few questions and you can select from the options or add your own responses.

**Ready to begin your skills analysis?**"""
    
    def process_message(self, message):
        """Process user message and return response"""
        if self.analysis_complete:
            return self._generate_final_analysis(), True, self._get_results()
        
        # Store the user's response
        self.responses.append(message)
        
        if self.current_question_index < len(self.questions):
            # Move to next question
            self.current_question_index += 1
            
            if self.current_question_index < len(self.questions):
                # Ask next question
                next_question = self.questions[self.current_question_index]
                return self._format_question(next_question), False, None
            else:
                # All questions answered, generate analysis
                self.analysis_complete = True
                return self._generate_final_analysis(), True, self._get_results()
        
        # This shouldn't happen, but just in case
        return "Thank you for your response. Let me analyze your skills profile.", True, self._get_results()
    
    def _format_question(self, question_data):
        """Format question with options"""
        question_text = f"""## {question_data['question']}

Please type your selections from the options below, or add your own:

**Available Options:**
"""
        
        for i, option in enumerate(question_data['options'], 1):
            question_text += f"\n{i}. {option}"
        
        question_text += f"""

**Instructions:** 
- Type the numbers (1, 2, 3, etc.) of your selections separated by commas
- Or type your own skills/responses
- Example: "1, 3, 5" or "Programming, Leadership, My custom skill"

**Progress:** Question {self.current_question_index + 1} of {len(self.questions)}"""
        
        return question_text
    
    def _generate_final_analysis(self):
        """Generate the final skills analysis"""
        # Analyze responses
        technical_skills = []
        transferable_skills = []
        development_areas = []
        
        # Process first response (technical skills)
        if len(self.responses) > 0:
            technical_skills = self._extract_skills(self.responses[0])
        
        # Process second response (transferable skills)
        if len(self.responses) > 1:
            transferable_skills = self._extract_skills(self.responses[1])
        
        # Process third response (development areas)
        if len(self.responses) > 2:
            development_areas = self._extract_skills(self.responses[2])
        
        analysis = """# 🎯 Skills & Competency Analysis Results

Based on our conversation, I've analyzed your current skill portfolio and identified potential development opportunities.

## 💪 Your Current Skill Portfolio

### 🔧 Technical/Specialized Skills
"""
        
        if technical_skills:
            for skill in technical_skills[:5]:  # Top 5 technical skills
                analysis += f"- **{skill}**\n"
        else:
            analysis += "- No specific technical skills identified in our conversation\n"
        
        analysis += """
### 🔄 Transferable Skills
"""
        
        if transferable_skills:
            for skill in transferable_skills[:5]:  # Top 5 transferable skills
                analysis += f"- **{skill}**\n"
        else:
            analysis += "- No specific transferable skills identified in our conversation\n"
        
        analysis += """
## 🎯 Development Opportunities

### Skills to Develop
"""
        
        if development_areas:
            for area in development_areas[:5]:  # Top 5 development areas
                analysis += f"- **{area}**\n"
        else:
            analysis += "- No specific development areas identified\n"
        
        analysis += f"""
## 📈 Strategic Recommendations

### Immediate Actions (Next 30 Days)
1. **Skill Inventory**: Create a detailed inventory of your current skills with proficiency levels
2. **Market Research**: Research skill requirements for your target roles
3. **Learning Plan**: Choose 1-2 high-impact skills to focus on first

### Short-term Development (3-6 Months)
1. **Skill Building**: Enroll in courses or certifications for priority skills
2. **Practice Opportunities**: Seek projects that allow you to apply new skills
3. **Networking**: Connect with professionals who have skills you want to develop

### Long-term Strategy (6-12 Months)
1. **Expertise Building**: Become proficient in your chosen development areas
2. **Portfolio Development**: Create examples demonstrating your new skills
3. **Career Positioning**: Update your professional profile to reflect new competencies

## 🏆 Key Insights

- **Skill Portfolio Strength**: You have a {self._assess_skill_strength(technical_skills, transferable_skills)} skill foundation
- **Development Focus**: Prioritize {len(development_areas)} key skill areas for maximum career impact
- **Market Alignment**: Your skills show {self._assess_market_alignment()} alignment with current market demands

This completes your skills analysis. Your skills profile will be integrated with insights from other agents to create your comprehensive career strategy."""
        
        return analysis
    
    def _extract_skills(self, response):
        """Extract skills from response text"""
        skills = []
        response_lower = response.lower()
        
        # Common skill keywords to look for
        skill_keywords = [
            "programming", "python", "javascript", "data analysis", "machine learning",
            "communication", "leadership", "project management", "problem solving",
            "critical thinking", "teamwork", "adaptability", "creativity", "strategic",
            "marketing", "sales", "finance", "design", "research", "writing",
            "presentation", "negotiation", "customer service", "training", "mentoring"
        ]
        
        for keyword in skill_keywords:
            if keyword in response_lower:
                skills.append(keyword.title())
        
        # Also split response by common separators and add relevant parts
        parts = response.replace(",", "\n").replace(";", "\n").replace(".", "\n").split("\n")
        for part in parts:
            part = part.strip()
            if len(part) > 3 and len(part) < 50:  # Reasonable skill name length
                skills.append(part.title())
        
        return list(set(skills))[:10]  # Remove duplicates and limit to 10
    
    def _assess_skill_strength(self, technical_skills, transferable_skills):
        """Assess overall skill portfolio strength"""
        total_skills = len(technical_skills) + len(transferable_skills)
        if total_skills >= 8:
            return "strong"
        elif total_skills >= 5:
            return "solid"
        elif total_skills >= 3:
            return "developing"
        else:
            return "emerging"
    
    def _assess_market_alignment(self):
        """Assess market alignment of skills"""
        # This is a simplified assessment - in reality would use job market data
        return "good"
    
    def _get_results(self):
        """Return structured results for integration with other agents"""
        technical_skills = []
        transferable_skills = []
        development_areas = []
        
        if len(self.responses) > 0:
            technical_skills = self._extract_skills(self.responses[0])
        if len(self.responses) > 1:
            transferable_skills = self._extract_skills(self.responses[1])
        if len(self.responses) > 2:
            development_areas = self._extract_skills(self.responses[2])
        
        return {
            "agent_name": "skills",
            "technical_skills": technical_skills,
            "transferable_skills": transferable_skills,
            "development_areas": development_areas,
            "skill_strength": self._assess_skill_strength(technical_skills, transferable_skills),
            "market_alignment": self._assess_market_alignment(),
            "total_skills_identified": len(technical_skills) + len(transferable_skills),
            "development_priorities": development_areas[:3],  # Top 3 priorities
            "core_skills": technical_skills[:3] + transferable_skills[:3],  # Top 3 from each category
            "skill_gaps": development_areas,
            "development_recommendations": [
                "Create detailed skill inventory",
                "Research market requirements for target roles", 
                "Develop 1-2 priority skills through structured learning",
                "Seek practice opportunities for new skills",
                "Update professional profile with new competencies"
            ]
        }