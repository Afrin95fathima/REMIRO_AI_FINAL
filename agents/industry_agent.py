import streamlit as st

class IndustryAgent:
    """
    Industry Agent - Market Intelligence Specialist
    Provides industry insights and strategic positioning advice
    """
    
    def __init__(self):
        self.name = "Market Intelligence Specialist"
        self.description = "Industry trends and strategic positioning advisor"
        self.questions = [
            "Which industries or sectors do you find most interesting or aligned with your values and goals?",
            "What excites or concerns you about the future of work in your fields of interest?",
            "Do you prefer established, stable industries or emerging, rapidly evolving ones?",
            "What factors do you consider most important when evaluating potential industries? (e.g., growth prospects, social impact, work-life balance, etc.)"
        ]
        self.current_question_index = 0
        self.responses = []
        self.industries_of_interest = []
        self.industry_concerns = []
        self.industry_preferences = {
            "stability_vs_growth": None,  # "stability" or "growth"
            "innovation_pace": None,      # "established" or "emerging"
            "size_preference": None,      # "large" or "small"
        }
        self.priority_factors = []
        self.analysis_complete = False
    
    def get_introduction(self):
        """Get the introduction message for this agent"""
        return f"""
        ## Industry Analysis
        
        I'm your **{self.name}**, {self.description}. I'll help you understand industry trends, 
        evaluate market dynamics, and position your career strategically within promising sectors.
        
        Understanding industry landscapes can help you identify growing fields, anticipate changes, 
        and make informed decisions about where to focus your career development.
        
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
            final_analysis = self._generate_industry_analysis()
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
        
        # First question: Industries of interest
        if question_index == 0:
            # Industry keywords
            industry_keywords = {
                "technology": ["tech", "software", "it", "information technology", "digital", "computing", "web", "internet", "computer"],
                "healthcare": ["health", "medical", "healthcare", "medicine", "pharma", "pharmaceutical", "biotech", "wellness"],
                "finance": ["finance", "banking", "investment", "financial", "fintech", "insurance", "wealth"],
                "education": ["education", "teaching", "training", "learning", "edtech", "academic", "school", "university"],
                "manufacturing": ["manufacturing", "production", "industrial", "factory", "assembly", "engineering"],
                "retail": ["retail", "e-commerce", "commerce", "shopping", "consumer", "store", "merchandise"],
                "media & entertainment": ["media", "entertainment", "film", "music", "gaming", "content", "streaming", "creative"],
                "energy": ["energy", "utility", "power", "electricity", "renewable", "solar", "wind", "sustainability"],
                "real estate": ["real estate", "property", "construction", "housing", "building", "development"],
                "transportation": ["transportation", "logistics", "shipping", "supply chain", "delivery", "travel"],
                "hospitality": ["hospitality", "hotel", "restaurant", "tourism", "travel", "leisure"],
                "consulting": ["consulting", "professional services", "advisory", "business services"],
                "nonprofit": ["nonprofit", "ngo", "social sector", "charity", "foundation", "social impact"],
                "government": ["government", "public sector", "civic", "policy", "administration", "defense"],
                "agriculture": ["agriculture", "farming", "food production", "agtech", "forestry"],
                "legal": ["legal", "law", "attorney", "compliance", "regulatory"],
                "marketing": ["marketing", "advertising", "pr", "public relations", "brand", "communications"]
            }
            
            for industry, keywords in industry_keywords.items():
                for keyword in keywords:
                    if keyword in message_lower and industry not in self.industries_of_interest:
                        self.industries_of_interest.append(industry)
                        break
        
        # Second question: Future concerns and excitement
        elif question_index == 1:
            # Common workplace concern keywords
            concern_keywords = {
                "automation": ["automation", "ai replacing", "robots", "machine", "job loss", "displacement"],
                "remote work challenges": ["remote", "wfh", "work from home", "virtual", "telecommuting"],
                "skill obsolescence": ["obsolete", "outdated", "keeping up", "rapid change", "continuous learning"],
                "work-life balance": ["work-life", "balance", "burnout", "overwork", "hours", "flexibility"],
                "job security": ["security", "stability", "layoffs", "downsizing", "restructuring", "uncertainty"],
                "income inequality": ["inequality", "pay gap", "fair compensation", "wealth gap"],
                "corporate ethics": ["ethics", "values", "social responsibility", "purpose", "mission"],
                "technological disruption": ["disruption", "disruptive", "upheaval", "transformation"],
                "sustainability": ["sustainability", "climate", "environmental", "green", "carbon"],
                "globalization": ["globalization", "outsourcing", "global competition", "international"]
            }
            
            for concern, keywords in concern_keywords.items():
                for keyword in keywords:
                    if keyword in message_lower and concern not in self.industry_concerns:
                        self.industry_concerns.append(concern)
                        break
        
        # Third question: Industry preferences (stable vs. emerging)
        elif question_index == 2:
            # Analyze preference for established vs. emerging industries
            established_keywords = ["established", "stable", "traditional", "proven", "mature", "reliable", "consistent", "predictable"]
            emerging_keywords = ["emerging", "new", "cutting-edge", "evolving", "growing", "innovative", "disruptive", "startup", "novel"]
            
            established_count = sum(1 for keyword in established_keywords if keyword in message_lower)
            emerging_count = sum(1 for keyword in emerging_keywords if keyword in message_lower)
            
            if established_count > emerging_count:
                self.industry_preferences["innovation_pace"] = "established"
            elif emerging_count > established_count:
                self.industry_preferences["innovation_pace"] = "emerging"
            else:
                # If equal or no clear preference
                self.industry_preferences["innovation_pace"] = "balanced"
            
            # Analyze preference for stability vs. growth
            stability_keywords = ["stability", "secure", "consistent", "reliable", "predictable", "steady"]
            growth_keywords = ["growth", "advancement", "opportunity", "potential", "upward", "expansion", "progressive"]
            
            stability_count = sum(1 for keyword in stability_keywords if keyword in message_lower)
            growth_count = sum(1 for keyword in growth_keywords if keyword in message_lower)
            
            if stability_count > growth_count:
                self.industry_preferences["stability_vs_growth"] = "stability"
            elif growth_count > stability_count:
                self.industry_preferences["stability_vs_growth"] = "growth"
            else:
                self.industry_preferences["stability_vs_growth"] = "balanced"
            
            # Analyze preference for company size
            large_keywords = ["large", "big", "enterprise", "corporation", "corporate", "established company"]
            small_keywords = ["small", "startup", "boutique", "independent", "entrepreneurial", "small business"]
            
            large_count = sum(1 for keyword in large_keywords if keyword in message_lower)
            small_count = sum(1 for keyword in small_keywords if keyword in message_lower)
            
            if large_count > small_count:
                self.industry_preferences["size_preference"] = "large"
            elif small_count > large_count:
                self.industry_preferences["size_preference"] = "small"
            else:
                self.industry_preferences["size_preference"] = "flexible"
        
        # Fourth question: Priority factors
        elif question_index == 3:
            # Priority factor keywords
            factor_keywords = {
                "growth potential": ["growth", "potential", "opportunity", "expand", "future", "prospect"],
                "compensation": ["salary", "pay", "compensation", "money", "income", "financial", "earning"],
                "work-life balance": ["balance", "flexibility", "hours", "schedule", "time off", "personal time"],
                "social impact": ["impact", "social", "purpose", "meaningful", "change", "difference", "society", "community"],
                "job security": ["security", "stability", "consistent", "reliable", "dependable"],
                "innovation": ["innovation", "cutting-edge", "technology", "advanced", "creative", "novel"],
                "professional development": ["development", "learning", "skill", "advancement", "grow", "progress", "career path"],
                "company culture": ["culture", "values", "environment", "people", "colleagues", "team"],
                "leadership": ["leadership", "management", "direction", "vision", "strategy"],
                "market position": ["market leader", "competitive", "dominant", "position", "industry standing"]
            }
            
            for factor, keywords in factor_keywords.items():
                for keyword in keywords:
                    if keyword in message_lower and factor not in self.priority_factors:
                        self.priority_factors.append(factor)
                        break
    
    def _get_next_question(self):
        """Get the next question to ask"""
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            return f"**{self.questions[self.current_question_index]}**"
        else:
            return None
    
    def _generate_industry_analysis(self):
        """Generate an industry analysis based on the responses"""
        
        # Ensure we have some industries of interest
        if not self.industries_of_interest:
            self.industries_of_interest = ["technology", "healthcare", "education"]
        
        # Ensure we have some priority factors
        if not self.priority_factors:
            self.priority_factors = ["growth potential", "work-life balance", "compensation"]
        
        # Generate the analysis
        analysis = f"""
        ## Industry & Market Analysis
        
        Based on our conversation, I've analyzed your industry preferences, concerns, and priorities 
        to provide strategic insights for positioning your career in promising sectors.
        
        ### Industries of Interest
        
        You've expressed interest in the following industries:
        """
        
        for industry in self.industries_of_interest:
            analysis += f"\n- **{industry.capitalize()}**"
        
        # Industry preferences analysis
        analysis += "\n\n### Industry Preferences\n"
        
        # Innovation pace preference
        if self.industry_preferences["innovation_pace"] == "established":
            analysis += "\nYou seem to prefer **established, mature industries** with proven business models and more predictable trajectories."
        elif self.industry_preferences["innovation_pace"] == "emerging":
            analysis += "\nYou appear drawn to **emerging, rapidly evolving industries** that offer innovation and novel opportunities."
        else:
            analysis += "\nYou show **balanced interest in both established and emerging sectors**, valuing aspects of each."
        
        # Stability vs. growth preference
        if self.industry_preferences["stability_vs_growth"] == "stability":
            analysis += "\nYou tend to prioritize **stability and predictability** in your industry choices."
        elif self.industry_preferences["stability_vs_growth"] == "growth":
            analysis += "\nYou seem oriented toward **growth and advancement potential** in your industry preferences."
        else:
            analysis += "\nYou value a **balance of stability and growth opportunities** in potential industries."
        
        # Company size preference
        if self.industry_preferences["size_preference"] == "large":
            analysis += "\nYour responses suggest preference for **larger organizations** with established structures and resources."
        elif self.industry_preferences["size_preference"] == "small":
            analysis += "\nYou appear to favor **smaller companies or startups** with more agility and entrepreneurial environments."
        else:
            analysis += "\nYou show **flexibility regarding organization size**, potentially seeing benefits in both large and small environments."
        
        # Industry concerns
        analysis += "\n\n### Future of Work Considerations\n"
        
        if self.industry_concerns:
            analysis += "\nYou've expressed awareness or concern about these industry dynamics:"
            for concern in self.industry_concerns:
                analysis += f"\n- **{concern.capitalize()}**"
        else:
            analysis += "\nYou haven't expressed specific concerns about future industry trends."
        
        # Priority factors
        analysis += "\n\n### Priority Factors in Industry Selection\n"
        
        analysis += "\nWhen evaluating industries, these factors appear most important to you:"
        for factor in self.priority_factors[:5]:  # Limit to top 5
            analysis += f"\n- **{factor.capitalize()}**"
        
        # Industry insights for top industries of interest
        analysis += "\n\n### Strategic Industry Insights\n"
        
        # Provide insights for top 2-3 industries
        for industry in self.industries_of_interest[:3]:
            analysis += f"\n#### {industry.capitalize()} Industry\n"
            
            if industry == "technology":
                analysis += """
                **Current Landscape:** 
                The technology sector remains a dominant force in the global economy, with continuing growth in cloud services, 
                artificial intelligence, cybersecurity, and enterprise software. Major players continue to expand while specialized 
                startups create innovation in focused niches.
                
                **Future Trajectory:** 
                Technology growth is expected to continue with particular acceleration in AI/ML applications, edge computing, 
                quantum computing, and extended reality. The integration of technology into traditionally non-tech sectors 
                (healthcare, finance, etc.) creates expanded opportunity spaces.
                
                **Strategic Positioning:**
                - Focus on developing versatile technical skills with depth in 1-2 specialized areas
                - Consider both technical and product/business hybrid roles for maximum value
                - Look for organizations solving meaningful problems rather than chasing trends
                - Build a portfolio of work that demonstrates both technical ability and business impact
                """
            elif industry == "healthcare":
                analysis += """
                **Current Landscape:** 
                Healthcare continues to undergo digital transformation, with telehealth, remote monitoring, 
                personalized medicine, and data analytics driving significant change. The sector faces 
                challenges in cost management, accessibility, and regulatory compliance.
                
                **Future Trajectory:** 
                Growth areas include digital health platforms, AI-powered diagnostics, precision medicine, 
                preventative care models, and health data infrastructure. Aging populations in many countries 
                are creating sustained demand for innovative healthcare solutions.
                
                **Strategic Positioning:**
                - Develop expertise that bridges clinical knowledge with technology capabilities
                - Consider roles in digital health transformation, data analysis, or patient experience
                - Look for organizations addressing healthcare accessibility and equity challenges
                - Understand regulatory frameworks and compliance requirements as a competitive advantage
                """
            elif industry == "finance":
                analysis += """
                **Current Landscape:** 
                Financial services is experiencing significant disruption through fintech innovation, 
                changing consumer expectations, and regulatory evolution. Traditional institutions are 
                investing heavily in digital transformation while specialized fintechs target specific verticals.
                
                **Future Trajectory:** 
                Growth areas include digital payments, wealth management technology, decentralized finance, 
                regtech (regulatory technology), and financial inclusion solutions. The sector is seeing increased 
                emphasis on data security, personalization, and embedded financial services.
                
                **Strategic Positioning:**
                - Develop hybrid skills combining financial knowledge with digital capabilities
                - Consider roles in product development, data analysis, or regulatory compliance
                - Look for organizations with clear digital transformation strategies
                - Build understanding of emerging models like embedded finance and decentralized systems
                """
            elif industry == "education":
                analysis += """
                **Current Landscape:** 
                Education is undergoing significant transformation through online learning platforms, 
                adaptive learning technologies, and skills-based alternatives to traditional credentials. 
                The sector faces challenges in accessibility, effectiveness measurement, and adapting to 
                changing workforce needs.
                
                **Future Trajectory:** 
                Growth areas include personalized learning technology, corporate training and upskilling platforms, 
                alternative credential systems, and global education access. The integration of AI for personalized 
                learning pathways shows particular promise.
                
                **Strategic Positioning:**
                - Focus on roles that bridge educational expertise with technology enablement
                - Consider opportunities in content creation, learning experience design, or outcomes analytics
                - Look for organizations addressing educational access and effectiveness challenges
                - Develop understanding of learning science and evidence-based approaches
                """
            elif industry == "media & entertainment":
                analysis += """
                **Current Landscape:** 
                Media and entertainment continues its digital transformation with streaming platforms, 
                creator economy growth, and immersive experiences driving innovation. Content creation, 
                distribution, and monetization models are evolving rapidly.
                
                **Future Trajectory:** 
                Growth areas include interactive and immersive content, personalized media experiences, 
                creator tools and platforms, and new monetization models. The integration of AI in content 
                creation and recommendation systems is accelerating.
                
                **Strategic Positioning:**
                - Develop hybrid skills across creative, technical, and business domains
                - Consider roles in content strategy, audience development, or platform management
                - Look for organizations with sustainable business models beyond pure content creation
                - Build understanding of emerging technologies like extended reality and AI-assisted creation
                """
            else:
                analysis += f"""
                **Industry Overview:** 
                The {industry} industry presents interesting opportunities aligned with your preferences. 
                Consider researching current trends, growth projections, and skill requirements to determine 
                specific positioning strategies within this sector.
                
                **Strategic Considerations:**
                - Identify specialized niches within {industry} that match your specific interests and strengths
                - Research leading organizations and emerging players to understand different approaches
                - Connect with professionals in the field to gain insider perspectives on trends and opportunities
                - Consider how your unique background and skills might create distinctive value in this sector
                """
        
        # Industry selection framework
        analysis += """
        
        ### Industry Selection Framework
        
        When evaluating specific opportunities within these industries, consider this decision framework:
        
        1. **Market Trajectory Analysis**: Assess both short-term momentum and long-term structural growth drivers
        
        2. **Skills Alignment Evaluation**: Match your current and developable skills to industry requirements
        
        3. **Values Congruence Check**: Ensure the industry's core activities and impact align with your values
        
        4. **Risk Diversification Strategy**: Consider how specialized vs. transferable your industry-specific experience will be
        
        5. **Network Accessibility Assessment**: Evaluate your ability to build meaningful professional connections in the industry
        
        Remember that industries are increasingly interconnected, with boundaries becoming more fluid. Developing skills that transfer across related sectors can create resilience in your career path while maintaining focus.
        """
        
        return analysis
    
    def _get_results(self):
        """Get the results of the analysis for other agents to use"""
        
        # Format industries of interest
        industries = [industry.capitalize() for industry in self.industries_of_interest]
        
        # Format industry concerns
        concerns = [concern.capitalize() for concern in self.industry_concerns]
        
        # Format priority factors
        factors = [factor.capitalize() for factor in self.priority_factors]
        
        # Compile results
        results = {
            "industries_of_interest": industries,
            "industry_concerns": concerns,
            "industry_preferences": {
                "innovation_pace": self.industry_preferences["innovation_pace"].capitalize() if self.industry_preferences["innovation_pace"] else "Balanced",
                "stability_vs_growth": self.industry_preferences["stability_vs_growth"].capitalize() if self.industry_preferences["stability_vs_growth"] else "Balanced",
                "size_preference": self.industry_preferences["size_preference"].capitalize() if self.industry_preferences["size_preference"] else "Flexible"
            },
            "priority_factors": factors
        }
        
        return results