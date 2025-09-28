import streamlit as st
import time

class PersonalityAgent:
    """
    Personality Agent - Personality & Work Style Strategist
    Expert Occupational Psychologist and Career Strategist
    """
    
    def __init__(self):
        self.name = "Personality & Work Style Strategist"
        self.description = "Expert Occupational Psychologist and Career Strategist"
        self.questions = [
            "When you complete a challenging work week, what kind of activity leaves you feeling most energized and recharged for the next one?",
            "Describe your ideal work environment: are you alone in a quiet space, in a bustling open-plan office, or a mix of both? What kind of interactions are you having?",
            "Think about a project where you felt you were at your absolute best. What was it about that situation that allowed you to thrive?"
        ]
        self.follow_up_questions = {
            "extraversion": [
                "On a scale of 1-10, how much do you enjoy being the center of attention in social settings?",
                "How energizing or draining do you find collaborative group work?",
                "After a day of intense social interaction at work, do you typically seek more social time or quiet time?"
            ],
            "conscientiousness": [
                "How important is structure and organization in your work process?",
                "How do you typically react to unexpected changes to plans or deadlines?",
                "Do you prefer clear, specific instructions or the freedom to approach tasks your own way?"
            ],
            "openness": [
                "How often do you seek out new experiences or novel ways of doing things?",
                "How comfortable are you with ambiguity and undefined problems?",
                "How important is creativity and innovation in your work?"
            ],
            "agreeableness": [
                "How do you typically handle workplace conflicts or disagreements?",
                "How important is team harmony versus productive debate in your workplace?",
                "Do you find it easy to say no to requests from colleagues or supervisors?"
            ],
            "neuroticism": [
                "How do you typically handle high-pressure situations or tight deadlines?",
                "How long does it take you to bounce back after a setback or failure?",
                "How often do you find yourself worrying about work outside of working hours?"
            ]
        }
        self.current_question_index = 0
        self.responses = []
        self.trait_scores = {
            "extraversion": 0,
            "conscientiousness": 0,
            "openness": 0,
            "agreeableness": 0,
            "neuroticism": 0
        }
        self.follow_up_focus = None
        self.analysis_complete = False
    
    def get_introduction(self):
        """Get the introduction message for this agent"""
        return f"""
        ## Personality & Work Style Assessment
        
        I'm your **{self.name}**, {self.description}. I'll help analyze your personality traits 
        and natural work style to identify environments where you'll thrive professionally.
        
        I'll be using frameworks like the Big Five personality traits (OCEAN) to understand your 
        natural tendencies and translate them into career insights.
        
        Let's start with this question: **{self.questions[0]}**
        """
    
    def process_message(self, message):
        """Process user message and return appropriate response"""
        
        # Store the user's response
        self.responses.append(message)
        
        # Analyze the response for trait indicators
        self._analyze_response(message)
        
        # If we've gone through all initial questions and any follow-ups
        if self.analysis_complete:
            # Generate and return the final analysis
            final_analysis = self._generate_personality_analysis()
            return final_analysis, True, self._get_results()
        
        # Determine if we should move to follow-up questions based on the responses so far
        if len(self.responses) >= 3 and not self.follow_up_focus:
            # Determine which trait to focus follow-up questions on
            self.follow_up_focus = self._determine_follow_up_focus()
        
        # Get the next question
        next_question = self._get_next_question()
        
        # Check if this was the last question
        if next_question is None:
            self.analysis_complete = True
            final_analysis = self._generate_personality_analysis()
            return final_analysis, True, self._get_results()
        
        return next_question, False, None
    
    def _analyze_response(self, message):
        """
        Analyze the user's response for trait indicators
        This is a simple keyword-based analysis, a real implementation would use NLP
        """
        message_lower = message.lower()
        
        # Extraversion indicators
        if any(word in message_lower for word in ["social", "people", "group", "team", "interact", "conversation", "discuss", "collaborate"]):
            self.trait_scores["extraversion"] += 1
        if any(word in message_lower for word in ["quiet", "alone", "solitary", "independent", "introvert", "by myself", "peace"]):
            self.trait_scores["extraversion"] -= 1
            
        # Conscientiousness indicators
        if any(word in message_lower for word in ["organized", "plan", "schedule", "detail", "careful", "precise", "thorough", "structure", "routine"]):
            self.trait_scores["conscientiousness"] += 1
        if any(word in message_lower for word in ["flexible", "spontaneous", "adaptable", "relaxed approach", "go with the flow"]):
            self.trait_scores["conscientiousness"] -= 1
            
        # Openness indicators
        if any(word in message_lower for word in ["creative", "innovative", "curious", "explore", "new", "different", "change", "imagination", "art"]):
            self.trait_scores["openness"] += 1
        if any(word in message_lower for word in ["traditional", "conventional", "familiar", "proven", "stable", "consistent"]):
            self.trait_scores["openness"] -= 1
            
        # Agreeableness indicators
        if any(word in message_lower for word in ["help", "cooperate", "support", "kind", "consensus", "harmony", "agree", "compassion", "empathy"]):
            self.trait_scores["agreeableness"] += 1
        if any(word in message_lower for word in ["compete", "challenge", "debate", "critique", "direct", "frank", "straightforward", "contest"]):
            self.trait_scores["agreeableness"] -= 1
            
        # Neuroticism indicators
        if any(word in message_lower for word in ["stress", "worry", "anxiety", "pressure", "concerned", "nervous", "fear", "uncertainty"]):
            self.trait_scores["neuroticism"] += 1
        if any(word in message_lower for word in ["calm", "relaxed", "confident", "steady", "balanced", "composed", "resilient", "stable"]):
            self.trait_scores["neuroticism"] -= 1
    
    def _determine_follow_up_focus(self):
        """
        Determine which trait to focus follow-up questions on
        based on the most ambiguous or interesting scores
        """
        # In a real implementation, this would be more sophisticated
        # For now, just pick the trait with the score closest to 0 (most ambiguous)
        scores = [(abs(score), trait) for trait, score in self.trait_scores.items()]
        scores.sort()
        return scores[0][1]  # Return the trait with score closest to 0
    
    def _get_next_question(self):
        """Get the next question to ask"""
        
        # If we're doing follow-up questions on a specific trait
        if self.follow_up_focus:
            follow_up_questions = self.follow_up_questions[self.follow_up_focus]
            follow_up_index = len(self.responses) - 3  # We've already asked 3 main questions
            
            if follow_up_index < len(follow_up_questions):
                return f"**Follow-up:** {follow_up_questions[follow_up_index]}"
            else:
                # No more follow-up questions
                return None
        
        # Otherwise, get the next main question
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            return f"**{self.questions[self.current_question_index]}**"
        else:
            # Start follow-up questions
            self.follow_up_focus = self._determine_follow_up_focus()
            return f"**Follow-up:** {self.follow_up_questions[self.follow_up_focus][0]}"
    
    def _generate_personality_analysis(self):
        """Generate a personality analysis based on the responses"""
        
        # Normalize trait scores to a -5 to 5 scale for clear interpretation
        normalized_traits = {}
        for trait, score in self.trait_scores.items():
            # Clamp scores to a -5 to 5 range
            normalized_traits[trait] = max(-5, min(5, score))
        
        # Map traits to work style characteristics
        work_style = self._get_work_style(normalized_traits)
        
        # Generate the analysis
        analysis = f"""
        ## Personality & Work Style Analysis
        
        Based on our conversation, here's an analysis of your personality traits and how they influence your work style:
        
        ### Core Personality Profile
        
        """
        
        # Add trait descriptions
        for trait, score in normalized_traits.items():
            analysis += f"- **{trait.capitalize()}**: "
            
            if trait == "extraversion":
                if score > 2:
                    analysis += "You tend to be outgoing and energized by social interaction. You likely thrive in collaborative, team-oriented environments."
                elif score < -2:
                    analysis += "You tend to be more reserved and energized by focused, independent work. You likely thrive in environments that allow for deep concentration."
                else:
                    analysis += "You show a balance between social engagement and independent focus. You likely adapt well to both collaborative and solo work."
            
            elif trait == "conscientiousness":
                if score > 2:
                    analysis += "You are highly organized and detail-oriented. You excel with clear structures and well-defined processes."
                elif score < -2:
                    analysis += "You prefer flexibility and spontaneity. You excel in adaptive, less structured environments that allow for creative approaches."
                else:
                    analysis += "You balance structure with flexibility. You appreciate organization but can adapt to changing circumstances."
            
            elif trait == "openness":
                if score > 2:
                    analysis += "You are curious and imaginative. You thrive in innovative environments that welcome new ideas and approaches."
                elif score < -2:
                    analysis += "You value tradition and established methods. You excel in stable environments with proven practices."
                else:
                    analysis += "You balance innovation with practicality. You appreciate new ideas while valuing what has been proven to work."
            
            elif trait == "agreeableness":
                if score > 2:
                    analysis += "You prioritize harmony and cooperation. You excel in supportive teams that value consensus and mutual support."
                elif score < -2:
                    analysis += "You are direct and challenging. You excel in environments that value critical thinking and robust debate."
                else:
                    analysis += "You balance cooperation with healthy challenge. You can support team dynamics while still providing constructive input."
            
            elif trait == "neuroticism":
                if score > 2:
                    analysis += "You are highly responsive to stress and may experience work pressure intensely. You benefit from supportive environments with stress management resources."
                elif score < -2:
                    analysis += "You are emotionally resilient and steady under pressure. You excel in high-stakes environments that require calm decision-making."
                else:
                    analysis += "You show balanced emotional responses. You're generally resilient while still remaining responsive to important concerns."
            
            analysis += "\n\n"
        
        # Add work style summary
        analysis += f"""
        ### Your Natural Work Style
        
        {work_style}
        
        ### Professional Strengths & Potential Blind Spots
        
        **Strengths:**
        - {self._get_strengths(normalized_traits)}
        
        **Potential Blind Spots:**
        - {self._get_blind_spots(normalized_traits)}
        
        ### Recommended Work Environments
        
        Based on your personality profile, you would likely thrive in environments that:
        - {self._get_environment_recommendations(normalized_traits)}
        
        This analysis provides insights into your natural tendencies, but remember that people are complex and adaptable. Your personality is just one factor in your career journey!
        """
        
        return analysis
    
    def _get_work_style(self, traits):
        """Generate work style description based on traits"""
        
        extraversion = traits["extraversion"]
        conscientiousness = traits["conscientiousness"]
        openness = traits["openness"]
        
        # Determine primary work style
        if extraversion > 2 and conscientiousness > 2:
            return "You have a **Structured Collaborative** work style. You excel in team environments with clear processes and defined goals. You enjoy organized group work and thrive when leading or participating in well-managed team projects."
        
        elif extraversion > 2 and openness > 2:
            return "You have a **Dynamic Collaborative** work style. You excel in creative team settings that encourage innovation and social energy. You're likely a catalyst for group brainstorming and excel when working with others to explore new ideas."
        
        elif extraversion < -2 and conscientiousness > 2:
            return "You have a **Structured Independent** work style. You excel in focused, organized solo work with clear objectives. You thrive in environments that allow for deep, uninterrupted concentration on well-defined tasks and projects."
        
        elif extraversion < -2 and openness > 2:
            return "You have a **Creative Independent** work style. You excel in roles that allow for deep, imaginative thinking without constant social demands. You likely produce your best ideas when given space for reflection and creative exploration."
        
        elif conscientiousness > 2 and openness < -2:
            return "You have a **Methodical Conventional** work style. You excel in environments with established procedures and predictable workflows. You appreciate stability and excel at perfecting existing systems."
        
        elif conscientiousness < -2 and openness > 2:
            return "You have an **Adaptive Explorer** work style. You excel in fluid, innovative environments that value experimentation over rigid processes. You're comfortable with ambiguity and adapt quickly to changing circumstances."
        
        else:
            return "You have a **Balanced Adaptable** work style. You show flexibility in how you approach work, able to adjust your style based on the context. This versatility allows you to succeed across various professional settings and team dynamics."
    
    def _get_strengths(self, traits):
        """Generate strengths based on trait profile"""
        
        strengths = []
        
        if traits["extraversion"] > 2:
            strengths.append("Building relationships and networks that create professional opportunities")
            strengths.append("Energizing team dynamics and collaborative projects")
        elif traits["extraversion"] < -2:
            strengths.append("Sustained focus on complex tasks without needing social validation")
            strengths.append("Deep thinking and careful consideration before communication")
        
        if traits["conscientiousness"] > 2:
            strengths.append("Exceptional attention to detail and follow-through")
            strengths.append("Reliability and consistency in meeting deadlines and commitments")
        elif traits["conscientiousness"] < -2:
            strengths.append("Adaptability when plans need to change quickly")
            strengths.append("Creative approaches to tasks that aren't limited by conventional procedures")
        
        if traits["openness"] > 2:
            strengths.append("Innovative thinking and ability to envision new possibilities")
            strengths.append("Comfort with complexity and abstract concepts")
        elif traits["openness"] < -2:
            strengths.append("Practical, grounded approaches focused on proven methods")
            strengths.append("Stability and consistency in implementation")
        
        if traits["agreeableness"] > 2:
            strengths.append("Creating harmonious team dynamics and resolving interpersonal conflicts")
            strengths.append("Building trust and psychological safety within teams")
        elif traits["agreeableness"] < -2:
            strengths.append("Providing direct feedback that drives improvement")
            strengths.append("Willingness to challenge ideas and push for better solutions")
        
        if traits["neuroticism"] < -2:
            strengths.append("Emotional resilience during high-pressure situations")
            strengths.append("Stability that provides confidence to others during uncertainty")
        
        # Select 2-3 strengths to return
        if len(strengths) > 3:
            return " \n- ".join(strengths[:3])
        else:
            return " \n- ".join(strengths) if strengths else "Balanced adaptability across different work contexts"
    
    def _get_blind_spots(self, traits):
        """Generate potential blind spots based on trait profile"""
        
        blind_spots = []
        
        if traits["extraversion"] > 2:
            blind_spots.append("May find deep, solitary work draining over extended periods")
            blind_spots.append("Could dominate conversations or overlook quieter colleagues' input")
        elif traits["extraversion"] < -2:
            blind_spots.append("Might miss opportunities that require networking or self-promotion")
            blind_spots.append("Could be perceived as distant or disengaged in team settings")
        
        if traits["conscientiousness"] > 2:
            blind_spots.append("Risk of perfectionism or over-planning that delays progress")
            blind_spots.append("Might struggle when flexibility is needed or processes must change quickly")
        elif traits["conscientiousness"] < -2:
            blind_spots.append("May miss important details or struggle with administrative tasks")
            blind_spots.append("Could find it challenging to maintain consistent routines")
        
        if traits["openness"] > 2:
            blind_spots.append("Might pursue novelty at the expense of practical implementation")
            blind_spots.append("Could become bored with necessary routine aspects of work")
        elif traits["openness"] < -2:
            blind_spots.append("May resist new approaches even when change would be beneficial")
            blind_spots.append("Might miss creative solutions by focusing too much on established methods")
        
        if traits["agreeableness"] > 2:
            blind_spots.append("Could avoid necessary conflict or difficult feedback")
            blind_spots.append("Might prioritize harmony over addressing performance issues")
        elif traits["agreeableness"] < -2:
            blind_spots.append("May create tension through overly direct communication")
            blind_spots.append("Could undervalue emotional needs in team dynamics")
        
        if traits["neuroticism"] > 2:
            blind_spots.append("Might find high-pressure situations more taxing than colleagues do")
            blind_spots.append("Could benefit from stress management techniques during challenging periods")
        
        # Select 2-3 blind spots to return
        if len(blind_spots) > 3:
            return " \n- ".join(blind_spots[:3])
        else:
            return " \n- ".join(blind_spots) if blind_spots else "No significant blind spots identified"
    
    def _get_environment_recommendations(self, traits):
        """Generate environment recommendations based on traits"""
        
        recommendations = []
        
        # Extraversion dimension
        if traits["extraversion"] > 2:
            recommendations.append("Offer regular collaboration and team interaction")
            recommendations.append("Provide opportunities for presentation and leadership")
        elif traits["extraversion"] < -2:
            recommendations.append("Allow for focused independent work without constant interruption")
            recommendations.append("Respect need for quiet spaces and thoughtful communication")
        else:
            recommendations.append("Balance collaborative and independent work")
        
        # Conscientiousness dimension
        if traits["conscientiousness"] > 2:
            recommendations.append("Maintain clear structures, processes, and expectations")
            recommendations.append("Recognize attention to detail and thoroughness")
        elif traits["conscientiousness"] < -2:
            recommendations.append("Offer flexibility in how tasks are approached and completed")
            recommendations.append("Focus on outcomes rather than specific processes")
        else:
            recommendations.append("Provide frameworks while allowing some procedural flexibility")
        
        # Openness dimension
        if traits["openness"] > 2:
            recommendations.append("Encourage innovation and exploration of new approaches")
            recommendations.append("Value creative thinking and conceptual work")
        elif traits["openness"] < -2:
            recommendations.append("Emphasize practical application and proven methodologies")
            recommendations.append("Provide stability and clear direction")
        else:
            recommendations.append("Balance innovation with practical implementation")
        
        # Select 3-4 recommendations to return
        if len(recommendations) > 4:
            return " \n- ".join(recommendations[:4])
        else:
            return " \n- ".join(recommendations)
    
    def _get_results(self):
        """Get the results of the analysis for other agents to use"""
        
        # Normalize trait scores to a -5 to 5 scale
        normalized_traits = {}
        for trait, score in self.trait_scores.items():
            # Clamp scores to a -5 to 5 range
            normalized_traits[trait] = max(-5, min(5, score))
        
        # Determine dominant traits (those with absolute values > 2)
        dominant_traits = {trait: score for trait, score in normalized_traits.items() if abs(score) > 2}
        
        # Create summary of work preferences
        if normalized_traits["extraversion"] > 2:
            social_preference = "collaborative"
        elif normalized_traits["extraversion"] < -2:
            social_preference = "independent"
        else:
            social_preference = "balanced"
            
        if normalized_traits["conscientiousness"] > 2:
            structure_preference = "structured"
        elif normalized_traits["conscientiousness"] < -2:
            structure_preference = "flexible"
        else:
            structure_preference = "moderately structured"
            
        if normalized_traits["openness"] > 2:
            innovation_preference = "innovative"
        elif normalized_traits["openness"] < -2:
            innovation_preference = "conventional"
        else:
            innovation_preference = "balanced innovation"
        
        # Compile results
        results = {
            "trait_scores": normalized_traits,
            "dominant_traits": dominant_traits,
            "work_preferences": {
                "social_style": social_preference,
                "structure_style": structure_preference,
                "innovation_style": innovation_preference
            }
        }
        
        return results