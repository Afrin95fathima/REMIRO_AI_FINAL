import streamlit as st

class LearningAgent:
    """
    Learning Agent - Growth Strategist
    Analyzes learning preferences and creates personalized development plans
    """
    
    def __init__(self):
        self.name = "Growth Strategist"
        self.description = "Learning and development advisor"
        self.questions = [
            {
                "question": "How do you prefer to learn new skills?",
                "type": "multiple_choice",
                "options": [
                    "Online courses and tutorials",
                    "Hands-on practice and experimentation",
                    "Classroom/workshop training",
                    "Mentorship and coaching",
                    "Reading books and articles",
                    "Learning from colleagues",
                    "Conferences and seminars",
                    "Certification programs",
                    "Self-directed study",
                    "Project-based learning"
                ]
            },
            {
                "question": "What is your preferred learning pace?",
                "type": "multiple_choice",
                "options": [
                    "Intensive, concentrated learning",
                    "Gradual, steady progress",
                    "Flexible, as needed basis",
                    "Regular scheduled sessions",
                    "Weekend/evening learning",
                    "Full-time immersive programs",
                    "Micro-learning sessions",
                    "Learn while working",
                    "Seasonal intensive programs",
                    "Just-in-time learning"
                ]
            },
            {
                "question": "What motivates you to learn and grow?",
                "type": "multiple_choice",
                "options": [
                    "Career advancement opportunities",
                    "Personal satisfaction and growth",
                    "Staying current with industry trends",
                    "Solving challenging problems",
                    "Increasing earning potential",
                    "Building expertise and reputation",
                    "Helping others and teaching",
                    "Job security and marketability",
                    "Creative expression",
                    "Making a meaningful impact"
                ]
            }
        ]
        self.current_question_index = 0
        self.responses = []
        self.analysis_complete = False
    
    def get_introduction(self):
        """Get the introduction message for this agent"""
        return """# 📚 Learning & Development Assessment
        
Welcome! I'm your **Growth Strategy Advisor**. I'll help you:

✅ **Identify your learning preferences**  
✅ **Understand your development style**  
✅ **Discover what motivates your growth**  
✅ **Create a personalized learning plan**  

Understanding how you learn best is key to continuous professional development and career success.

**Ready to explore your learning and growth strategy?**"""
    
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
        
        return "Thank you for your response. Let me analyze your learning preferences.", False, None
    
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
- Or type your own learning preferences/responses
- Example: "1, 3, 7" or "Online learning, Mentorship, My custom approach"

**Progress:** Question {self.current_question_index + 1} of {len(self.questions)}"""
        
        return question_text
    
    def _generate_final_analysis(self):
        """Generate the final learning analysis"""
        # Extract learning preferences from responses
        learning_methods = self._extract_values(self.responses[0]) if len(self.responses) > 0 else []
        learning_pace = self._extract_values(self.responses[1]) if len(self.responses) > 1 else []
        motivations = self._extract_values(self.responses[2]) if len(self.responses) > 2 else []
        
        analysis = f"""# 📚 Learning & Development Analysis Results

## 🎯 Your Learning Profile

Based on your responses, here's your personalized learning strategy:

**Preferred Learning Methods:**
"""
        for method in learning_methods[:5]:
            analysis += f"• {method}\n"
        
        analysis += f"""

**Preferred Learning Pace:**
"""
        for pace in learning_pace[:3]:
            analysis += f"• {pace}\n"
        
        analysis += f"""

**Learning Motivations:**
"""
        for motivation in motivations[:3]:
            analysis += f"• {motivation}\n"
        
        analysis += """

## 🚀 Personalized Development Strategy

Your learning profile suggests you should:

- Choose development opportunities that match your preferred learning methods
- Structure your learning schedule to align with your ideal pace
- Focus on learning that connects to your core motivations
- Combine multiple learning approaches for maximum effectiveness
- Set clear goals that align with your motivational drivers

## 📈 Learning Action Plan

1. **Identify Priority Skills**: Focus on 2-3 key areas for development
2. **Choose Right Methods**: Use your preferred learning approaches
3. **Create Schedule**: Plan learning activities that fit your pace preference
4. **Track Progress**: Monitor development using your motivational drivers
5. **Apply Learning**: Seek opportunities to practice and demonstrate new skills

Your learning strategy should fuel continuous growth throughout your career!
"""
        
        return analysis
    
    def _extract_values(self, response):
        """Extract values from user response"""
        if not response:
            return []
        
        values = []
        
        # Try to extract based on numbers
        import re
        numbers = re.findall(r'\d+', response)
        
        if numbers:
            # User used numbers - map to actual options
            for num in numbers:
                try:
                    idx = int(num) - 1
                    question_idx = min(len(self.responses)-1, len(self.questions)-1)
                    if 0 <= idx < len(self.questions[question_idx]['options']):
                        values.append(self.questions[question_idx]['options'][idx])
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
                "learning_methods": self._extract_values(self.responses[0]),
                "learning_pace": self._extract_values(self.responses[1]),
                "learning_motivations": self._extract_values(self.responses[2]),
                "development_strategy": "Learning analysis completed"
            }
        return {"development_strategy": "In progress"}