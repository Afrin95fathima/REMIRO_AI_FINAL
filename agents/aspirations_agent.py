import streamlit as st

class AspirationsAgent:
    """
    Aspirations Agent - Career Vision & Legacy Coach
    Helps users define long-term career vision and impact
    """
    
    def __init__(self):
        self.name = "Career Vision & Legacy Coach"
        self.description = "Executive Coach and Career Visionary focusing on your professional legacy"
        self.questions = [
            "Imagine it's your retirement party, and a close colleague is giving a speech about your career. What is the one core achievement or quality you hope they emphasize above all else?",
            "Beyond salary and job title, what would need to be true about your work for you to feel genuinely successful and fulfilled on a daily basis?",
            "What change do you want to bring about in your field, your community, or for your clients? What is the unique impact that only you can make?"
        ]
        self.follow_up_questions = {
            "impact": [
                "When you think about making an impact through your work, is it more important to affect many people in small ways or a few people in profound ways?",
                "Which would be more meaningful to you: Creating something new and innovative, or improving something that already exists to make it better?",
                "If money and practical constraints weren't factors, what kind of impact would you want to make with your work?"
            ],
            "recognition": [
                "How important is external recognition or appreciation in your sense of career fulfillment?",
                "Would you rather be well-known as an expert in a specialized niche, or have broader recognition across different areas?",
                "Think about someone whose career you admire - what specific aspects of their achievement or legacy do you hope to emulate?"
            ],
            "autonomy": [
                "How important is having control over your work - the what, when, how, and why of it?",
                "Would you prefer to set your own vision and direction, or contribute to a larger vision established by others?",
                "How much risk and uncertainty are you comfortable with in pursuit of greater career autonomy?"
            ]
        }
        self.current_question_index = 0
        self.responses = []
        self.aspiration_scores = {
            "impact": 0,
            "recognition": 0,
            "autonomy": 0,
            "mastery": 0,
            "security": 0,
            "connection": 0
        }
        self.follow_up_focus = None
        self.analysis_complete = False
    
    def get_introduction(self):
        """Get the introduction message for this agent"""
        return f"""
        ## Career Vision & Legacy Assessment
        
        I'm your **{self.name}**, {self.description}. I'll help you define a clear 
        and compelling vision for your career by clarifying your definition of "success," 
        your long-range goals, and the impact you wish to create.
        
        Together, we'll develop your career "North Star" that can guide your decisions 
        for years to come.
        
        Let's start with this question: **{self.questions[0]}**
        """
    
    def process_message(self, message):
        """Process user message and return appropriate response"""
        
        # Store the user's response
        self.responses.append(message)
        
        # Analyze the response for aspiration indicators
        self._analyze_response(message)
        
        # If we've gone through all initial questions and any follow-ups
        if self.analysis_complete:
            # Generate and return the final analysis
            final_analysis = self._generate_aspirations_analysis()
            return final_analysis, True, self._get_results()
        
        # Determine if we should move to follow-up questions based on the responses so far
        if len(self.responses) >= 3 and not self.follow_up_focus:
            # Determine which aspiration area to focus follow-up questions on
            self.follow_up_focus = self._determine_follow_up_focus()
        
        # Get the next question
        next_question = self._get_next_question()
        
        # Check if this was the last question
        if next_question is None:
            self.analysis_complete = True
            final_analysis = self._generate_aspirations_analysis()
            return final_analysis, True, self._get_results()
        
        return next_question, False, None
    
    def _analyze_response(self, message):
        """
        Analyze the user's response for aspiration indicators
        This is a simple keyword-based analysis, a real implementation would use NLP
        """
        message_lower = message.lower()
        
        # Impact indicators
        if any(word in message_lower for word in ["impact", "change", "difference", "help", "improve", "better", "world", "society", "community", "environment"]):
            self.aspiration_scores["impact"] += 1
            
        # Recognition indicators
        if any(word in message_lower for word in ["recognition", "respected", "known for", "reputation", "legacy", "remembered", "admired", "expert", "authority", "leader"]):
            self.aspiration_scores["recognition"] += 1
            
        # Autonomy indicators
        if any(word in message_lower for word in ["freedom", "independence", "own", "control", "decide", "choice", "flexible", "autonomy", "self-directed"]):
            self.aspiration_scores["autonomy"] += 1
            
        # Mastery indicators
        if any(word in message_lower for word in ["master", "excel", "best", "expertise", "skill", "craft", "perfect", "quality", "excellence"]):
            self.aspiration_scores["mastery"] += 1
            
        # Security indicators
        if any(word in message_lower for word in ["security", "stable", "reliable", "predictable", "safe", "consistent", "dependable"]):
            self.aspiration_scores["security"] += 1
            
        # Connection indicators
        if any(word in message_lower for word in ["team", "collaborate", "people", "relationships", "connect", "together", "community", "colleagues", "friends"]):
            self.aspiration_scores["connection"] += 1
    
    def _determine_follow_up_focus(self):
        """
        Determine which aspiration area to focus follow-up questions on
        based on the highest scores
        """
        # Find the top aspiration areas
        focus_areas = ["impact", "recognition", "autonomy"]
        scores = [(score, area) for area, score in self.aspiration_scores.items() if area in focus_areas]
        scores.sort(reverse=True)
        
        # Return the highest-scoring focus area
        return scores[0][1] if scores else "impact"  # Default to impact if no clear winner
    
    def _get_next_question(self):
        """Get the next question to ask"""
        
        # If we're doing follow-up questions on a specific aspiration area
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
    
    def _generate_aspirations_analysis(self):
        """Generate an aspirations analysis based on the responses"""
        
        # Get top three aspiration areas
        sorted_aspirations = sorted(self.aspiration_scores.items(), key=lambda x: x[1], reverse=True)
        top_three = sorted_aspirations[:3]
        
        # Generate the analysis
        analysis = f"""
        ## Career Vision & Legacy Analysis
        
        Based on our conversation, I've analyzed what truly drives your career aspirations and what success means to you on a deeper level.
        
        ### Your Key Career Drivers
        
        """
        
        # Add descriptions for top three aspiration areas
        for aspiration, score in top_three:
            analysis += f"- **{aspiration.capitalize()}**: "
            
            if aspiration == "impact":
                analysis += """
                Making a meaningful difference is a core driver in your career vision. You value work that contributes 
                to positive change, whether at the individual, organizational, or societal level. You're likely to find 
                fulfillment in roles where you can clearly see how your efforts improve situations, solve important 
                problems, or enhance people's lives.
                """
            
            elif aspiration == "recognition":
                analysis += """
                Being acknowledged for your contributions and developing a positive professional legacy matters to you. 
                You aspire to be respected for your expertise and the unique value you bring. This doesn't necessarily 
                mean public fame—it could be recognition within your field, organization, or from those you directly serve.
                """
            
            elif aspiration == "autonomy":
                analysis += """
                Having freedom and control over your work is important to you. You value the ability to direct your own path, 
                make key decisions, and have flexibility in how you approach your responsibilities. You're likely to thrive in 
                environments that provide clear objectives but give you latitude in how to achieve them.
                """
            
            elif aspiration == "mastery":
                analysis += """
                Excellence and continuous improvement in your craft drive you. You aspire to develop deep expertise and 
                take pride in the quality of your work. You're likely to find satisfaction in roles that challenge you 
                to keep growing, refining your skills, and producing work you can be proud of.
                """
            
            elif aspiration == "security":
                analysis += """
                Stability and predictability are important elements in your career vision. You value knowing that your 
                position, income, and professional future have a solid foundation. You're likely to appreciate environments 
                that offer clear structures, reliable processes, and long-term prospects.
                """
            
            elif aspiration == "connection":
                analysis += """
                Meaningful relationships and collaboration energize your work. You value being part of a community or team 
                and find fulfillment in the human aspects of your professional life. You're likely to thrive in environments 
                with strong cultural alignment, supportive colleagues, and opportunities for meaningful interaction.
                """
        
        # Synthesize a North Star statement based on top drivers
        north_star = self._generate_north_star(top_three)
        
        # Generate timeline perspectives
        short_term, long_term = self._generate_timeline_perspectives(top_three)
        
        analysis += f"""
        ### Your Career North Star
        
        {north_star}
        
        This North Star statement encapsulates the essence of what would make work deeply fulfilling for you, beyond titles and compensation.
        
        ### Timeline Perspectives
        
        **Short-term (1-3 years):**
        {short_term}
        
        **Long-term (10+ years):**
        {long_term}
        
        ### Reflection Questions to Keep Your Vision Clear
        
        As you navigate future career decisions, ask yourself:
        
        1. Does this opportunity align with my definition of meaningful work?
        2. Will this path allow me to create the kind of impact I find fulfilling?
        3. How does this choice position me to build the professional legacy I desire?
        
        Remember that your career vision may evolve over time, and that's perfectly natural. This analysis provides a snapshot 
        of what matters to you now, which can serve as a valuable compass as you navigate your next career moves.
        """
        
        return analysis
    
    def _generate_north_star(self, top_aspirations):
        """Generate a North Star statement based on top aspirations"""
        
        # Extract the aspiration types
        aspiration_types = [a[0] for a in top_aspirations]
        
        # Different templates based on combinations of top aspirations
        if "impact" in aspiration_types and "mastery" in aspiration_types:
            return """
            "To apply my growing expertise in ways that create meaningful, positive change, continuously improving 
            both my capabilities and the value I deliver to others."
            """
            
        elif "impact" in aspiration_types and "recognition" in aspiration_types:
            return """
            "To be recognized as someone whose work consistently makes a significant difference, building a legacy 
            of meaningful contributions that positively affect others."
            """
            
        elif "impact" in aspiration_types and "autonomy" in aspiration_types:
            return """
            "To have the freedom to pursue work that creates meaningful change on my own terms, directing my talents 
            toward challenges where I can make a genuine difference."
            """
            
        elif "recognition" in aspiration_types and "mastery" in aspiration_types:
            return """
            "To be respected for exceptional expertise in my field, continually refining my skills and being acknowledged 
            as someone who produces work of the highest quality."
            """
            
        elif "autonomy" in aspiration_types and "mastery" in aspiration_types:
            return """
            "To have the freedom to pursue excellence on my own terms, continuously deepening my expertise while 
            maintaining control over how I apply my skills and direct my professional growth."
            """
            
        elif "connection" in aspiration_types and "impact" in aspiration_types:
            return """
            "To work collaboratively with others to create meaningful change, building strong relationships that 
            enhance both the quality of my work experience and the positive difference we make together."
            """
            
        elif "security" in aspiration_types:
            return """
            "To build a stable, sustainable career path that provides reliable foundations while still allowing me 
            to find fulfillment through " + ("impact" if "impact" in aspiration_types else "meaningful work") + "."
            """
            
        else:
            # Default template combining the top three in a generic way
            aspects = []
            for aspect, _ in top_aspirations:
                if aspect == "impact":
                    aspects.append("make a meaningful difference")
                elif aspect == "recognition":
                    aspects.append("be recognized for my contributions")
                elif aspect == "autonomy":
                    aspects.append("have freedom in directing my work")
                elif aspect == "mastery":
                    aspects.append("excel through continuous improvement")
                elif aspect == "security":
                    aspects.append("build stable professional foundations")
                elif aspect == "connection":
                    aspects.append("collaborate within meaningful relationships")
            
            return f""""To {aspects[0]}, while finding ways to {aspects[1]} and {aspects[2]}, creating a career 
            that aligns with my deepest values and aspirations."""
    
    def _generate_timeline_perspectives(self, top_aspirations):
        """Generate short and long term perspectives based on top aspirations"""
        
        # Extract the aspiration types
        aspiration_types = [a[0] for a in top_aspirations]
        
        # Short-term perspective
        short_term = "Focus on building foundations that align with your core drivers: "
        if "impact" in aspiration_types:
            short_term += "Seek opportunities to create tangible, measurable positive outcomes, even at a small scale. "
        if "recognition" in aspiration_types:
            short_term += "Start establishing your reputation in specific areas by developing focused expertise and sharing your work. "
        if "autonomy" in aspiration_types:
            short_term += "Find or create pockets of independence within your current or future roles. "
        if "mastery" in aspiration_types:
            short_term += "Develop deliberate practice routines to steadily improve your key skills. "
        if "connection" in aspiration_types:
            short_term += "Build a supportive network of meaningful professional relationships. "
        if "security" in aspiration_types:
            short_term += "Establish reliable income streams while building versatile, marketable skills. "
            
        # Long-term perspective
        long_term = "Position yourself to maximize fulfillment through: "
        if "impact" in aspiration_types:
            long_term += "Creating systems, products, or initiatives with far-reaching or lasting positive effects. "
        if "recognition" in aspiration_types:
            long_term += "Becoming a recognized voice or authority in your area of expertise. "
        if "autonomy" in aspiration_types:
            long_term += "Structuring your career to give you significant control over your work, whether through entrepreneurship, seniority, or specialized expertise. "
        if "mastery" in aspiration_types:
            long_term += "Reaching advanced levels of expertise that allow you to innovate and set standards in your field. "
        if "connection" in aspiration_types:
            long_term += "Creating or leading communities where meaningful collaboration drives both personal satisfaction and exceptional outcomes. "
        if "security" in aspiration_types:
            long_term += "Establishing multiple sources of professional value that provide stability regardless of market or industry changes. "
        
        return short_term, long_term
    
    def _get_results(self):
        """Get the results of the analysis for other agents to use"""
        
        # Get top three aspiration areas
        sorted_aspirations = sorted(self.aspiration_scores.items(), key=lambda x: x[1], reverse=True)
        top_three = [area for area, _ in sorted_aspirations[:3]]
        
        # Interpret responses to create career vision elements
        if len(self.responses) >= 3:
            achievement_focus = self.responses[0][:100] + "..." if len(self.responses[0]) > 100 else self.responses[0]
            daily_fulfillment = self.responses[1][:100] + "..." if len(self.responses[1]) > 100 else self.responses[1]
            impact_focus = self.responses[2][:100] + "..." if len(self.responses[2]) > 100 else self.responses[2]
        else:
            achievement_focus = "Career achievement and recognition"
            daily_fulfillment = "Meaningful and engaging work"
            impact_focus = "Making a positive difference"
        
        # Determine short and long-term focus based on responses
        short_term_goals = []
        long_term_goals = []
        
        if "impact" in top_three:
            short_term_goals.append("Finding opportunities for meaningful contribution")
            long_term_goals.append("Creating lasting positive change")
        
        if "recognition" in top_three:
            short_term_goals.append("Building expertise and visibility")
            long_term_goals.append("Establishing professional legacy and authority")
        
        if "autonomy" in top_three:
            short_term_goals.append("Increasing control over work processes")
            long_term_goals.append("Achieving significant professional independence")
        
        if "mastery" in top_three:
            short_term_goals.append("Deliberate skill improvement")
            long_term_goals.append("Becoming an expert in chosen specialty")
        
        if "security" in top_three:
            short_term_goals.append("Establishing reliable income and stability")
            long_term_goals.append("Building long-term financial and professional security")
        
        if "connection" in top_three:
            short_term_goals.append("Cultivating meaningful professional relationships")
            long_term_goals.append("Building or leading collaborative communities")
        
        # Compile results
        results = {
            "aspiration_scores": self.aspiration_scores,
            "top_aspirations": top_three,
            "career_vision": {
                "achievement_focus": achievement_focus,
                "daily_fulfillment": daily_fulfillment,
                "impact_focus": impact_focus
            },
            "short_term_goals": short_term_goals,
            "long_term_goals": long_term_goals
        }
        
        return results