import streamlit as st

class IdentityAgent:
    """
    Identity Agent - Personal Brand Strategist
    Develops authentic personal branding aligned with career goals
    """
    
    def __init__(self):
        self.name = "Personal Brand Strategist"
        self.description = "Personal identity and brand architect"
        self.questions = [
            "How would you describe your professional identity today? What are the key elements that define you professionally?",
            "What aspects of your professional identity do you feel are most authentic to who you really are?",
            "What professional reputation or personal brand would you like to build or strengthen?",
            "What unique perspectives, experiences, or qualities do you bring that differentiate you from others in your field?"
        ]
        self.current_question_index = 0
        self.responses = []
        self.current_identity = []
        self.authentic_elements = []
        self.target_identity = []
        self.differentiators = []
        self.brand_archetypes = {}
        self.selected_archetype = None
        self.analysis_complete = False
    
    def get_introduction(self):
        """Get the introduction message for this agent"""
        return f"""
        ## Personal Identity Assessment
        
        I'm your **{self.name}**, {self.description}. I'll help you develop an authentic, 
        compelling personal brand that aligns with your career aspirations.
        
        Your professional identity shapes how you're perceived and the opportunities that come your way. 
        Let's discover how to express your unique value proposition in a way that resonates with your 
        target audience while staying true to your authentic self.
        
        Let's start with this question: **{self.questions[0]}**
        """
    
    def process_message(self, message):
        """Process user message and return appropriate response"""
        
        # Store the user's response
        self.responses.append(message)
        
        # Analyze the response
        self._analyze_response(len(self.responses) - 1, message)
        
        # Check if we've gone through all questions
        if len(self.responses) >= len(self.questions):
            # Generate the final analysis
            self.analysis_complete = True
            final_analysis = self._generate_identity_analysis()
            return final_analysis, True, self._get_results()
        
        # Get the next question
        next_question = self._get_next_question()
        
        return next_question, False, None
    
    def _analyze_response(self, question_index, message):
        """
        Analyze the user's response based on which question was asked
        This is a simple keyword-based analysis, a real implementation would use NLP
        """
        message_lower = message.lower()
        
        # First question: Current professional identity
        if question_index == 0:
            identity_keywords = [
                # Professional roles
                "developer", "designer", "manager", "director", "specialist", "analyst", "consultant",
                "engineer", "executive", "founder", "entrepreneur", "researcher", "scientist", "educator",
                "teacher", "professor", "doctor", "lawyer", "accountant", "marketer", "writer", "artist",
                "leader", "coach", "mentor", "coordinator", "administrator", "technician", "assistant",
                # Professional characteristics
                "innovative", "creative", "analytical", "strategic", "detail-oriented", "visionary", 
                "technical", "practical", "experienced", "expert", "knowledgeable", "skilled", 
                "collaborative", "independent", "versatile", "adaptable", "organized", "efficient",
                "communicator", "problem-solver", "decision-maker", "influencer", "negotiator",
                # Industries and fields
                "tech", "technology", "healthcare", "finance", "education", "marketing", "sales", 
                "design", "manufacturing", "retail", "hospitality", "non-profit", "government", 
                "entertainment", "media", "fashion", "automotive", "aerospace", "construction", 
                "energy", "telecommunications", "consulting", "legal", "real estate"
            ]
            
            for keyword in identity_keywords:
                if keyword in message_lower and keyword not in self.current_identity:
                    self.current_identity.append(keyword)
            
            # Extract phrases with "I am" or "I'm"
            import re
            i_am_phrases = re.findall(r'I am [a-z ]+ [a-z]+|I\'m [a-z ]+ [a-z]+', message_lower)
            for phrase in i_am_phrases:
                identity_phrase = phrase.replace('i am ', '').replace('i\'m ', '')
                if identity_phrase and identity_phrase not in self.current_identity:
                    self.current_identity.append(identity_phrase)
        
        # Second question: Authentic elements
        elif question_index == 1:
            authenticity_keywords = {
                "passion": ["passion", "passionate", "love", "enjoy", "enthusiastic", "excited", "energized"],
                "values": ["value", "values", "important", "belief", "believe", "principle", "integrity", "ethics"],
                "strengths": ["strength", "good at", "excel", "skilled", "natural", "talent", "gifted", "capability"],
                "personality": ["personality", "character", "nature", "temperament", "style", "approach", "demeanor"],
                "purpose": ["purpose", "mission", "calling", "meaningful", "meaning", "impact", "difference", "contribution"],
                "story": ["story", "journey", "experience", "background", "history", "path", "narrative"]
            }
            
            for element, keywords in authenticity_keywords.items():
                for keyword in keywords:
                    if keyword in message_lower and element not in self.authentic_elements:
                        self.authentic_elements.append(element)
                        break
            
            # Extract phrases with "truly me" or "authentic self" or similar
            authentic_phrases = ["truly me", "authentic self", "real me", "genuine", "true to myself", "natural for me", "who i really am"]
            for phrase in authentic_phrases:
                if phrase in message_lower:
                    # Look for surrounding context
                    index = message_lower.find(phrase)
                    start = max(0, index - 30)
                    end = min(len(message_lower), index + 30)
                    context = message_lower[start:end]
                    
                    # Extract words that might represent authentic elements
                    import re
                    words = re.findall(r'\b[a-z]{5,}\b', context)
                    for word in words:
                        if word not in self.authentic_elements and word not in ["truly", "authentic", "genuine", "natural", "really"]:
                            self.authentic_elements.append(word)
        
        # Third question: Target identity/reputation
        elif question_index == 2:
            target_keywords = [
                # Professional aspirations
                "expert", "authority", "thought leader", "innovator", "pioneer", "specialist", "trusted advisor",
                "influencer", "connector", "visionary", "change agent", "mentor", "strategic partner",
                # Reputation qualities
                "reliable", "creative", "innovative", "knowledgeable", "skilled", "professional", "ethical",
                "collaborative", "influential", "impactful", "respected", "recognized", "accomplished",
                "forward-thinking", "cutting-edge", "dynamic", "approachable", "articulate", "dedicated"
            ]
            
            for keyword in target_keywords:
                if keyword in message_lower and keyword not in self.target_identity:
                    self.target_identity.append(keyword)
            
            # Extract phrases with "want to be known for" or "want to be seen as" or similar
            aspiration_phrases = ["want to be known", "like to be seen", "aim to be", "aspire to be", "goal is to be", "hope to be recognized", "build a reputation"]
            for phrase in aspiration_phrases:
                if phrase in message_lower:
                    # Look for surrounding context
                    index = message_lower.find(phrase)
                    start = max(0, index - 5)
                    end = min(len(message_lower), index + 50)
                    context = message_lower[start:end]
                    
                    # Extract words that might represent target elements
                    import re
                    context_words = re.findall(r'\b[a-z]{5,}\b', context)
                    for word in context_words:
                        if word not in self.target_identity and word not in ["known", "recognized", "reputation"]:
                            self.target_identity.append(word)
        
        # Fourth question: Differentiators
        elif question_index == 3:
            differentiator_keywords = [
                # Unique attributes
                "unique", "different", "distinctive", "special", "rare", "uncommon", "unusual", "exceptional",
                "extraordinary", "remarkable", "standout", "one-of-a-kind", "niche", "specialized",
                # Competitive advantages
                "advantage", "perspective", "approach", "background", "experience", "expertise", "skill set",
                "combination", "insight", "education", "training", "certification", "qualification",
                # Personal qualities
                "strength", "talent", "gift", "ability", "passion", "drive", "enthusiasm", "creativity",
                "innovation", "adaptability", "resilience", "determination", "dedication", "commitment"
            ]
            
            for keyword in differentiator_keywords:
                if keyword in message_lower and keyword not in self.differentiators:
                    self.differentiators.append(keyword)
            
            # Extract phrases with "sets me apart" or "makes me different" or similar
            differentiator_phrases = ["sets me apart", "makes me different", "unique about me", "different from others", "stand out", "differentiates me", "competitive advantage"]
            for phrase in differentiator_phrases:
                if phrase in message_lower:
                    # Look for surrounding context
                    index = message_lower.find(phrase)
                    start = max(0, index - 20)
                    end = min(len(message_lower), index + 50)
                    context = message_lower[start:end]
                    
                    # Extract potential differentiators
                    import re
                    for word in re.findall(r'\b[a-z]{5,}\b', context):
                        if word not in self.differentiators and word not in ["apart", "different", "unique", "others", "stand", "differentiate", "competitive"]:
                            self.differentiators.append(word)
    
    def _get_next_question(self):
        """Get the next question to ask"""
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            return f"**{self.questions[self.current_question_index]}**"
        else:
            return None
    
    def _identify_brand_archetype(self):
        """
        Identify potential brand archetypes based on responses
        This is a simplified implementation - a real one would be more sophisticated
        """
        # Define 12 brand archetypes with attributes
        archetypes = {
            "The Sage": {
                "traits": ["knowledgeable", "expert", "analytical", "thoughtful", "advisor", "wisdom", "intelligence", "truth", "understanding", "insight", "research", "information", "expertise"],
                "description": "Values knowledge, truth, and understanding. Helps others make sense of the world through expertise and insight.",
                "strengths": ["Deep expertise", "Thoughtful analysis", "Wisdom", "Clarity of thought", "Credibility", "Intellectual leadership"],
                "examples": ["Academic experts", "Researchers", "Thought leaders", "Advisors", "Analysts"],
                "communication": ["Educational content", "Research findings", "Analysis", "Expert opinions", "Thoughtful perspectives"],
                "score": 0
            },
            "The Creator": {
                "traits": ["creative", "innovative", "artistic", "designer", "imagination", "originality", "visionary", "expressive", "craftsmanship", "invention", "design"],
                "description": "Values self-expression, innovation, and originality. Creates things of enduring value and brings new ideas to life.",
                "strengths": ["Innovation", "Originality", "Artistic vision", "Design thinking", "Creative problem-solving"],
                "examples": ["Designers", "Artists", "Innovators", "Inventors", "Content creators"],
                "communication": ["Creative portfolios", "Innovative solutions", "Artistic expressions", "Original perspectives", "Design showcases"],
                "score": 0
            },
            "The Ruler": {
                "traits": ["leader", "authority", "control", "executive", "organized", "structured", "power", "influence", "command", "director", "manager", "orderly", "systematic"],
                "description": "Values order, structure, and control. Creates stable and successful environments through leadership and organization.",
                "strengths": ["Leadership", "Organization", "Strategic thinking", "Authority", "Decision-making", "Executive presence"],
                "examples": ["Executives", "Leaders", "Managers", "Directors", "Administrators"],
                "communication": ["Strategic visions", "Authoritative statements", "Leadership perspectives", "Organizational frameworks", "Governance insights"],
                "score": 0
            },
            "The Caregiver": {
                "traits": ["helpful", "supportive", "nurturing", "service", "compassionate", "empathetic", "caring", "protective", "generous", "coach", "mentor"],
                "description": "Values service and protection of others. Helps and supports through compassion, generosity, and selflessness.",
                "strengths": ["Empathy", "Supportiveness", "Service orientation", "Relationship building", "Trust creation"],
                "examples": ["Coaches", "Mentors", "Healthcare professionals", "Support specialists", "Service providers"],
                "communication": ["Supportive guidance", "Helpful resources", "Nurturing advice", "Service offerings", "Empathetic responses"],
                "score": 0
            },
            "The Explorer": {
                "traits": ["adventurous", "independent", "pioneering", "discovery", "freedom", "journey", "curious", "experimental", "trailblazer", "seeker", "authentic"],
                "description": "Values freedom, discovery, and authenticity. Pushes boundaries and explores new territories and possibilities.",
                "strengths": ["Independence", "Curiosity", "Adaptability", "Pioneering spirit", "Authenticity", "Discovery orientation"],
                "examples": ["Entrepreneurs", "Researchers", "Consultants", "Adventure-seekers", "Innovators"],
                "communication": ["Journey narratives", "Discovery stories", "Authentic experiences", "Novel approaches", "Exploration insights"],
                "score": 0
            },
            "The Rebel": {
                "traits": ["disruptive", "revolutionary", "challenger", "unconventional", "rule-breaker", "bold", "provocative", "radical", "transformative", "counter-culture"],
                "description": "Values revolution and disruption of the status quo. Challenges conventions and drives radical change.",
                "strengths": ["Disruption", "Challenging norms", "Bold action", "Revolutionary thinking", "Game-changing approaches"],
                "examples": ["Disruptors", "Change agents", "Activists", "Revolutionaries", "Unconventional thinkers"],
                "communication": ["Provocative statements", "Challenging perspectives", "Disruptive ideas", "Radical proposals", "Status quo critiques"],
                "score": 0
            },
            "The Magician": {
                "traits": ["transformative", "visionary", "catalyst", "facilitator", "change agent", "inspirational", "transformational", "charismatic", "influential", "alchemist"],
                "description": "Values transformation and making dreams reality. Creates transformative experiences and catalyzes meaningful change.",
                "strengths": ["Vision casting", "Transformation facilitation", "Charisma", "Inspiring others", "Creating change"],
                "examples": ["Transformational leaders", "Visionaries", "Facilitators", "Change consultants", "Inspirational speakers"],
                "communication": ["Visionary statements", "Transformational frameworks", "Inspiring stories", "Change methodologies", "Future casting"],
                "score": 0
            },
            "The Hero": {
                "traits": ["courageous", "determined", "achiever", "champion", "overcomer", "bold", "brave", "tenacious", "strong", "protector", "defender"],
                "description": "Values courage, achievement, and victory. Rises to challenges and inspires through determination and mastery.",
                "strengths": ["Courage", "Determination", "Achievement orientation", "Mastery", "Overcoming obstacles"],
                "examples": ["Champions", "High-achievers", "Defenders", "Athletes", "Problem-solvers"],
                "communication": ["Achievement stories", "Challenge narratives", "Victory accounts", "Mastery demonstrations", "Inspirational struggles"],
                "score": 0
            },
            "The Regular Person": {
                "traits": ["relatable", "practical", "down-to-earth", "accessible", "inclusive", "everyday", "approachable", "common sense", "pragmatic", "straightforward", "unpretentious"],
                "description": "Values belonging, practicality, and connection. Creates accessible solutions and fosters inclusion and community.",
                "strengths": ["Relatability", "Practical approach", "Accessibility", "Community building", "Common sense"],
                "examples": ["Connectors", "Community builders", "Practical problem solvers", "Inclusive leaders", "Team players"],
                "communication": ["Relatable stories", "Practical advice", "Accessible insights", "Inclusive messages", "Common experiences"],
                "score": 0
            },
            "The Lover": {
                "traits": ["passionate", "relationship-focused", "appreciative", "connected", "intimate", "quality-focused", "sensory", "enjoyment", "beauty", "aesthetics", "pleasure"],
                "description": "Values relationships, connection, and aesthetic experiences. Creates beauty and fosters deep connections and appreciation.",
                "strengths": ["Relationship building", "Appreciation", "Sensory engagement", "Quality focus", "Aesthetic sensibility"],
                "examples": ["Relationship experts", "Experience designers", "Quality specialists", "Aesthetics professionals", "Connection facilitators"],
                "communication": ["Relationship insights", "Quality demonstrations", "Aesthetic presentations", "Appreciation expressions", "Sensory experiences"],
                "score": 0
            },
            "The Jester": {
                "traits": ["humorous", "playful", "entertaining", "fun", "witty", "lighthearted", "joy", "clever", "engaging", "amusing", "enjoyable"],
                "description": "Values enjoyment, humor, and lightness. Brings joy through playfulness, wit, and entertainment.",
                "strengths": ["Humor", "Engagement", "Lightness", "Entertainment value", "Memorability"],
                "examples": ["Entertainers", "Engagers", "Creative communicators", "Experience designers", "Presenters"],
                "communication": ["Humorous content", "Playful messaging", "Engaging presentations", "Entertaining formats", "Joy-inducing experiences"],
                "score": 0
            },
            "The Innocent": {
                "traits": ["optimistic", "honest", "ethical", "transparent", "simple", "pure", "trustworthy", "genuine", "authentic", "idealistic", "positive", "hopeful"],
                "description": "Values simplicity, goodness, and optimism. Creates trust through authenticity, transparency, and ethical approaches.",
                "strengths": ["Trust creation", "Optimism", "Ethical stance", "Simplicity", "Authenticity"],
                "examples": ["Trust builders", "Ethical leaders", "Authenticity experts", "Simplicity advocates", "Positive influencers"],
                "communication": ["Transparent messages", "Ethical frameworks", "Simple explanations", "Authentic stories", "Optimistic visions"],
                "score": 0
            }
        }
        
        # Analyze all responses together for archetype scoring
        all_responses = ' '.join(self.responses).lower()
        
        # Score archetypes based on traits found in responses
        for archetype, attributes in archetypes.items():
            score = 0
            for trait in attributes["traits"]:
                if trait in all_responses:
                    score += 1
            
            # Additional scoring based on extracted elements
            for element in self.current_identity + self.authentic_elements + self.target_identity + self.differentiators:
                if element in attributes["traits"]:
                    score += 2
            
            archetypes[archetype]["score"] = score
        
        # Find primary and secondary archetypes
        sorted_archetypes = sorted(archetypes.items(), key=lambda x: x[1]["score"], reverse=True)
        primary_archetype = sorted_archetypes[0][0]
        secondary_archetype = sorted_archetypes[1][0] if sorted_archetypes[1][1]["score"] > 0 else None
        
        # Store all archetypes with scores for future reference
        self.brand_archetypes = {name: details for name, details in sorted_archetypes}
        
        # Store selected archetype
        self.selected_archetype = primary_archetype
        
        return primary_archetype, secondary_archetype, archetypes[primary_archetype], archetypes.get(secondary_archetype, None)
    
    def _generate_identity_analysis(self):
        """Generate a personal identity analysis based on the responses"""
        
        # First identify brand archetypes
        primary_archetype, secondary_archetype, primary_details, secondary_details = self._identify_brand_archetype()
        
        # Generate the analysis
        analysis = f"""
        ## Personal Identity Analysis
        
        Based on our conversation, I've analyzed the elements of your current and desired professional 
        identity to help you develop an authentic, compelling personal brand that aligns with your career aspirations.
        
        ### Current Professional Identity
        
        Your current professional identity includes these key elements:
        """
        
        if self.current_identity:
            for identity in self.current_identity[:5]:  # Show top 5
                analysis += f"\n- **{identity.capitalize()}**"
        else:
            analysis += "\nYou haven't specified clear elements of your current professional identity."
        
        analysis += "\n\n### Authentic Core Elements"
        
        if self.authentic_elements:
            analysis += "\n\nThese elements of your identity feel most authentic to you:"
            for element in self.authentic_elements[:5]:  # Show top 5
                analysis += f"\n- **{element.capitalize()}**"
        else:
            analysis += "\n\nYou haven't specified which elements feel most authentic to you."
        
        analysis += "\n\n### Target Brand Identity"
        
        if self.target_identity:
            analysis += "\n\nYou aspire to build or strengthen a professional reputation as:"
            for identity in self.target_identity[:5]:  # Show top 5
                analysis += f"\n- **{identity.capitalize()}**"
        else:
            analysis += "\n\nYou haven't specified clear aspirations for your professional reputation."
        
        analysis += "\n\n### Key Differentiators"
        
        if self.differentiators:
            analysis += "\n\nYour unique qualities or perspectives that set you apart include:"
            for differentiator in self.differentiators[:5]:  # Show top 5
                analysis += f"\n- **{differentiator.capitalize()}**"
        else:
            analysis += "\n\nYou haven't specified clear differentiators that set you apart."
        
        # Brand archetype analysis
        analysis += f"""
        
        ### Brand Archetype Analysis
        
        Based on your responses, your primary brand archetype appears to be **{primary_archetype}**.
        
        **{primary_archetype}** Archetype:
        {primary_details["description"]}
        
        **Key Strengths of This Archetype:**
        """
        
        for strength in primary_details["strengths"][:4]:  # Show top 4 strengths
            analysis += f"\n- {strength}"
        
        analysis += f"""
        
        **Professional Examples:**
        """
        
        for example in primary_details["examples"][:3]:  # Show top 3 examples
            analysis += f"\n- {example}"
        
        if secondary_archetype and secondary_details:
            analysis += f"""
            
            Your secondary brand archetype appears to be **{secondary_archetype}**, which complements your primary archetype by adding dimensions of {", ".join(secondary_details["traits"][:3])}.
            """
        
        # Brand alignment analysis
        alignment_score = 0
        alignment_strengths = []
        alignment_gaps = []
        
        # Check alignment between current and target identity
        current_set = set(self.current_identity)
        target_set = set(self.target_identity)
        authentic_set = set(self.authentic_elements)
        
        overlap_current_target = current_set.intersection(target_set)
        overlap_authentic_target = authentic_set.intersection(target_set)
        
        gaps_current_target = target_set.difference(current_set)
        gaps_authentic_target = target_set.difference(authentic_set)
        
        # Calculate alignment score (simplified)
        if target_set:
            alignment_score += (len(overlap_current_target) / len(target_set)) * 50
            alignment_score += (len(overlap_authentic_target) / len(target_set)) * 50
        else:
            alignment_score = 50  # Default middle score
        
        # Identify alignment strengths and gaps
        for item in overlap_current_target.union(overlap_authentic_target):
            if item not in alignment_strengths:
                alignment_strengths.append(item)
        
        for item in gaps_current_target.union(gaps_authentic_target):
            if item not in alignment_gaps:
                alignment_gaps.append(item)
        
        analysis += f"""
        
        ### Brand Alignment Analysis
        
        **Alignment Score: {int(alignment_score)}%**
        
        This score reflects how well your current identity and authentic elements align with your target professional reputation.
        """
        
        if alignment_strengths:
            analysis += "\n\n**Alignment Strengths:**\n"
            for strength in alignment_strengths[:3]:  # Show top 3
                analysis += f"- Your identity already embodies **{strength}**, which aligns with your target reputation\n"
        
        if alignment_gaps:
            analysis += "\n**Alignment Opportunities:**\n"
            for gap in alignment_gaps[:3]:  # Show top 3
                analysis += f"- You aim to be known for **{gap}**, which may require intentional development or expression\n"
        
        # Personal brand strategy
        analysis += """
        
        ### Personal Brand Strategy
        
        Based on this analysis, here's a framework for developing your authentic personal brand:
        
        #### 1. Core Identity Foundation
        """
        
        # Core identity recommendations
        if self.authentic_elements:
            authentic_core = self.authentic_elements[:3]
            analysis += "\nCenter your brand on these authentic core elements:\n"
            for element in authentic_core:
                analysis += f"- **{element.capitalize()}**: Express this through consistent messaging and demonstrations\n"
        else:
            analysis += """
            Identify and prioritize the aspects of your professional identity that:
            - Energize you rather than drain you
            - Feel natural rather than forced
            - Have been consistently present throughout your career journey
            - Reflect your genuine strengths and values
            """
        
        # Target positioning recommendations
        analysis += "\n#### 2. Strategic Positioning\n"
        
        if self.target_identity and self.differentiators:
            target_elements = self.target_identity[:2]
            differentiator_elements = self.differentiators[:2]
            
            analysis += f"""
            Position yourself at the intersection of what you want to be known for and what makes you unique:
            
            "The **{target_elements[0]}** with **{differentiator_elements[0]}**" or
            "The professional who brings **{target_elements[1] if len(target_elements) > 1 else target_elements[0]}** through a unique **{differentiator_elements[1] if len(differentiator_elements) > 1 else differentiator_elements[0]}** approach"
            """
        else:
            analysis += """
            Create a positioning statement that combines:
            - The professional identity you aspire to
            - Your unique perspective or approach that differentiates you
            - The specific value this creates for others
            """
        
        # Brand expression recommendations based on archetype
        analysis += f"\n#### 3. Brand Expression as {primary_archetype}\n"
        
        analysis += "Express your brand through these communication approaches:\n"
        
        for comm in primary_details["communication"][:3]:
            analysis += f"- **{comm}**: "
            
            if "Educational" in comm or "Research" in comm or "Analysis" in comm:
                analysis += "Share insights, research, and thoughtful perspectives that demonstrate expertise\n"
            elif "Creative" in comm or "Innovative" in comm or "Artistic" in comm or "Design" in comm:
                analysis += "Showcase your creative process, innovative solutions, and unique design thinking\n"
            elif "Strategic" in comm or "Leadership" in comm or "Authority" in comm:
                analysis += "Articulate clear visions, definitive viewpoints, and structured frameworks\n"
            elif "Supportive" in comm or "Helpful" in comm or "Nurturing" in comm or "Service" in comm:
                analysis += "Offer guidance, resources, and assistance that demonstrate your service orientation\n"
            elif "Journey" in comm or "Discovery" in comm or "Authentic" in comm or "Novel" in comm:
                analysis += "Share stories of exploration, discovery, and authentic experiences in your field\n"
            elif "Provocative" in comm or "Challenging" in comm or "Disruptive" in comm or "Radical" in comm:
                analysis += "Present alternative perspectives and challenge conventional wisdom in your industry\n"
            elif "Visionary" in comm or "Transform" in comm or "Inspiring" in comm or "Change" in comm:
                analysis += "Articulate compelling future visions and transformational possibilities\n"
            elif "Achievement" in comm or "Challenge" in comm or "Victory" in comm or "Mastery" in comm:
                analysis += "Document your process of overcoming obstacles and achieving meaningful results\n"
            elif "Relatable" in comm or "Practical" in comm or "Accessible" in comm or "Common" in comm:
                analysis += "Offer straightforward, practical insights that connect with everyday experiences\n"
            elif "Relationship" in comm or "Quality" in comm or "Aesthetic" in comm or "Appreciation" in comm:
                analysis += "Focus on quality, beauty, and meaningful connections in your communications\n"
            elif "Humorous" in comm or "Playful" in comm or "Engaging" in comm or "Entertaining" in comm:
                analysis += "Incorporate wit, playfulness, and enjoyment into your professional communications\n"
            elif "Transparent" in comm or "Ethical" in comm or "Simple" in comm or "Authentic" in comm:
                analysis += "Emphasize straightforward, ethical approaches and transparent communications\n"
            else:
                analysis += "Integrate this into your regular professional communications\n"
        
        # Communication channel recommendations
        analysis += "\n#### 4. Strategic Visibility Plan\n"
        
        analysis += """
        Build your brand visibility through these approaches:
        
        1. **Content Creation Strategy**
           - Develop a content mix that showcases your expertise and authentic voice
           - Focus on quality over quantity, with consistency in theme and timing
           - Choose formats that align with your strengths (writing, speaking, visual, etc.)
        
        2. **Platform Selection**
           - Identify 2-3 primary platforms where your target audience engages
           - Adapt your content strategy to each platform's unique environment
           - Build meaningful presence rather than spreading yourself too thin
        
        3. **Relationship Building**
           - Move beyond broadcast communication to meaningful engagement
           - Create opportunities for two-way dialogue with your audience
           - Cultivate relationships with strategic connections in your field
        
        4. **Credibility Building**
           - Identify opportunities to demonstrate your expertise
           - Seek validation through appropriate credentials, testimonials, or endorsements
           - Document and share evidence of your impact and results
        """
        
        # Brand evolution strategy
        analysis += """
        
        #### 5. Brand Evolution Strategy
        
        Your professional identity should evolve intentionally:
        
        1. **Regular Self-Assessment**
           - Schedule quarterly reviews of how well your expressed identity matches your authentic self
           - Assess whether your brand is creating the opportunities you desire
           - Identify areas where your brand may need refinement or evolution
        
        2. **Feedback Integration**
           - Seek specific feedback on how others perceive your professional identity
           - Look for patterns in how people describe you or introduce you to others
           - Identify gaps between intended and received brand impressions
        
        3. **Strategic Pivoting**
           - When evolving your brand, maintain core authentic elements while shifting emphasis
           - Signal intentional evolution rather than erratic repositioning
           - Create narrative bridges between your previous and emerging identity
        """
        
        # Authenticity safeguards
        analysis += """
        
        ### Authenticity Safeguards
        
        As you develop your professional identity, use these questions to maintain authenticity:
        
        1. **Energy Check**: Does expressing this aspect of my identity energize me or drain me?
        2. **Consistency Test**: Is this consistent with my values and natural way of being?
        3. **Longevity Assessment**: Can I sustain this identity expression over the long term?
        4. **Integrated Self**: Does this allow me to bring my whole self to my professional life?
        5. **Internal Alignment**: Does this feel like an expression of who I am, not just what I do?
        
        Remember that the most powerful personal brands emerge from the intersection of:
        - What you're genuinely good at (your strengths)
        - What feels natural and energizing (your authentic self)
        - What creates value for others (your contribution)
        
        By building a brand at this intersection, you create a sustainable professional identity that attracts the right opportunities while allowing you to work from a place of authenticity.
        """
        
        return analysis
    
    def _get_results(self):
        """Get the results of the analysis for other agents to use"""
        
        # Format current identity
        current = [identity.capitalize() for identity in self.current_identity]
        
        # Format authentic elements
        authentic = [element.capitalize() for element in self.authentic_elements]
        
        # Format target identity
        target = [identity.capitalize() for identity in self.target_identity]
        
        # Format differentiators
        differentiators = [diff.capitalize() for diff in self.differentiators]
        
        # Get top 3 archetype matches
        top_archetypes = sorted(self.brand_archetypes.items(), key=lambda x: x[1]["score"], reverse=True)[:3]
        archetype_results = {}
        for archetype, details in top_archetypes:
            if details["score"] > 0:
                archetype_results[archetype] = {
                    "score": details["score"],
                    "description": details["description"],
                    "strengths": details["strengths"][:3]
                }
        
        # Compile results
        results = {
            "current_identity": current,
            "authentic_elements": authentic,
            "target_identity": target,
            "differentiators": differentiators,
            "primary_archetype": self.selected_archetype,
            "archetype_matches": archetype_results
        }
        
        return results