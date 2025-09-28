import streamlit as st

class PurposeAgent:
    """
    Purpose Agent - Meaning Architect
    Helps identify meaningful work and purpose-aligned career paths
    """
    
    def __init__(self):
        self.name = "Meaning Architect"
        self.description = "Purpose and meaningful work specialist"
        self.questions = [
            "What activities or work gives you a sense of meaning, purpose, or fulfillment?",
            "When have you felt your work had the most positive impact on others or the world?",
            "What problems or issues in the world do you feel most drawn to address through your work?",
            "How would you describe your ideal legacy or long-term contribution through your career?"
        ]
        self.current_question_index = 0
        self.responses = []
        self.meaningful_activities = []
        self.impact_experiences = []
        self.problem_areas = []
        self.legacy_aspirations = []
        self.purpose_themes = []
        self.analysis_complete = False
    
    def get_introduction(self):
        """Get the introduction message for this agent"""
        return f"""
        ## Purpose Assessment
        
        I'm your **{self.name}**, {self.description}. I'll help you identify what makes work 
        meaningful for you and how to align your career with your deeper sense of purpose.
        
        Finding meaning in your work is one of the strongest predictors of job satisfaction, 
        resilience, and long-term career success. Let's explore how you can connect your professional 
        path with what matters most to you.
        
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
            final_analysis = self._generate_purpose_analysis()
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
        
        # First question: Meaningful activities
        if question_index == 0:
            meaning_keywords = {
                "creative expression": ["create", "design", "build", "make", "craft", "art", "express", "innovative", "imagination"],
                "problem solving": ["solve", "problem", "solution", "challenge", "resolve", "fix", "figure out", "analyze"],
                "helping others": ["help", "support", "assist", "guide", "mentor", "coach", "teach", "serve", "care"],
                "leading/influencing": ["lead", "influence", "direct", "guide", "inspire", "motivate", "change", "impact"],
                "learning/growth": ["learn", "grow", "develop", "discover", "explore", "study", "understand", "knowledge"],
                "organizing/structuring": ["organize", "structure", "plan", "arrange", "order", "systematize", "coordinate"],
                "analyzing/researching": ["analyze", "research", "investigate", "examine", "study", "assess", "evaluate"],
                "connecting people": ["connect", "relationship", "network", "community", "bring together", "facilitate", "collaborate"]
            }
            
            for activity, keywords in meaning_keywords.items():
                for keyword in keywords:
                    if keyword in message_lower and activity not in self.meaningful_activities:
                        self.meaningful_activities.append(activity)
                        break
            
            # Extract phrases with "meaning", "purpose", "fulfillment", etc.
            meaning_phrases = ["meaning", "purpose", "fulfillment", "satisfaction", "enjoy", "passionate", "love", "energized"]
            for phrase in meaning_phrases:
                if phrase in message_lower:
                    # Look for surrounding context
                    index = message_lower.find(phrase)
                    start = max(0, index - 20)
                    end = min(len(message_lower), index + 20)
                    context = message_lower[start:end]
                    
                    # Extract potential activities
                    import re
                    verbs = re.findall(r'\b[a-z]+ing\b', context)
                    for verb in verbs:
                        if verb not in [a.lower() for a in self.meaningful_activities]:
                            self.meaningful_activities.append(verb + "ing")
        
        # Second question: Impact experiences
        elif question_index == 1:
            impact_keywords = {
                "direct helping": ["helped", "supported", "assisted", "guided", "mentored", "coached", "taught", "served", "cared"],
                "knowledge sharing": ["shared", "taught", "educated", "informed", "explained", "presented", "trained"],
                "creation/innovation": ["created", "designed", "built", "developed", "invented", "innovated", "introduced"],
                "problem resolution": ["solved", "resolved", "fixed", "improved", "addressed", "overcame", "handled"],
                "leadership": ["led", "directed", "managed", "guided", "influenced", "inspired", "coordinated"],
                "advocacy": ["advocated", "represented", "spoke", "defended", "championed", "promoted", "supported"],
                "community building": ["connected", "united", "brought together", "built community", "facilitated", "fostered"]
            }
            
            for impact, keywords in impact_keywords.items():
                for keyword in keywords:
                    if keyword in message_lower and impact not in self.impact_experiences:
                        self.impact_experiences.append(impact)
                        break
            
            # Look for specific beneficiaries of impact
            beneficiaries = {
                "individuals": ["person", "individual", "client", "customer", "patient", "student"],
                "teams": ["team", "group", "colleagues", "peers", "coworkers", "department"],
                "organizations": ["organization", "company", "business", "institution", "employer", "firm"],
                "communities": ["community", "neighborhood", "city", "town", "society", "public"],
                "environment": ["environment", "planet", "nature", "ecosystem", "sustainability"],
                "specific populations": ["children", "youth", "elderly", "women", "men", "minority", "underserved", "marginalized"]
            }
            
            for group, keywords in beneficiaries.items():
                for keyword in keywords:
                    if keyword in message_lower and group not in self.impact_experiences:
                        self.impact_experiences.append(f"impact on {group}")
                        break
        
        # Third question: Problem areas
        elif question_index == 2:
            problem_keywords = {
                "education/learning": ["education", "learning", "knowledge", "teaching", "training", "skills", "literacy"],
                "health/wellbeing": ["health", "wellbeing", "wellness", "healthcare", "mental health", "physical health", "disease"],
                "environment/sustainability": ["environment", "sustainability", "climate", "conservation", "pollution", "waste", "green"],
                "social justice/equality": ["justice", "equality", "equity", "rights", "discrimination", "diversity", "inclusion"],
                "economic opportunity": ["economic", "poverty", "wealth", "opportunity", "jobs", "employment", "financial"],
                "technology access": ["technology", "digital", "access", "connectivity", "information", "divide", "innovation"],
                "community development": ["community", "development", "local", "neighborhood", "housing", "infrastructure"],
                "organizational effectiveness": ["organizational", "effectiveness", "efficiency", "productivity", "leadership", "management"],
                "communication/understanding": ["communication", "understanding", "discourse", "dialogue", "connection", "divide", "polarization"],
                "creativity/expression": ["creativity", "expression", "arts", "culture", "design", "innovation"]
            }
            
            for problem, keywords in problem_keywords.items():
                for keyword in keywords:
                    if keyword in message_lower and problem not in self.problem_areas:
                        self.problem_areas.append(problem)
                        break
        
        # Fourth question: Legacy aspirations
        elif question_index == 3:
            legacy_keywords = {
                "innovator/creator": ["innovation", "creation", "pioneer", "inventor", "creator", "designer", "builder", "maker"],
                "mentor/developer": ["mentor", "develop others", "teach", "train", "guide", "coach", "nurture", "grow"],
                "problem solver": ["solve", "solutions", "fix", "address", "improve", "overcome", "resolve", "transform"],
                "connector/community builder": ["connect", "community", "network", "bridge", "relationships", "unite", "bring together"],
                "advocate/voice": ["advocate", "voice", "speak", "represent", "champion", "defend", "support", "promote"],
                "healer/helper": ["heal", "help", "care", "support", "assist", "serve", "aid", "comfort"],
                "leader/influencer": ["lead", "influence", "impact", "change", "shape", "guide", "direct", "transform"],
                "knowledge contributor": ["knowledge", "research", "discover", "findings", "theory", "understanding", "insight"]
            }
            
            for legacy, keywords in legacy_keywords.items():
                for keyword in keywords:
                    if keyword in message_lower and legacy not in self.legacy_aspirations:
                        self.legacy_aspirations.append(legacy)
                        break
            
            # Look for impact scale
            scale_indicators = {
                "individual impact": ["individual", "person", "one by one", "directly", "personally"],
                "organizational impact": ["organization", "company", "business", "institution", "workplace"],
                "community impact": ["community", "local", "neighborhood", "city", "region"],
                "societal impact": ["society", "world", "global", "humanity", "culture", "social"],
                "field/industry impact": ["field", "industry", "profession", "sector", "discipline", "domain"]
            }
            
            for scale, indicators in scale_indicators.items():
                for indicator in indicators:
                    if indicator in message_lower and scale not in self.legacy_aspirations:
                        self.legacy_aspirations.append(scale)
                        break
    
    def _get_next_question(self):
        """Get the next question to ask"""
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            return f"**{self.questions[self.current_question_index]}**"
        else:
            return None
    
    def _identify_purpose_themes(self):
        """
        Identify recurring purpose themes from all responses
        This is a simplified implementation - a real one would use more sophisticated NLP
        """
        # Core purpose archetypes
        purpose_archetypes = {
            "The Creator": {
                "activities": ["creative expression", "building", "designing", "making", "innovating"],
                "impacts": ["creation/innovation", "bringing new ideas to life"],
                "problems": ["creativity/expression", "innovation challenges"],
                "legacies": ["innovator/creator", "field/industry impact"],
                "description": "Finding meaning in bringing new things into existence - whether products, services, systems, or ideas.",
                "work_motivations": ["Originality", "Self-expression", "Innovation", "Building", "Craftsmanship"],
                "fulfillment_sources": ["Creating something from nothing", "Expressing vision through tangible outcomes", "Making ideas real", "Designing elegant solutions", "Building lasting works"],
                "score": 0
            },
            "The Healer": {
                "activities": ["helping others", "supporting", "caring"],
                "impacts": ["direct helping", "impact on individuals"],
                "problems": ["health/wellbeing", "mental health"],
                "legacies": ["healer/helper", "individual impact"],
                "description": "Finding meaning in directly helping others overcome challenges, heal from wounds, or improve wellbeing.",
                "work_motivations": ["Compassion", "Care", "Support", "Alleviating suffering", "Restoration"],
                "fulfillment_sources": ["Seeing others heal or improve", "Providing care in difficult times", "Being present for transformation", "Offering comfort or relief", "Supporting recovery and growth"],
                "score": 0
            },
            "The Teacher": {
                "activities": ["learning/growth", "sharing knowledge", "mentoring"],
                "impacts": ["knowledge sharing", "guided others"],
                "problems": ["education/learning"],
                "legacies": ["mentor/developer", "knowledge contributor"],
                "description": "Finding meaning in sharing knowledge and facilitating growth and development in others.",
                "work_motivations": ["Knowledge sharing", "Development", "Growth", "Learning", "Understanding"],
                "fulfillment_sources": ["Witnessing others' growth", "Sharing valuable knowledge", "Developing potential in others", "Creating learning opportunities", "Building capabilities"],
                "score": 0
            },
            "The Problem Solver": {
                "activities": ["problem solving", "analyzing/researching", "improving systems"],
                "impacts": ["problem resolution", "overcame challenges"],
                "problems": ["any complex challenge"],
                "legacies": ["problem solver"],
                "description": "Finding meaning in addressing challenges, resolving issues, and creating effective solutions.",
                "work_motivations": ["Resolution", "Improvement", "Optimization", "Effectiveness", "Solutions"],
                "fulfillment_sources": ["Solving difficult problems", "Creating elegant solutions", "Improving existing systems", "Overcoming obstacles", "Making things work better"],
                "score": 0
            },
            "The Builder": {
                "activities": ["organizing/structuring", "developing systems", "creating infrastructure"],
                "impacts": ["creation/innovation", "improved processes"],
                "problems": ["organizational effectiveness", "community development"],
                "legacies": ["innovator/creator", "organizational impact"],
                "description": "Finding meaning in creating structures, systems, organizations, or communities that endure.",
                "work_motivations": ["Construction", "Structure", "Organization", "Development", "Durability"],
                "fulfillment_sources": ["Building lasting structures", "Creating effective systems", "Developing strong foundations", "Organizing for effectiveness", "Constructing for the future"],
                "score": 0
            },
            "The Advocate": {
                "activities": ["leading/influencing", "speaking up", "representing others"],
                "impacts": ["advocacy", "representation"],
                "problems": ["social justice/equality", "rights"],
                "legacies": ["advocate/voice", "societal impact"],
                "description": "Finding meaning in championing causes, addressing injustices, and giving voice to important issues.",
                "work_motivations": ["Justice", "Equity", "Rights", "Fairness", "Representation"],
                "fulfillment_sources": ["Standing up for others", "Creating positive change", "Addressing injustice", "Giving voice to important issues", "Protecting rights and dignity"],
                "score": 0
            },
            "The Connector": {
                "activities": ["connecting people", "building relationships", "facilitating"],
                "impacts": ["community building", "bringing people together"],
                "problems": ["communication/understanding", "connection"],
                "legacies": ["connector/community builder", "community impact"],
                "description": "Finding meaning in bringing people together, building relationships, and fostering community.",
                "work_motivations": ["Connection", "Community", "Relationships", "Belonging", "Unity"],
                "fulfillment_sources": ["Building meaningful communities", "Creating connection between people", "Facilitating belonging", "Developing networks", "Fostering relationships"],
                "score": 0
            },
            "The Leader": {
                "activities": ["leading/influencing", "guiding", "directing"],
                "impacts": ["leadership", "guided vision"],
                "problems": ["organizational effectiveness", "direction"],
                "legacies": ["leader/influencer", "organizational impact"],
                "description": "Finding meaning in guiding, influencing, and bringing out the best in groups toward important objectives.",
                "work_motivations": ["Direction", "Vision", "Influence", "Mobilization", "Achievement"],
                "fulfillment_sources": ["Setting meaningful direction", "Inspiring collective action", "Achieving shared goals", "Guiding others effectively", "Creating lasting impact through others"],
                "score": 0
            },
            "The Discoverer": {
                "activities": ["analyzing/researching", "learning/growth", "exploring"],
                "impacts": ["knowledge sharing", "discoveries"],
                "problems": ["knowledge gaps", "exploration"],
                "legacies": ["knowledge contributor", "field/industry impact"],
                "description": "Finding meaning in exploring, understanding, discovering, and expanding knowledge.",
                "work_motivations": ["Discovery", "Understanding", "Knowledge", "Research", "Exploration"],
                "fulfillment_sources": ["Finding new knowledge", "Understanding complex subjects", "Exploring unknown territories", "Researching important questions", "Contributing to understanding"],
                "score": 0
            },
            "The Steward": {
                "activities": ["organizing/structuring", "preserving", "protecting"],
                "impacts": ["protection", "preservation"],
                "problems": ["environment/sustainability", "conservation"],
                "legacies": ["individual impact", "community impact"],
                "description": "Finding meaning in preserving, protecting, and carefully maintaining what is valuable.",
                "work_motivations": ["Preservation", "Protection", "Sustainability", "Conservation", "Care"],
                "fulfillment_sources": ["Protecting what matters", "Preserving important elements", "Maintaining valuable systems", "Ensuring sustainability", "Careful stewardship"],
                "score": 0
            }
        }
        
        # Score each purpose archetype based on all collected information
        for archetype, attributes in purpose_archetypes.items():
            score = 0
            
            # Score based on meaningful activities
            for activity in self.meaningful_activities:
                if any(keyword in activity.lower() for keyword in attributes["activities"]):
                    score += 2
            
            # Score based on impact experiences
            for impact in self.impact_experiences:
                if any(keyword in impact.lower() for keyword in attributes["impacts"]):
                    score += 2
            
            # Score based on problem areas
            for problem in self.problem_areas:
                if any(keyword in problem.lower() for keyword in attributes["problems"]):
                    score += 2
            
            # Score based on legacy aspirations
            for legacy in self.legacy_aspirations:
                if any(keyword in legacy.lower() for keyword in attributes["legacies"]):
                    score += 2
            
            purpose_archetypes[archetype]["score"] = score
        
        # Sort archetypes by score
        sorted_archetypes = sorted(purpose_archetypes.items(), key=lambda x: x[1]["score"], reverse=True)
        
        # Extract top themes (those with scores > 0)
        themes = []
        for archetype, details in sorted_archetypes:
            if details["score"] > 0:
                themes.append({
                    "name": archetype,
                    "score": details["score"],
                    "description": details["description"],
                    "work_motivations": details["work_motivations"],
                    "fulfillment_sources": details["fulfillment_sources"]
                })
        
        self.purpose_themes = themes
        return themes
    
    def _generate_purpose_analysis(self):
        """Generate a purpose analysis based on the responses"""
        
        # First identify purpose themes
        purpose_themes = self._identify_purpose_themes()
        
        # Generate the analysis
        analysis = f"""
        ## Purpose & Meaning Analysis
        
        Based on our conversation, I've analyzed the activities, impacts, problems, and legacy aspirations 
        that are most meaningful to you. This helps identify how you can align your career with your deeper 
        sense of purpose.
        
        ### Sources of Meaning in Your Work
        
        These activities appear to give you the most sense of meaning or fulfillment:
        """
        
        if self.meaningful_activities:
            for activity in self.meaningful_activities[:5]:  # Show top 5
                analysis += f"\n- **{activity.capitalize()}**"
        else:
            analysis += "\nYou haven't specified activities that bring you meaning or fulfillment."
        
        analysis += "\n\n### Impact That Resonates"
        
        if self.impact_experiences:
            analysis += "\n\nYou've felt your work had the most positive impact when it involved:"
            for experience in self.impact_experiences[:5]:  # Show top 5
                analysis += f"\n- **{experience.capitalize()}**"
        else:
            analysis += "\n\nYou haven't specified experiences where your work had positive impact."
        
        analysis += "\n\n### Problems You're Drawn To"
        
        if self.problem_areas:
            analysis += "\n\nYou appear most drawn to addressing these problems or issues:"
            for problem in self.problem_areas[:5]:  # Show top 5
                analysis += f"\n- **{problem.capitalize()}**"
        else:
            analysis += "\n\nYou haven't specified problems you're drawn to address."
        
        analysis += "\n\n### Legacy Aspirations"
        
        if self.legacy_aspirations:
            analysis += "\n\nYour ideal legacy or long-term contribution includes:"
            for legacy in self.legacy_aspirations[:5]:  # Show top 5
                analysis += f"\n- **{legacy.capitalize()}**"
        else:
            analysis += "\n\nYou haven't specified legacy aspirations."
        
        # Purpose archetype analysis
        analysis += "\n\n### Purpose Themes Analysis\n"
        
        if purpose_themes:
            # Show primary theme
            primary_theme = purpose_themes[0]
            
            analysis += f"""
            Your responses suggest that your primary purpose theme is **{primary_theme["name"]}**.
            
            **{primary_theme["name"]}**: {primary_theme["description"]}
            
            **Key Work Motivations:**
            """
            
            for motivation in primary_theme["work_motivations"][:3]:  # Show top 3
                analysis += f"\n- {motivation}"
            
            analysis += "\n\n**Sources of Fulfillment:**"
            
            for source in primary_theme["fulfillment_sources"][:3]:  # Show top 3
                analysis += f"\n- {source}"
            
            # Show secondary theme if available
            if len(purpose_themes) > 1:
                secondary_theme = purpose_themes[1]
                analysis += f"""
                
                Your secondary purpose theme appears to be **{secondary_theme["name"]}**, which complements your primary theme by adding motivation through {secondary_theme["description"].lower()}
                """
        else:
            analysis += """
            Based on your responses, there isn't a clear pattern of purpose themes emerging. This could mean:
            
            1. You're in a period of purpose exploration or transition
            2. Your sense of meaning comes from a highly personalized combination of factors
            3. You might benefit from deeper reflection on what activities and impacts truly energize you
            """
        
        # Purpose statement development
        analysis += """
        
        ### Purpose Statement Development
        
        A personal purpose statement can serve as a compass for career decisions. Based on your responses, here's a framework for developing yours:
        """
        
        if purpose_themes and self.meaningful_activities and self.problem_areas:
            primary_activity = self.meaningful_activities[0] if self.meaningful_activities else "engaging in work"
            primary_problem = self.problem_areas[0] if self.problem_areas else "solving important problems"
            primary_impact = self.impact_experiences[0] if self.impact_experiences else "having positive impact"
            primary_legacy = self.legacy_aspirations[0] if self.legacy_aspirations else "leaving a meaningful legacy"
            
            analysis += f"""
            **Draft Purpose Statement:**
            
            "I find meaning through {primary_activity} that addresses {primary_problem}, creating impact through {primary_impact}, ultimately contributing to {primary_legacy}."
            
            This statement combines:
            - The work activities that energize you
            - The problems that matter to you
            - The kind of impact that feels meaningful
            - The legacy you hope to create
            """
        else:
            analysis += """
            To create your purpose statement, complete this frame:
            
            "I find meaning through [meaningful activities] that address [important problems], creating impact through [type of contribution], ultimately contributing to [desired legacy]."
            
            Your statement should combine:
            - The work activities that energize you
            - The problems that matter to you
            - The kind of impact that feels meaningful
            - The legacy you hope to create
            """
        
        # Career alignment recommendations
        analysis += """
        
        ### Career Alignment Recommendations
        
        To align your career more closely with your sense of purpose:
        
        #### 1. Role Alignment
        """
        
        if purpose_themes and self.meaningful_activities:
            primary_theme = purpose_themes[0]["name"]
            
            if primary_theme == "The Creator":
                analysis += """
                Look for roles that allow you to:
                - Design and develop new solutions or innovations
                - Express creativity through your work products
                - Have autonomy over your creative process
                - See tangible outcomes from your efforts
                - Apply originality to solving problems
                
                **Role characteristics to prioritize:**
                - Creative control and input
                - Opportunity to build or design
                - Recognition for original contributions
                - Space for experimentation and iteration
                - Connection to the end product or creation
                """
            elif primary_theme == "The Healer":
                analysis += """
                Look for roles that allow you to:
                - Directly help or support others
                - See the positive impact of your work on individuals
                - Address suffering or challenges
                - Provide care or assistance
                - Create conditions for wellbeing
                
                **Role characteristics to prioritize:**
                - Direct service or support components
                - Clear line of sight to who benefits
                - Opportunities for compassionate interaction
                - Focus on improvement and wellbeing
                - Space for personal connection
                """
            elif primary_theme == "The Teacher":
                analysis += """
                Look for roles that allow you to:
                - Share knowledge and develop others
                - Create learning opportunities
                - Watch others grow through your guidance
                - Organize and communicate complex information
                - Mentor less experienced colleagues
                
                **Role characteristics to prioritize:**
                - Knowledge sharing components
                - Development or training responsibilities
                - Mentorship opportunities
                - Creating resources that help others learn
                - Seeing the growth and progress of others
                """
            elif primary_theme == "The Problem Solver":
                analysis += """
                Look for roles that allow you to:
                - Address complex or challenging problems
                - Create effective solutions
                - Improve systems or processes
                - Apply analytical thinking
                - Overcome obstacles through strategy
                
                **Role characteristics to prioritize:**
                - Clear problems to be solved
                - Analytical components and decision making
                - Measuring improvements and outcomes
                - Opportunity to optimize and enhance
                - Recognition for effective solutions
                """
            elif primary_theme == "The Builder":
                analysis += """
                Look for roles that allow you to:
                - Create enduring structures or systems
                - Develop foundations for future growth
                - Organize resources effectively
                - Build something larger than yourself
                - Leave lasting infrastructure
                
                **Role characteristics to prioritize:**
                - System or structure development
                - Long-term impact potential
                - Creating frameworks others will use
                - Building components that endure
                - Seeing your constructions support others
                """
            elif primary_theme == "The Advocate":
                analysis += """
                Look for roles that allow you to:
                - Champion important causes or issues
                - Represent underserved voices or needs
                - Address injustices or inequities
                - Create positive social change
                - Stand for important principles
                
                **Role characteristics to prioritize:**
                - Connection to social impact
                - Advocacy components
                - Voice for important issues
                - Addressing systemic challenges
                - Creating more equitable conditions
                """
            elif primary_theme == "The Connector":
                analysis += """
                Look for roles that allow you to:
                - Bring people together around shared purposes
                - Build communities or networks
                - Facilitate meaningful relationships
                - Create belonging for others
                - Bridge between different groups
                
                **Role characteristics to prioritize:**
                - Community building aspects
                - Relationship development
                - Creating connections between people
                - Facilitating groups or teams
                - Fostering collaboration and belonging
                """
            elif primary_theme == "The Leader":
                analysis += """
                Look for roles that allow you to:
                - Guide others toward important objectives
                - Influence direction and strategy
                - Inspire collective action
                - Create environments where others thrive
                - Set meaningful vision
                
                **Role characteristics to prioritize:**
                - Leadership opportunities
                - Strategic influence
                - Team development responsibilities
                - Vision-setting components
                - Mobilizing collective efforts
                """
            elif primary_theme == "The Discoverer":
                analysis += """
                Look for roles that allow you to:
                - Explore new territories or knowledge
                - Research important questions
                - Understand complex phenomena
                - Uncover new insights
                - Expand understanding in your field
                
                **Role characteristics to prioritize:**
                - Research components
                - Exploration of new areas
                - Learning and discovery
                - Finding and sharing insights
                - Advancing knowledge frontiers
                """
            elif primary_theme == "The Steward":
                analysis += """
                Look for roles that allow you to:
                - Preserve what's valuable
                - Protect important resources
                - Maintain sustainable systems
                - Ensure careful management
                - Safeguard for future generations
                
                **Role characteristics to prioritize:**
                - Preservation components
                - Sustainability focus
                - Resource management
                - Long-term thinking
                - Protection of what matters
                """
        else:
            analysis += """
            When evaluating potential roles, prioritize those that:
            - Include activities you find inherently meaningful
            - Address problems you care about solving
            - Create the kind of impact that energizes you
            - Connect to your longer-term legacy aspirations
            
            Look beyond job titles to the actual day-to-day activities and impacts of the role.
            """
        
        # Organizational alignment recommendations
        analysis += "\n\n#### 2. Organizational Alignment\n"
        
        if self.problem_areas:
            priority_problems = self.problem_areas[:2]  # Top 2 problems
            
            analysis += f"""
            Seek organizations whose mission addresses {priority_problems[0]}{" or " + priority_problems[1] if len(priority_problems) > 1 else ""}.
            
            Evaluate potential employers by:
            - How directly their mission connects to problems you care about
            - Whether their values align with your own
            - If their impact approach resonates with your preferences
            - Whether you can see a clear line between your work and meaningful outcomes
            
            Remember that purpose can be found in many sectors - nonprofit, for-profit, government, 
            or academic. The key is alignment between the organization's mission and your sources of meaning.
            """
        else:
            analysis += """
            When evaluating potential organizations:
            - Research their mission and impact to ensure alignment with what matters to you
            - Look for values statements that resonate with your own priorities
            - Speak with current employees about meaning in their work
            - Consider how the organization measures success beyond financial metrics
            - Evaluate how directly you can see your work connecting to meaningful outcomes
            """
        
        # Daily practices recommendations
        analysis += """
        
        #### 3. Daily Practices
        
        Even in your current role, you can increase meaning through:
        
        1. **Purpose Reframing**
           - Connect daily tasks to their broader impact
           - Identify who ultimately benefits from your work
           - Recognize how routine work supports larger meaningful goals
        
        2. **Meaningful Expansion**
           - Volunteer for projects aligned with your purpose themes
           - Suggest initiatives that address problems you care about
           - Look for ways to incorporate more purposeful activities
        
        3. **Impact Tracking**
           - Keep a "purpose journal" noting moments of meaning
           - Document positive impacts, however small
           - Collect feedback that demonstrates your contribution
        
        4. **Connection Building**
           - Build relationships with those who benefit from your work
           - Connect with colleagues who share your sense of purpose
           - Learn from those who find deep meaning in similar work
        """
        
        # Meaning integration strategies
        analysis += """
        
        ### Purpose Integration Framework
        
        Meaning in work comes from three key alignments:
        
        1. **Activity Alignment:** When your day-to-day tasks include activities that you find inherently meaningful
        
        2. **Impact Alignment:** When your work addresses problems you care about and creates impact that matters to you
        
        3. **Story Alignment:** When you can connect your work to your broader life narrative and legacy aspirations
        
        The strongest sense of purpose emerges when all three alignments are present. When this isn't possible, consider:
        
        - **Role Crafting:** Reshaping aspects of your current role to increase meaningful activities
        - **Impact Connecting:** Finding clearer lines between your work and its ultimate impact
        - **Narrative Integration:** Developing a stronger story about how your work connects to your larger life purpose
        - **Portfolio Approach:** Meeting different purpose needs through a combination of work, volunteer, and personal projects
        
        Remember that finding purpose is rarely a one-time discovery but rather an ongoing process of alignment and integration. By regularly reflecting on what gives your work meaning, you can continuously evolve your career to express your unique purpose more fully.
        """
        
        return analysis
    
    def _get_results(self):
        """Get the results of the analysis for other agents to use"""
        
        # Format meaningful activities
        activities = [activity.capitalize() for activity in self.meaningful_activities]
        
        # Format impact experiences
        impacts = [impact.capitalize() for impact in self.impact_experiences]
        
        # Format problem areas
        problems = [problem.capitalize() for problem in self.problem_areas]
        
        # Format legacy aspirations
        legacy = [aspiration.capitalize() for aspiration in self.legacy_aspirations]
        
        # Format purpose themes
        themes = []
        for theme in self.purpose_themes:
            themes.append({
                "name": theme["name"],
                "score": theme["score"],
                "description": theme["description"]
            })
        
        # Get primary purpose theme
        primary_theme = None
        if self.purpose_themes:
            primary_theme = self.purpose_themes[0]["name"]
        
        # Compile results
        results = {
            "meaningful_activities": activities,
            "impact_experiences": impacts,
            "problem_areas": problems,
            "legacy_aspirations": legacy,
            "purpose_themes": themes,
            "primary_purpose_theme": primary_theme
        }
        
        return results