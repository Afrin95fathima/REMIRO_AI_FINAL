import streamlit as st

class ValuesAgent:
    """
    Values Agent - Principle Navigator
    Identifies core values to guide authentic career alignment and decision-making
    """
    
    def __init__(self):
        self.name = "Principle Navigator"
        self.description = "Values alignment specialist for authentic career paths"
        self.questions = [
            {
                "question": "What work values are most important to you?",
                "type": "multiple_choice",
                "options": [
                    "Work-Life Balance",
                    "Professional Growth & Development",
                    "Making a Meaningful Impact",
                    "Financial Security & Compensation",
                    "Creative Expression & Innovation",
                    "Autonomy & Independence",
                    "Collaboration & Teamwork",
                    "Leadership & Influence",
                    "Job Security & Stability",
                    "Recognition & Achievement"
                ]
            },
            {
                "question": "What type of work environment brings out your best performance?",
                "type": "multiple_choice", 
                "options": [
                    "Fast-paced & Dynamic",
                    "Structured & Organized",
                    "Collaborative & Social",
                    "Quiet & Focused",
                    "Innovative & Creative",
                    "Results-oriented & Competitive",
                    "Supportive & Nurturing",
                    "Flexible & Adaptable",
                    "Mission-driven & Purpose-focused",
                    "Entrepreneurial & Risk-taking"
                ]
            },
            {
                "question": "What causes or impacts do you care most about?",
                "type": "multiple_choice",
                "options": [
                    "Education & Learning",
                    "Healthcare & Wellness",
                    "Environmental Sustainability",
                    "Social Justice & Equality",
                    "Technology & Innovation",
                    "Economic Development",
                    "Arts & Culture",
                    "Community Building",
                    "Scientific Research",
                    "Global Issues & International Relations"
                ]
            }
        ]
        self.current_question_index = 0
        self.responses = []
        self.analysis_complete = False
    
    def get_introduction(self):
        """Get the introduction message for this agent"""
        return """# ⚖️ Values & Principles Assessment
        
Welcome! I'm your **Principle Navigator**. I'm here to help you:

✅ **Identify your core work values and principles**  
✅ **Understand what drives your career satisfaction**  
✅ **Align your career choices with your authentic self**  
✅ **Recognize potential value conflicts to avoid**  

Understanding your values is essential for finding work that feels meaningful and aligned with who you are. When your career aligns with your values, you're more likely to find fulfillment and purpose.

**Ready to explore what matters most to you in your career?**"""
    
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
        
        return "Thank you for your response. Let me analyze your values profile.", True, self._get_results()
    
    def _format_question(self, question_data):
        """Format question with options"""
        question_text = f"""## 💭 {question_data['question']}

**Select all that apply to you:**
"""
        
        for option in question_data['options']:
            question_text += f"\n☐ {option}"
        
        question_text += f"""

**Or describe your own values:**
_Feel free to type additional values or elaborate on your selections._

---

**Progress:** Question {self.current_question_index + 1} of {len(self.questions)}"""
        
        return question_text
    
    def _generate_final_analysis(self):
        """Generate the final values analysis"""
        # Analyze responses
        core_values = []
        environment_preferences = []
        impact_areas = []
        
        # Process first response (core values)
        if len(self.responses) > 0:
            core_values = self._extract_values(self.responses[0])
        
        # Process second response (environment preferences)
        if len(self.responses) > 1:
            environment_preferences = self._extract_values(self.responses[1])
        
        # Process third response (impact areas)
        if len(self.responses) > 2:
            impact_areas = self._extract_values(self.responses[2])
        
        analysis = """# ⚖️ Values & Principles Analysis Results

Based on our conversation, I've identified your core values and preferences that should guide your career decisions.

## 🎯 Your Core Work Values
"""
        
        if core_values:
            for value in core_values[:5]:  # Top 5 core values
                analysis += f"- **{value}**\n"
        else:
            analysis += "- No specific core values identified in our conversation\n"
        
        analysis += """
### 🏢 Preferred Work Environment
"""
        
        if environment_preferences:
            for pref in environment_preferences[:5]:  # Top 5 environment preferences
                analysis += f"- **{pref}**\n"
        else:
            analysis += "- No specific environment preferences identified\n"
        
        analysis += """
### 🌍 Meaningful Impact Areas
"""
        
        if impact_areas:
            for area in impact_areas[:5]:  # Top 5 impact areas
                analysis += f"- **{area}**\n"
        else:
            analysis += "- No specific impact areas identified\n"
        
        analysis += f"""
## 🧭 Values-Based Career Guidance

### Career Decision Framework
When evaluating career opportunities, prioritize options that:
1. **Honor your core values**: Look for roles that align with your top values
2. **Match your environment preferences**: Seek workplaces that match your preferred style
3. **Enable meaningful impact**: Choose roles that contribute to causes you care about

### Potential Value Conflicts to Watch
- **Work-life balance vs. career advancement**: Be aware of roles that may require significant time investment
- **Financial goals vs. meaningful work**: Consider how to balance compensation with purpose
- **Independence vs. collaboration**: Look for roles that match your preferred working style

### Values Alignment Strategies
1. **Research company culture**: Investigate whether potential employers share your values
2. **Ask values-based interview questions**: Inquire about company mission and culture during interviews
3. **Seek values-aligned organizations**: Target companies whose missions resonate with your impact areas
4. **Create values-based criteria**: Use your values as key factors in career decision-making

## 🏆 Key Insights

- **Values Profile**: You have a {self._assess_values_clarity(core_values)} values foundation for career decision-making
- **Alignment Priority**: Focus on {len(core_values)} core values when evaluating opportunities
- **Impact Focus**: Your desire to contribute to {len(impact_areas)} specific areas provides clear direction

This completes your values analysis. Your values profile will be integrated with insights from other agents to ensure your career strategy is authentically aligned with who you are."""
        
        return analysis
    
    def _extract_values(self, response):
        """Extract values from response text"""
        values = []
        response_lower = response.lower()
        
        # Common value keywords to look for
        value_keywords = [
            "work-life balance", "growth", "development", "impact", "meaningful",
            "security", "creativity", "autonomy", "independence", "collaboration",
            "teamwork", "leadership", "achievement", "recognition", "innovation",
            "flexibility", "stability", "purpose", "mission", "helping others",
            "learning", "challenge", "variety", "respect", "integrity"
        ]
        
        for keyword in value_keywords:
            if keyword in response_lower:
                values.append(keyword.title())
        
        # Also split response by common separators and add relevant parts
        parts = response.replace(",", "\n").replace(";", "\n").replace(".", "\n").split("\n")
        for part in parts:
            part = part.strip()
            if len(part) > 3 and len(part) < 50:  # Reasonable value name length
                values.append(part.title())
        
        return list(set(values))[:8]  # Remove duplicates and limit to 8
    
    def _assess_values_clarity(self, core_values):
        """Assess clarity of values"""
        if len(core_values) >= 5:
            return "clear and well-defined"
        elif len(core_values) >= 3:
            return "solid"
        elif len(core_values) >= 1:
            return "emerging"
        else:
            return "developing"
    
    def _get_results(self):
        """Return structured results for integration with other agents"""
        core_values = []
        environment_preferences = []
        impact_areas = []
        
        if len(self.responses) > 0:
            core_values = self._extract_values(self.responses[0])
        if len(self.responses) > 1:
            environment_preferences = self._extract_values(self.responses[1])
        if len(self.responses) > 2:
            impact_areas = self._extract_values(self.responses[2])
        
        return {
            "agent_name": "values",
            "core_values": core_values,
            "environment_preferences": environment_preferences,
            "impact_areas": impact_areas,
            "values_clarity": self._assess_values_clarity(core_values),
            "total_values_identified": len(core_values),
            "top_values": core_values[:3],  # Top 3 values
            "value_conflicts": [],  # Could be enhanced with conflict detection
            "career_implications": [
                "Prioritize values alignment in career decisions",
                "Research company culture and mission alignment",
                "Use values as key criteria for opportunity evaluation",
                "Seek roles that enable meaningful impact",
                "Consider values when negotiating work arrangements"
            ]
        }