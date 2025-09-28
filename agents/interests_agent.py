import streamlit as st

class InterestsAgent:
    """
    Interests Agent - Career Interests Navigator
    Connects a person's intrinsic curiosities to viable career paths
    """
    
    def __init__(self):
        self.name = "Career Interests Navigator"
        self.description = "Expert in connecting your interests to viable and fulfilling career paths"
        self.questions = [
            "If you had a free Saturday with no obligations, what topics would you find yourself researching, reading about, or watching videos on, just for the fun of it?",
            "What kind of problems in the world do you find yourself complaining about or wishing someone would solve? What about those problems captures your attention?",
            "Think about the classes, projects, or tasks (in school or work) that you genuinely enjoyed. What were you doing, thinking, or creating in those moments?"
        ]
        self.follow_up_questions = {
            "realistic": [
                "How much do you enjoy working with your hands or physical tools to build or fix things?",
                "Do you prefer concrete, practical tasks with tangible results over abstract or theoretical work?",
                "How interested are you in activities like engineering, construction, athletics, or working outdoors?"
            ],
            "investigative": [
                "How much do you enjoy solving complex problems through analysis and research?",
                "How interested are you in understanding how and why things work the way they do?",
                "Do you find yourself drawn to scientific, technical, or mathematical topics in your free time?"
            ],
            "artistic": [
                "How important is creative expression in your life and work?",
                "How much do you value aesthetics, design, and the arts in your environment?",
                "How often do you engage in activities like writing, visual arts, music, or performance?"
            ],
            "social": [
                "How fulfilling do you find activities focused on helping, teaching, or connecting with others?",
                "How interested are you in understanding human behavior and social dynamics?",
                "Do you prefer working on projects that directly impact people's lives and wellbeing?"
            ],
            "enterprising": [
                "How much do you enjoy persuading others or taking the lead in group settings?",
                "How interested are you in business, leadership, or entrepreneurial activities?",
                "Do you find yourself naturally organizing people or resources to achieve goals?"
            ],
            "conventional": [
                "How satisfied do you feel when organizing information or creating structured systems?",
                "How comfortable are you working within established rules and procedures?",
                "Do you enjoy activities that require attention to detail and systematic approaches?"
            ]
        }
        self.current_question_index = 0
        self.responses = []
        self.riasec_scores = {
            "realistic": 0,
            "investigative": 0,
            "artistic": 0,
            "social": 0,
            "enterprising": 0,
            "conventional": 0
        }
        self.follow_up_focus = None
        self.analysis_complete = False
    
    def get_introduction(self):
        """Get the introduction message for this agent"""
        return f"""
        ## Interest & Career Alignment Analysis
        
        I'm your **{self.name}**, {self.description}. I'll help identify your natural interests and 
        curiosities, and connect them to potential career paths where you'll find genuine engagement.
        
        I'll be using frameworks like the Holland Codes (RIASEC) to understand what types of work 
        naturally draw your attention and energy.
        
        Let's start with this question: **{self.questions[0]}**
        """
    
    def process_message(self, message):
        """Process user message and return appropriate response"""
        
        # Store the user's response
        self.responses.append(message)
        
        # Analyze the response for interest indicators
        self._analyze_response(message)
        
        # If we've gone through all initial questions and any follow-ups
        if self.analysis_complete:
            # Generate and return the final analysis
            final_analysis = self._generate_interests_analysis()
            return final_analysis, True, self._get_results()
        
        # Determine if we should move to follow-up questions based on the responses so far
        if len(self.responses) >= 3 and not self.follow_up_focus:
            # Determine which interest area to focus follow-up questions on
            self.follow_up_focus = self._determine_follow_up_focus()
        
        # Get the next question
        next_question = self._get_next_question()
        
        # Check if this was the last question
        if next_question is None:
            self.analysis_complete = True
            final_analysis = self._generate_interests_analysis()
            return final_analysis, True, self._get_results()
        
        return next_question, False, None
    
    def _analyze_response(self, message):
        """
        Analyze the user's response for interest indicators
        This is a simple keyword-based analysis, a real implementation would use NLP
        """
        message_lower = message.lower()
        
        # Realistic indicators
        if any(word in message_lower for word in ["build", "fix", "physical", "hands-on", "outdoors", "mechanical", "tools", "nature", "sports"]):
            self.riasec_scores["realistic"] += 1
            
        # Investigative indicators
        if any(word in message_lower for word in ["research", "analyze", "science", "understand", "solve", "curious", "technology", "data", "theory", "experiment"]):
            self.riasec_scores["investigative"] += 1
            
        # Artistic indicators
        if any(word in message_lower for word in ["create", "design", "art", "music", "write", "perform", "express", "creative", "novel", "innovative", "aesthetic", "beauty"]):
            self.riasec_scores["artistic"] += 1
            
        # Social indicators
        if any(word in message_lower for word in ["help", "teach", "counsel", "people", "social", "community", "care", "serve", "communicate", "connect", "empower"]):
            self.riasec_scores["social"] += 1
            
        # Enterprising indicators
        if any(word in message_lower for word in ["lead", "manage", "persuade", "sell", "business", "influence", "entrepreneurship", "strategy", "compete", "achieve", "negotiate"]):
            self.riasec_scores["enterprising"] += 1
            
        # Conventional indicators
        if any(word in message_lower for word in ["organize", "detail", "data", "structure", "systematic", "process", "procedure", "order", "follow", "precise", "efficient"]):
            self.riasec_scores["conventional"] += 1
    
    def _determine_follow_up_focus(self):
        """
        Determine which interest area to focus follow-up questions on
        based on the highest scores
        """
        # Find the interest area with the highest score
        max_score = max(self.riasec_scores.values())
        candidates = [area for area, score in self.riasec_scores.items() if score == max_score]
        
        # If there's a tie, pick the first one in the list
        return candidates[0] if candidates else "investigative"  # Default to investigative if no clear winner
    
    def _get_next_question(self):
        """Get the next question to ask"""
        
        # If we're doing follow-up questions on a specific interest area
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
    
    def _generate_interests_analysis(self):
        """Generate an interests analysis based on the responses"""
        
        # Get top three interest areas
        sorted_interests = sorted(self.riasec_scores.items(), key=lambda x: x[1], reverse=True)
        top_three = sorted_interests[:3]
        
        # Generate the analysis
        analysis = f"""
        ## Interest & Career Alignment Analysis
        
        Based on our conversation, I've analyzed your interests using the Holland Codes (RIASEC) framework, 
        which helps connect natural curiosities to career paths where you'll find genuine engagement.
        
        ### Your Top Interest Areas
        
        """
        
        # Add descriptions for top three interest areas
        for interest_area, score in top_three:
            analysis += f"- **{interest_area.capitalize()}**: "
            
            if interest_area == "realistic":
                analysis += """
                You show interest in practical, hands-on activities that involve working with tools, machines, or the natural environment. 
                You likely prefer concrete tasks with tangible results over abstract or theoretical work.
                
                **Career Connection:** These interests align with fields like engineering, construction, agriculture, athletics, 
                and technical trades that involve building, fixing, or working with physical objects.
                """
            
            elif interest_area == "investigative":
                analysis += """
                You show curiosity about understanding how things work and solving complex problems through analysis and research. 
                You're likely drawn to intellectual challenges and systematic exploration of ideas.
                
                **Career Connection:** These interests align with fields like scientific research, technology development, 
                data analysis, medicine, and other areas that involve investigation and problem-solving.
                """
            
            elif interest_area == "artistic":
                analysis += """
                You value creative expression and opportunities to think outside conventional boundaries. 
                You likely appreciate aesthetics and have interest in design, language, or artistic creation.
                
                **Career Connection:** These interests align with fields like graphic design, writing, music, 
                performance arts, architecture, and other creative professions that value originality and self-expression.
                """
            
            elif interest_area == "social":
                analysis += """
                You show interest in working with and helping others. You likely enjoy activities focused on 
                teaching, supporting, or connecting with people in meaningful ways.
                
                **Career Connection:** These interests align with fields like education, healthcare, counseling, 
                social services, human resources, and other professions centered on supporting human development and wellbeing.
                """
            
            elif interest_area == "enterprising":
                analysis += """
                You show interest in leadership, persuasion, and achieving goals. You likely enjoy taking initiative, 
                influencing others, and pursuing concrete objectives or outcomes.
                
                **Career Connection:** These interests align with fields like business management, sales, marketing, 
                entrepreneurship, law, politics, and other areas involving leadership, strategy, and persuasion.
                """
            
            elif interest_area == "conventional":
                analysis += """
                You show interest in organization, structure, and working with data in systematic ways. 
                You likely value clear procedures, attention to detail, and creating order from information.
                
                **Career Connection:** These interests align with fields like accounting, logistics, data management, 
                quality assurance, administration, and other roles that involve organizing, processing, and maintaining information systems.
                """
        
        # Generate career path recommendations based on top interests
        conventional_paths = self._get_conventional_paths(top_three)
        creative_paths = self._get_creative_paths(top_three)
        
        analysis += f"""
        ### Recommended Career Paths
        
        Based on your interest profile, here are some career paths worth exploring:
        
        #### Established Paths
        {conventional_paths}
        
        #### Creative/Emerging Paths
        {creative_paths}
        
        ### Interest Integration Strategy
        
        The most fulfilling careers often incorporate multiple interest areas. For you, look for roles that combine elements of {top_three[0][0].capitalize()}, {top_three[1][0].capitalize()}, and {top_three[2][0].capitalize()} when possible.
        
        For example, a role that requires {self._get_integration_example(top_three)} would leverage your natural curiosities and potentially lead to higher engagement and satisfaction.
        
        Remember that interests evolve throughout your career. The key is finding environments where your natural curiosities are valued and can be expressed through your work.
        """
        
        return analysis
    
    def _get_conventional_paths(self, top_interests):
        """Get conventional career paths based on top interests"""
        
        interest_to_careers = {
            "realistic": [
                "Civil/Mechanical/Electrical Engineering",
                "Construction Management",
                "Physical Therapy",
                "Environmental Science",
                "Veterinary Medicine",
                "Agricultural Science"
            ],
            "investigative": [
                "Scientific Research",
                "Medicine/Healthcare",
                "Computer Science/Programming",
                "Market Research Analyst",
                "Financial Analyst",
                "Academic Research"
            ],
            "artistic": [
                "Graphic Design",
                "Content Creation",
                "Architecture",
                "Interior Design",
                "Marketing Creative",
                "User Experience (UX) Design"
            ],
            "social": [
                "Teaching/Education",
                "Social Work",
                "Human Resources",
                "Counseling/Therapy",
                "Healthcare Administration",
                "Non-profit Management"
            ],
            "enterprising": [
                "Business Management",
                "Sales/Marketing",
                "Law",
                "Real Estate",
                "Public Relations",
                "Project Management"
            ],
            "conventional": [
                "Accounting/Finance",
                "Data Analysis",
                "Quality Assurance",
                "Logistics Coordination",
                "Administrative Management",
                "Information Management"
            ]
        }
        
        # Get careers for top two interest areas
        first_type, _ = top_interests[0]
        second_type, _ = top_interests[1]
        
        first_careers = interest_to_careers[first_type][:3]  # Get top 3 from first interest
        second_careers = interest_to_careers[second_type][:2]  # Get top 2 from second interest
        
        # Combine into formatted string
        careers_text = ""
        for career in first_careers + second_careers:
            careers_text += f"- {career}\n"
            
        return careers_text
    
    def _get_creative_paths(self, top_interests):
        """Get creative/emerging career paths based on top interests"""
        
        # Combinations of interest areas to creative careers
        combinations = {
            ("realistic", "investigative"): [
                "Robotics Engineering",
                "Sustainable Building Design",
                "Medical Device Innovation"
            ],
            ("realistic", "artistic"): [
                "Furniture Design",
                "Scenic Construction",
                "Artisanal Craftsmanship"
            ],
            ("realistic", "social"): [
                "Occupational Therapy",
                "Outdoor Education",
                "Sustainable Community Development"
            ],
            ("realistic", "enterprising"): [
                "Construction Entrepreneurship",
                "Technical Sales Engineering",
                "Sustainable Resource Management"
            ],
            ("realistic", "conventional"): [
                "Building Information Modeling",
                "Quality Control Innovation",
                "Precision Agriculture Management"
            ],
            ("investigative", "artistic"): [
                "Scientific Visualization",
                "Medical Illustration",
                "Data-Driven Art Creation"
            ],
            ("investigative", "social"): [
                "User Research",
                "Educational Technology Development",
                "Health Communication"
            ],
            ("investigative", "enterprising"): [
                "Biotech Entrepreneurship",
                "Technology Investment Analysis",
                "Innovation Strategy Consulting"
            ],
            ("investigative", "conventional"): [
                "Data Science",
                "Computational Linguistics",
                "Bioinformatics"
            ],
            ("artistic", "social"): [
                "Art Therapy",
                "Experience Design",
                "Community Arts Programming"
            ],
            ("artistic", "enterprising"): [
                "Creative Direction",
                "Independent Studio Ownership",
                "Design Entrepreneurship"
            ],
            ("artistic", "conventional"): [
                "Digital Asset Management",
                "Museum Curation",
                "Publication Design"
            ],
            ("social", "enterprising"): [
                "Social Entrepreneurship",
                "Talent Development",
                "Community Organizing"
            ],
            ("social", "conventional"): [
                "Healthcare Information Management",
                "Educational Administration",
                "Social Services Coordination"
            ],
            ("enterprising", "conventional"): [
                "Financial Technology (FinTech)",
                "Business Systems Analysis",
                "Compliance Management"
            ]
        }
        
        # Get top two interest types
        first_type, _ = top_interests[0]
        second_type, _ = top_interests[1]
        
        # Sort the pair to match dictionary keys
        pair = tuple(sorted([first_type, second_type]))
        
        # Get matching careers or default to generic options
        if pair in combinations and pair[0] != pair[1]:  # If it's a valid combination
            careers = combinations[pair]
        else:
            # Default creative options based on top interest
            default_creative = {
                "realistic": ["Custom Fabrication", "Sustainable Construction", "Technical Restoration Specialist"],
                "investigative": ["Independent Research", "Problem-Solving Consultation", "Specialized Technical Writing"],
                "artistic": ["Multimedia Production", "Concept Art", "Creative Platform Development"],
                "social": ["Alternative Education Models", "Community Program Innovation", "Specialized Support Services"],
                "enterprising": ["Niche Market Development", "Industry Disruption Ventures", "Specialized Consulting"],
                "conventional": ["Information System Design", "Process Optimization Consulting", "Specialized Compliance Solutions"]
            }
            careers = default_creative[first_type]
        
        # Format as text
        careers_text = ""
        for career in careers:
            careers_text += f"- {career}\n"
            
        return careers_text
    
    def _get_integration_example(self, top_interests):
        """Get an example of how top interests might integrate in a role"""
        
        first_type, _ = top_interests[0]
        second_type, _ = top_interests[1]
        third_type, _ = top_interests[2]
        
        integration_examples = {
            "realistic": {
                "investigative": "analyzing physical systems and applying technical knowledge",
                "artistic": "creating physical objects with aesthetic considerations",
                "social": "teaching or demonstrating hands-on skills to others",
                "enterprising": "leading teams on technical or physical projects",
                "conventional": "maintaining precise documentation of physical work"
            },
            "investigative": {
                "realistic": "translating research into practical applications",
                "artistic": "visualizing complex data or concepts",
                "social": "explaining complex findings to non-technical audiences",
                "enterprising": "developing business strategies based on research insights",
                "conventional": "creating systematic frameworks for information analysis"
            },
            "artistic": {
                "realistic": "designing functional objects that are also aesthetically pleasing",
                "investigative": "using creative approaches to solve complex problems",
                "social": "creating content that resonates emotionally with audiences",
                "enterprising": "developing unique brand identities or marketing concepts",
                "conventional": "organizing creative assets with meticulous attention to detail"
            },
            "social": {
                "realistic": "helping others develop practical skills",
                "investigative": "researching human behavior or educational methods",
                "artistic": "using creative expression to facilitate human connection",
                "enterprising": "motivating and leading community initiatives",
                "conventional": "organizing and managing human service data systems"
            },
            "enterprising": {
                "realistic": "managing projects with tangible outcomes",
                "investigative": "using data analysis to inform business decisions",
                "artistic": "developing innovative market approaches",
                "social": "building teams and nurturing talent",
                "conventional": "developing efficient business processes and systems"
            },
            "conventional": {
                "realistic": "implementing quality control systems for physical products",
                "investigative": "analyzing patterns in organizational data",
                "artistic": "designing clear and aesthetically pleasing information systems",
                "social": "coordinating people and resources in structured environments",
                "enterprising": "ensuring regulatory compliance while achieving business goals"
            }
        }
        
        # Get examples for first and second types
        example1 = integration_examples.get(first_type, {}).get(second_type, "combining your top interests")
        example2 = integration_examples.get(first_type, {}).get(third_type, "leveraging diverse skills")
        
        return f"{example1} while also {example2}"
    
    def _get_results(self):
        """Get the results of the analysis for other agents to use"""
        
        # Get top three interest areas
        sorted_interests = sorted(self.riasec_scores.items(), key=lambda x: x[1], reverse=True)
        top_three = [area for area, _ in sorted_interests[:3]]
        
        # Map interest areas to career fields
        interest_to_fields = {
            "realistic": ["engineering", "construction", "technical trades", "agriculture", "environmental work"],
            "investigative": ["research", "science", "medicine", "technology", "academia"],
            "artistic": ["design", "writing", "media", "architecture", "creative arts"],
            "social": ["education", "counseling", "healthcare", "human resources", "non-profit"],
            "enterprising": ["business", "law", "sales", "entrepreneurship", "politics"],
            "conventional": ["finance", "administration", "logistics", "data analysis", "quality assurance"]
        }
        
        # Get related fields for top three interests
        related_fields = []
        for interest in top_three:
            related_fields.extend(interest_to_fields.get(interest, []))
        
        # Compile results
        results = {
            "interest_scores": self.riasec_scores,
            "top_interests": top_three,
            "related_fields": related_fields[:10]  # Limit to top 10 fields
        }
        
        return results