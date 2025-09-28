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
                    "Work-life balance",
                    "High salary/financial security",
                    "Job security and stability", 
                    "Career advancement opportunities",
                    "Making a positive impact",
                    "Creative freedom and expression",
                    "Independence and autonomy",
                    "Team collaboration",
                    "Learning and development",
                    "Recognition and achievement"
                ]
            },
            {
                "question": "What type of work environment do you prefer?",
                "type": "multiple_choice",
                "options": [
                    "Fast-paced and dynamic",
                    "Structured and organized",
                    "Collaborative team setting",
                    "Quiet and focused",
                    "Flexible and remote-friendly",
                    "Innovation-focused culture",
                    "Results-oriented environment",
                    "Supportive and inclusive",
                    "Competitive atmosphere",
                    "Mission-driven organization"
                ]
            },
            {
                "question": "What type of impact do you want to make through work?",
                "type": "multiple_choice", 
                "options": [
                    "Help individuals improve their lives",
                    "Solve complex technical problems",
                    "Create innovative products/services",
                    "Drive business growth and success",
                    "Contribute to social causes",
                    "Advance scientific knowledge",
                    "Educate and develop others",
                    "Improve organizational efficiency",
                    "Build sustainable solutions",
                    "Enable others to succeed"
                ]
            }
        ]
        self.current_question_index = 0
        self.responses = []
        self.analysis_complete = False
    
    def get_introduction(self):
        """Get the introduction message for this agent"""
        return """# 💎 Values & Principles Assessment
        
Welcome! I'm your **Values Alignment Specialist**. I'll help you:

✅ **Identify your core work values**  
✅ **Understand your ideal work environment**  
✅ **Discover what impact you want to make**  
✅ **Align your career with your principles**  

Understanding your values is essential for finding work that feels meaningful and fulfilling.

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
        question_text = f"""## {question_data['question']}

Please type your selections from the options below, or add your own:

**Available Options:**
"""
        
        for i, option in enumerate(question_data['options'], 1):
            question_text += f"\n{i}. {option}"
        
        question_text += f"""

**Instructions:** 
- Type the numbers (1, 2, 3, etc.) of your selections separated by commas
- Or type your own values/responses
- Example: "1, 3, 7" or "Work-life balance, Creativity, My personal value"

**Progress:** Question {self.current_question_index + 1} of {len(self.questions)}"""
        
        return question_text
    
    def _generate_final_analysis(self):
        """Generate the final values analysis"""
        # Extract values from responses
        work_values = self._extract_values(self.responses[0]) if len(self.responses) > 0 else []
        environment_prefs = self._extract_values(self.responses[1]) if len(self.responses) > 1 else []
        impact_desires = self._extract_values(self.responses[2]) if len(self.responses) > 2 else []
        
        analysis = f"""# 🎯 Values & Principles Analysis Results

## 💎 Your Core Work Values

Based on your responses, here are your primary work values:

**Top Work Values:**
"""
        for value in work_values[:5]:
            analysis += f"• {value}\n"
        
        analysis += f"""

**Preferred Work Environment:**
"""
        for env in environment_prefs[:3]:
            analysis += f"• {env}\n"
        
        analysis += f"""

**Desired Impact:**
"""
        for impact in impact_desires[:3]:
            analysis += f"• {impact}\n"
        
        analysis += """

## 🔍 Values-Based Career Insights

Your values profile suggests you would thrive in roles and organizations that:

- Align with your core values and provide meaningful work
- Offer the type of work environment you prefer
- Allow you to make the kind of impact you desire
- Provide opportunities for growth while maintaining your values

## 📋 Values-Driven Decision Framework

When evaluating career opportunities, consider:

1. **Values Alignment**: Does this opportunity align with your core values?
2. **Environment Fit**: Does the work environment match your preferences?
3. **Impact Potential**: Will you be able to make the kind of impact you desire?
4. **Growth Opportunities**: Does it provide growth while maintaining your values?

Your values are your career compass - use them to guide your decisions!
"""
        
        return analysis
    
    def _extract_values(self, response):
        """Extract values from user response"""
        if not response:
            return []
        
        # Simple extraction - look for numbers or direct mentions
        values = []
        response_lower = response.lower()
        
        # Try to extract based on numbers
        import re
        numbers = re.findall(r'\d+', response)
        
        if numbers:
            # User used numbers - map to actual options
            for num in numbers:
                try:
                    idx = int(num) - 1
                    if 0 <= idx < len(self.questions[min(len(self.responses)-1, len(self.questions)-1)]['options']):
                        values.append(self.questions[min(len(self.responses)-1, len(self.questions)-1)]['options'][idx])
                except ValueError:
                    continue
        else:
            # User typed their own responses
            values = [response.strip()]
        
        return values
    
    def _get_results(self):
        """Get the results for this agent"""
        if len(self.responses) >= 3:
            return {
                "core_values": self._extract_values(self.responses[0]),
                "environment_preferences": self._extract_values(self.responses[1]),
                "impact_desires": self._extract_values(self.responses[2]),
                "values_summary": "Values analysis completed"
            }
        return {"values_summary": "In progress"}