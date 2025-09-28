import streamlit as st

class FinancialAgent:
    """
    Financial Agent - Financial Strategist
    Develops personalized compensation and financial strategies for career decisions
    """
    
    def __init__(self):
        self.name = "Financial Strategist"
        self.description = "Compensation and financial planning advisor"
        self.questions = [
            {
                "question": "What are your current financial priorities?",
                "type": "multiple_choice",
                "options": [
                    "Maximizing current income",
                    "Job security and stability",
                    "Comprehensive benefits package",
                    "Equity/stock options potential",
                    "Work-life balance over high pay",
                    "Steady career progression",
                    "Retirement/pension benefits",
                    "Learning opportunities",
                    "Flexible work arrangements",
                    "Professional development budget"
                ]
            },
            {
                "question": "What is your target income level?",
                "type": "multiple_choice",
                "options": [
                    "Below $40,000 annually",
                    "$40,000 - $60,000 annually",
                    "$60,000 - $80,000 annually", 
                    "$80,000 - $100,000 annually",
                    "$100,000 - $150,000 annually",
                    "$150,000 - $200,000 annually",
                    "Above $200,000 annually",
                    "I prioritize other factors over income",
                    "I'm flexible on salary expectations",
                    "I'm unsure about realistic targets"
                ]
            },
            {
                "question": "How important are benefits and non-salary compensation?",
                "type": "multiple_choice",
                "options": [
                    "Extremely important - deal breakers",
                    "Very important in decision making",
                    "Moderately important consideration",
                    "Nice to have but not essential",
                    "Not very important to me",
                    "Health insurance is critical",
                    "Retirement contributions matter most",
                    "Flexible PTO is key",
                    "Professional development budget",
                    "Remote work allowance"
                ]
            }
        ]
        self.current_question_index = 0
        self.responses = []
        self.analysis_complete = False
    
    def get_introduction(self):
        """Get the introduction message for this agent"""
        return """# 💰 Financial Strategy Assessment
        
Welcome! I'm your **Financial Strategy Advisor**. I'll help you:

✅ **Clarify your financial priorities**  
✅ **Set realistic income targets**  
✅ **Evaluate benefits and compensation**  
✅ **Plan your financial career path**  

Understanding your financial goals is crucial for making career decisions that support your overall life objectives.

**Ready to discuss your financial career strategy?**"""
    
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
        
        return "Thank you for your response. Let me analyze your financial priorities.", True, self._get_results()
    
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
- Or type your own financial priorities/responses
- Example: "1, 4, 7" or "High salary, Good benefits, My custom priority"

**Progress:** Question {self.current_question_index + 1} of {len(self.questions)}"""
        
        return question_text
    
    def _generate_final_analysis(self):
        """Generate the final financial analysis"""
        # Extract financial priorities from responses
        priorities = self._extract_values(self.responses[0]) if len(self.responses) > 0 else []
        income_targets = self._extract_values(self.responses[1]) if len(self.responses) > 1 else []
        benefits_importance = self._extract_values(self.responses[2]) if len(self.responses) > 2 else []
        
        analysis = f"""# 💰 Financial Strategy Analysis Results

## 🎯 Your Financial Profile

Based on your responses, here's your financial career strategy:

**Top Financial Priorities:**
"""
        for priority in priorities[:5]:
            analysis += f"• {priority}\n"
        
        analysis += f"""

**Income Targets:**
"""
        for target in income_targets[:3]:
            analysis += f"• {target}\n"
        
        analysis += f"""

**Benefits Preferences:**
"""
        for benefit in benefits_importance[:3]:
            analysis += f"• {benefit}\n"
        
        analysis += """

## 💡 Financial Career Strategy

Your financial profile suggests you should:

- Focus on opportunities that align with your financial priorities
- Target roles within your desired income range
- Evaluate total compensation packages, not just base salary
- Consider long-term financial growth potential
- Balance immediate needs with future financial goals

## 📈 Financial Action Plan

1. **Research Market Rates**: Understand compensation ranges for your target roles
2. **Negotiate Strategically**: Focus on your highest-priority financial elements
3. **Plan for Growth**: Consider both immediate and long-term financial trajectory
4. **Evaluate Total Package**: Look beyond salary to benefits, equity, and perks

Your financial strategy should align with your overall career goals and life priorities!
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
                "financial_priorities": self._extract_values(self.responses[0]),
                "income_targets": self._extract_values(self.responses[1]),
                "benefits_importance": self._extract_values(self.responses[2]),
                "financial_strategy": "Financial analysis completed"
            }
        return {"financial_strategy": "In progress"}