import streamlit as st

class CareerTrajectoryAgent:
    """
    Career Trajectory Agent - Strategic Pathway Designer
    Develops strategic career paths with informed progression planning
    """
    
    def __init__(self):
        self.name = "Strategic Pathway Designer"
        self.description = "Career trajectory and advancement specialist"
        self.questions = [
            "What are your short-term career goals (next 1-2 years)?",
            "What are your medium to long-term career aspirations (3-10 years)?",
            "What do you see as potential obstacles or challenges to reaching these goals?",
            "What resources, skills, or support do you think you'll need to advance along your desired path?"
        ]
        self.current_question_index = 0
        self.responses = []
        self.short_term_goals = []
        self.long_term_goals = []
        self.obstacles = []
        self.resources_needed = []
        self.path_recommendations = {}
        self.analysis_complete = False
    
    def get_introduction(self):
        """Get the introduction message for this agent"""
        return f"""
        ## Career Trajectory Assessment
        
        I'm your **{self.name}**, {self.description}. I'll help you map out strategic career 
        pathways and develop progression plans that align with your goals and aspirations.
        
        Understanding where you want to go and how to get there is essential for making 
        informed career decisions and investments. Let's create a roadmap for your professional journey.
        
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
            final_analysis = self._generate_trajectory_analysis()
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
        
        # First question: Short-term goals
        if question_index == 0:
            short_term_keywords = {
                "promotion": ["promotion", "advance", "move up", "next level", "higher position", "senior"],
                "skill development": ["learn", "develop", "improve", "gain", "build", "enhance", "master"],
                "project leadership": ["lead", "manage", "oversee", "direct", "head", "run", "coordinate"],
                "specialization": ["specialize", "focus", "expertise", "concentration", "deepen knowledge"],
                "industry transition": ["transition", "move to", "switch to", "change to", "pivot", "shift"],
                "role change": ["new role", "different position", "change roles", "new position", "job change"],
                "entrepreneurship": ["start", "launch", "found", "create", "my own", "business", "company"],
                "networking": ["network", "connections", "relationships", "expand circle", "meet", "connect"],
                "certification": ["certif", "credential", "qualification", "license", "exam", "diploma"],
                "work-life balance": ["balance", "flexibility", "hours", "remote", "lifestyle", "family"]
            }
            
            for goal, keywords in short_term_keywords.items():
                for keyword in keywords:
                    if keyword in message_lower and goal not in self.short_term_goals:
                        self.short_term_goals.append(goal)
                        break
            
            # Extract specific titles, roles, or positions mentioned
            title_indicators = ["become a", "position as", "role as", "work as", "job as", "title of"]
            for indicator in title_indicators:
                if indicator in message_lower:
                    # Look for surrounding context
                    index = message_lower.find(indicator)
                    start = index + len(indicator)
                    end = min(start + 30, len(message_lower))
                    potential_title = message_lower[start:end].strip()
                    
                    # Extract the title (simplified approach)
                    import re
                    title_match = re.search(r'^([a-z\s]+)', potential_title)
                    if title_match:
                        title = title_match.group(0).strip()
                        if title and "specific title: " + title not in self.short_term_goals:
                            self.short_term_goals.append("specific title: " + title)
        
        # Second question: Long-term goals
        elif question_index == 1:
            long_term_keywords = {
                "executive leadership": ["executive", "c-suite", "director", "chief", "vp", "head of", "leader"],
                "expert status": ["expert", "thought leader", "authority", "recognized", "known for", "specialist"],
                "business ownership": ["own business", "my company", "entrepreneur", "founder", "start company"],
                "career change": ["change careers", "new field", "different industry", "switch to", "transition to"],
                "work impact": ["impact", "difference", "change", "improve", "solve", "contribute", "meaningful"],
                "financial goals": ["salary", "compensation", "earn", "income", "financial", "money", "pay"],
                "work-life integration": ["balance", "flexibility", "lifestyle", "family", "freedom", "location"],
                "legacy building": ["legacy", "lasting", "remember", "known for", "contribution", "leave behind"],
                "international": ["global", "international", "abroad", "overseas", "different country", "worldwide"],
                "portfolio career": ["portfolio", "multiple", "diverse", "variety", "different roles", "combination"]
            }
            
            for goal, keywords in long_term_keywords.items():
                for keyword in keywords:
                    if keyword in message_lower and goal not in self.long_term_goals:
                        self.long_term_goals.append(goal)
                        break
            
            # Extract specific positions or achievements mentioned
            position_indicators = ["become", "position as", "role as", "achieve", "reach"]
            for indicator in position_indicators:
                if indicator in message_lower:
                    # Look for surrounding context
                    index = message_lower.find(indicator)
                    start = index + len(indicator)
                    end = min(start + 30, len(message_lower))
                    potential_position = message_lower[start:end].strip()
                    
                    # Extract the position (simplified approach)
                    import re
                    position_match = re.search(r'^([a-z\s]+)', potential_position)
                    if position_match:
                        position = position_match.group(0).strip()
                        if position and "specific goal: " + position not in self.long_term_goals:
                            self.long_term_goals.append("specific goal: " + position)
        
        # Third question: Obstacles
        elif question_index == 2:
            obstacle_keywords = {
                "skill gaps": ["skills", "abilities", "capabilities", "technical", "knowledge", "experience", "expertise"],
                "credential requirements": ["degree", "education", "certification", "qualification", "credentials", "license"],
                "network limitations": ["network", "connections", "relationships", "contacts", "referrals", "who you know"],
                "experience gaps": ["experience", "background", "track record", "history", "proven", "demonstrated"],
                "market conditions": ["market", "economy", "industry", "sector", "demand", "opportunities", "jobs"],
                "competition": ["competitive", "competition", "others", "candidates", "applicants", "many people"],
                "geographic constraints": ["location", "relocation", "move", "geographic", "region", "city", "area"],
                "personal circumstances": ["family", "personal", "health", "financial", "situation", "circumstances"],
                "organizational limitations": ["company", "organization", "employer", "structure", "advancement", "promotion"],
                "work-life balance": ["balance", "time", "hours", "commitment", "demands", "responsibilities"],
                "discrimination/bias": ["bias", "discrimination", "prejudice", "stereotype", "barrier", "ceiling", "unfair"],
                "visibility/recognition": ["visibility", "recognition", "noticed", "seen", "acknowledged", "appreciated"]
            }
            
            for obstacle, keywords in obstacle_keywords.items():
                for keyword in keywords:
                    if keyword in message_lower and obstacle not in self.obstacles:
                        self.obstacles.append(obstacle)
                        break
            
            # Extract specific obstacles mentioned
            obstacle_indicators = ["challenge", "obstacle", "barrier", "difficult", "hard", "trouble", "issue", "problem"]
            for indicator in obstacle_indicators:
                if indicator in message_lower:
                    # Look for surrounding context
                    index = message_lower.find(indicator)
                    start = max(0, index - 20)
                    end = min(index + 30, len(message_lower))
                    context = message_lower[start:end]
                    
                    # Extract potential specific obstacles
                    import re
                    for word in re.findall(r'\b[a-z]{5,}\b', context):
                        if word not in ["challenge", "obstacle", "barrier", "difficult"] and word not in self.obstacles:
                            if "specific obstacle: " + word not in self.obstacles:
                                self.obstacles.append("specific obstacle: " + word)
        
        # Fourth question: Resources needed
        elif question_index == 3:
            resource_keywords = {
                "education": ["education", "degree", "school", "university", "college", "course", "program"],
                "training": ["training", "workshop", "seminar", "bootcamp", "class", "instruction"],
                "mentorship": ["mentor", "guidance", "advise", "coach", "support", "direction"],
                "networking": ["network", "connections", "relationships", "contacts", "meet", "connect"],
                "experience": ["experience", "practice", "exposure", "opportunity", "hands-on"],
                "funding": ["money", "funding", "financial", "budget", "cost", "investment", "savings"],
                "time": ["time", "hours", "schedule", "availability", "balance"],
                "specific skills": ["skills", "abilities", "capabilities", "competencies", "proficiencies"],
                "technology/tools": ["tools", "technology", "software", "equipment", "resources", "platform"],
                "information/knowledge": ["information", "knowledge", "insight", "understanding", "awareness"],
                "support system": ["support", "help", "assistance", "encouragement", "backing"],
                "self-development": ["confidence", "mindset", "attitude", "belief", "motivation", "discipline"]
            }
            
            for resource, keywords in resource_keywords.items():
                for keyword in keywords:
                    if keyword in message_lower and resource not in self.resources_needed:
                        self.resources_needed.append(resource)
                        break
            
            # Extract specific resources mentioned
            resource_indicators = ["need", "require", "help", "support", "assistance", "looking for"]
            for indicator in resource_indicators:
                if indicator in message_lower:
                    # Look for surrounding context
                    index = message_lower.find(indicator)
                    start = index + len(indicator)
                    end = min(start + 30, len(message_lower))
                    potential_resource = message_lower[start:end].strip()
                    
                    # Extract the resource (simplified approach)
                    import re
                    resource_match = re.search(r'^([a-z\s]+)', potential_resource)
                    if resource_match:
                        resource = resource_match.group(0).strip()
                        if resource and "specific resource: " + resource not in self.resources_needed:
                            self.resources_needed.append("specific resource: " + resource)
    
    def _get_next_question(self):
        """Get the next question to ask"""
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            return f"**{self.questions[self.current_question_index]}**"
        else:
            return None
    
    def _identify_career_paths(self):
        """
        Identify potential career paths based on goals and aspirations
        This is a simplified implementation - a real one would use more sophisticated logic
        """
        # Define common career paths with characteristics
        career_paths = {
            "specialist/expert track": {
                "description": "Deepening expertise in a specific domain, becoming recognized for specialized knowledge and skills",
                "short_term_indicators": ["skill development", "specialization", "certification"],
                "long_term_indicators": ["expert status", "thought leadership", "specialized impact"],
                "progression_milestones": [
                    "Entry specialist role",
                    "Intermediate specialist with demonstrated expertise",
                    "Senior specialist with recognized domain authority",
                    "Principal/lead specialist guiding domain strategy",
                    "Distinguished expert/thought leader in the field"
                ],
                "development_priorities": [
                    "Deep technical skill development",
                    "Specialized credentials and certifications",
                    "Research and knowledge contribution",
                    "Visibility through speaking and publishing",
                    "Problem-solving portfolio in specialty area"
                ],
                "score": 0
            },
            "management track": {
                "description": "Taking on increasing people and organizational leadership responsibilities",
                "short_term_indicators": ["promotion", "project leadership", "team management"],
                "long_term_indicators": ["executive leadership", "organizational impact"],
                "progression_milestones": [
                    "Team lead or project management responsibilities",
                    "Manager of a functional team",
                    "Director overseeing multiple teams or a department",
                    "VP/Senior executive leading organization divisions",
                    "C-suite or enterprise leadership"
                ],
                "development_priorities": [
                    "Leadership and people management skills",
                    "Strategic thinking and business acumen",
                    "Cross-functional collaboration",
                    "Organizational development and change management",
                    "Executive presence and influence"
                ],
                "score": 0
            },
            "entrepreneurial track": {
                "description": "Building ventures, whether independent businesses or entrepreneurial initiatives within organizations",
                "short_term_indicators": ["entrepreneurship", "project leadership", "autonomy"],
                "long_term_indicators": ["business ownership", "financial independence", "legacy building"],
                "progression_milestones": [
                    "Side projects or entrepreneurial responsibilities",
                    "Founding or co-founding initial venture",
                    "Growing and stabilizing business operations",
                    "Scaling or expanding business reach",
                    "Portfolio development or strategic exit"
                ],
                "development_priorities": [
                    "Business model development",
                    "Market research and customer development",
                    "Fundraising and financial management",
                    "Leadership and team building",
                    "Strategic planning and execution"
                ],
                "score": 0
            },
            "project/product track": {
                "description": "Leading increasingly significant projects, products, or initiatives with cross-functional impact",
                "short_term_indicators": ["project leadership", "skill development", "cross-functional"],
                "long_term_indicators": ["portfolio management", "organizational impact", "innovation leadership"],
                "progression_milestones": [
                    "Project team member with specific responsibilities",
                    "Project lead or product owner",
                    "Senior project/product manager with strategic ownership",
                    "Program manager overseeing multiple projects/products",
                    "Portfolio director setting project/product strategy"
                ],
                "development_priorities": [
                    "Project/product management methodologies",
                    "Stakeholder management and communication",
                    "Technical and domain knowledge",
                    "Cross-functional leadership",
                    "Strategic prioritization and resource allocation"
                ],
                "score": 0
            },
            "portfolio/hybrid track": {
                "description": "Developing a diverse portfolio of roles, skills, and income streams rather than a linear progression",
                "short_term_indicators": ["skill development", "role change", "diversification"],
                "long_term_indicators": ["portfolio career", "work-life integration", "diverse impact"],
                "progression_milestones": [
                    "Initial role with side projects or additional responsibilities",
                    "Multiple complementary roles or income streams",
                    "Established portfolio with intentional balance",
                    "Strategic integration of portfolio elements",
                    "Optimized portfolio with maximum leverage and minimum friction"
                ],
                "development_priorities": [
                    "Diverse skill development across domains",
                    "Personal brand as a connector of different areas",
                    "Time and energy management across commitments",
                    "Strategic networking across multiple communities",
                    "Identifying synergies between portfolio elements"
                ],
                "score": 0
            }
        }
        
        # Score career paths based on goal alignment
        for path, attributes in career_paths.items():
            score = 0
            
            # Score based on short-term goals
            for goal in self.short_term_goals:
                # Extract the core goal without "specific" prefix
                core_goal = goal.replace("specific title: ", "").lower()
                
                # Check if goal matches path indicators
                if any(indicator in core_goal for indicator in attributes["short_term_indicators"]):
                    score += 2
                # Check for specific role mentions that align with this path
                elif "specialist" in path and any(term in core_goal for term in ["expert", "specialist", "technical", "analyst"]):
                    score += 2
                elif "management" in path and any(term in core_goal for term in ["manager", "director", "lead", "supervisor"]):
                    score += 2
                elif "entrepreneurial" in path and any(term in core_goal for term in ["founder", "start", "business", "entrepreneur"]):
                    score += 2
                elif "project" in path and any(term in core_goal for term in ["project", "product", "program", "initiative"]):
                    score += 2
                elif "portfolio" in path and any(term in core_goal for term in ["diverse", "multiple", "balance", "variety"]):
                    score += 2
            
            # Score based on long-term goals
            for goal in self.long_term_goals:
                # Extract the core goal without "specific" prefix
                core_goal = goal.replace("specific goal: ", "").lower()
                
                # Check if goal matches path indicators
                if any(indicator in core_goal for indicator in attributes["long_term_indicators"]):
                    score += 3  # Higher weight for long-term alignment
                # Check for specific role mentions that align with this path
                elif "specialist" in path and any(term in core_goal for term in ["expert", "specialist", "authority", "thought leader"]):
                    score += 3
                elif "management" in path and any(term in core_goal for term in ["executive", "chief", "director", "leader"]):
                    score += 3
                elif "entrepreneurial" in path and any(term in core_goal for term in ["founder", "owner", "company", "business"]):
                    score += 3
                elif "project" in path and any(term in core_goal for term in ["portfolio", "program", "product", "initiative"]):
                    score += 3
                elif "portfolio" in path and any(term in core_goal for term in ["balance", "variety", "multiple", "diverse"]):
                    score += 3
            
            # Store the score
            career_paths[path]["score"] = score
        
        # Sort paths by score
        sorted_paths = sorted(career_paths.items(), key=lambda x: x[1]["score"], reverse=True)
        
        # Store top paths for later use
        self.path_recommendations = {name: details for name, details in sorted_paths if details["score"] > 0}
        
        return sorted_paths
    
    def _generate_trajectory_analysis(self):
        """Generate a career trajectory analysis based on the responses"""
        
        # First identify potential career paths
        career_paths = self._identify_career_paths()
        
        # Generate the analysis
        analysis = f"""
        ## Career Trajectory Analysis
        
        Based on our conversation, I've analyzed your goals, aspirations, and potential challenges 
        to help you develop a strategic career pathway that aligns with your objectives.
        
        ### Your Career Goals
        
        #### Short-Term Goals (1-2 years)
        """
        
        if self.short_term_goals:
            for goal in self.short_term_goals:
                goal_text = goal
                if goal.startswith("specific title:"):
                    goal_text = f"Target role: **{goal.replace('specific title:', '').strip().capitalize()}**"
                else:
                    goal_text = f"**{goal.capitalize()}**"
                analysis += f"\n- {goal_text}"
        else:
            analysis += "\nYou haven't specified clear short-term career goals."
        
        analysis += "\n\n#### Medium to Long-Term Aspirations (3-10 years)"
        
        if self.long_term_goals:
            for goal in self.long_term_goals:
                goal_text = goal
                if goal.startswith("specific goal:"):
                    goal_text = f"**{goal.replace('specific goal:', '').strip().capitalize()}**"
                else:
                    goal_text = f"**{goal.capitalize()}**"
                analysis += f"\n- {goal_text}"
        else:
            analysis += "\nYou haven't specified clear long-term career aspirations."
        
        analysis += "\n\n### Potential Challenges"
        
        if self.obstacles:
            for obstacle in self.obstacles:
                obstacle_text = obstacle
                if obstacle.startswith("specific obstacle:"):
                    obstacle_text = f"**{obstacle.replace('specific obstacle:', '').strip().capitalize()}**"
                else:
                    obstacle_text = f"**{obstacle.capitalize()}**"
                analysis += f"\n- {obstacle_text}"
        else:
            analysis += "\nYou haven't specified potential obstacles to your career progress."
        
        analysis += "\n\n### Resources & Support Needed"
        
        if self.resources_needed:
            for resource in self.resources_needed:
                resource_text = resource
                if resource.startswith("specific resource:"):
                    resource_text = f"**{resource.replace('specific resource:', '').strip().capitalize()}**"
                else:
                    resource_text = f"**{resource.capitalize()}**"
                analysis += f"\n- {resource_text}"
        else:
            analysis += "\nYou haven't specified resources or support needed for your career advancement."
        
        # Career path recommendations
        analysis += "\n\n### Career Pathway Recommendations\n"
        
        if career_paths and career_paths[0][1]["score"] > 0:
            # Primary recommended path
            primary_path = career_paths[0]
            
            analysis += f"""
            Based on your goals and aspirations, your most aligned career pathway appears to be the **{primary_path[0].capitalize()}**.
            
            **{primary_path[0].capitalize()}**: {primary_path[1]["description"]}
            
            #### Typical Progression Milestones:
            """
            
            for milestone in primary_path[1]["progression_milestones"]:
                analysis += f"\n{milestone_index+1}. {milestone}" if 'milestone_index' in locals() else f"\n1. {milestone}"
                milestone_index = 0 if not 'milestone_index' in locals() else milestone_index + 1
            
            analysis += "\n\n#### Key Development Priorities:"
            
            for priority in primary_path[1]["development_priorities"]:
                analysis += f"\n- {priority}"
            
            # If there's a secondary path with a non-zero score, include it
            if len(career_paths) > 1 and career_paths[1][1]["score"] > 0:
                secondary_path = career_paths[1]
                
                analysis += f"""
                
                #### Alternative Pathway: {secondary_path[0].capitalize()}
                
                You also show alignment with the **{secondary_path[0].capitalize()}** ({secondary_path[1]["description"]}), which could be:
                
                - A parallel development track alongside your primary path
                - An alternative if your primary path encounters obstacles
                - A future evolution of your career after progress on your primary path
                """
        else:
            analysis += """
            Based on your responses, there isn't a clear alignment with common career pathways. This could mean:
            
            1. You're in an exploratory career phase, still discovering direction
            2. You're creating a highly customized path that blends multiple trajectories
            3. You might benefit from more specific goal articulation to clarify your path
            
            Consider exploring different career archetypes to identify which elements resonate most with you.
            """
        
        # Strategic recommendations
        analysis += """
        
        ### Strategic Trajectory Planning
        
        To move effectively toward your career goals:
        
        #### 1. Near-Term Strategic Moves
        """
        
        # Near-term recommendations based on short-term goals and obstacles
        if self.short_term_goals:
            if any(goal in ["promotion", "project leadership", "specialization"] for goal in self.short_term_goals):
                analysis += """
                **Growth Within Current Role:**
                - Identify stretch assignments that demonstrate readiness for advancement
                - Build visibility through high-impact projects or initiatives
                - Document achievements and quantifiable contributions
                - Clearly communicate your advancement interests to decision-makers
                - Seek specific feedback on promotion readiness and gap areas
                """
            
            if any(goal in ["skill development", "certification"] for goal in self.short_term_goals):
                analysis += """
                **Skill & Credential Development:**
                - Create a prioritized learning plan aligned with your target role requirements
                - Identify both formal education and practical application opportunities
                - Secure projects that allow you to apply and demonstrate new skills
                - Build portfolio evidence of your developing capabilities
                - Connect with others who have successfully developed similar skills
                """
            
            if any(goal in ["role change", "industry transition"] for goal in self.short_term_goals):
                analysis += """
                **Transition Preparation:**
                - Research specific requirements for target roles or industries
                - Identify transferable skills and experience you can leverage
                - Develop narratives that reframe your background for new contexts
                - Build strategic network connections in target areas
                - Consider bridge roles that can facilitate your transition
                """
            
            if any(goal in ["entrepreneurship"] for goal in self.short_term_goals):
                analysis += """
                **Entrepreneurial Foundation:**
                - Start with small entrepreneurial projects to test and learn
                - Build business fundamentals through education and mentorship
                - Develop minimally viable offerings to validate market interest
                - Create financial runway to support transition to entrepreneurship
                - Cultivate relationships with potential partners, advisors, or investors
                """
        else:
            analysis += """
            Establish clear near-term objectives by:
            - Identifying what specific achievements would represent progress
            - Setting measurable milestones for the next 3, 6, and 12 months
            - Creating accountability structures for your goals
            - Aligning daily and weekly activities with your objectives
            - Regularly reassessing and adjusting your tactical approach
            """
        
        # Medium-term recommendations
        analysis += "\n\n#### 2. Medium-Term Strategic Positioning\n"
        
        if self.long_term_goals:
            if any(goal in ["executive leadership", "expert status"] for goal in self.long_term_goals):
                analysis += """
                **Strategic Visibility:**
                - Seek opportunities to demonstrate leadership or expertise beyond your immediate role
                - Develop your personal brand and professional narrative
                - Build strategic relationships with senior leaders or industry influencers
                - Contribute to your field through speaking, writing, or other visible platforms
                - Seek cross-functional or enterprise-wide project involvement
                """
            
            if any(goal in ["career change", "work impact"] for goal in self.long_term_goals):
                analysis += """
                **Exploratory Positioning:**
                - Create intentional exploration opportunities through projects or responsibilities
                - Develop relationships with people already doing what interests you
                - Test assumptions about target paths through informational interviews
                - Build bridge skills that connect your current expertise to future interests
                - Seek volunteer or side project opportunities in areas of interest
                """
            
            if any(goal in ["business ownership", "portfolio career"] for goal in self.long_term_goals):
                analysis += """
                **Independence Foundation:**
                - Develop multiple skill streams that create diversified value
                - Begin building audience, network, or customer relationships
                - Create systems to track and nurture your professional connections
                - Test smaller offerings or services to validate your approach
                - Build financial resources to support future independence
                """
        else:
            analysis += """
            To create directional momentum:
            - Explore different potential career directions through informational interviews
            - Test possible paths through projects, volunteer work, or learning experiences
            - Identify what work environments and activities energize you most
            - Consider what impact or contribution would feel most meaningful
            - Develop a broad skill foundation while exploring specific paths
            """
        
        # Addressing obstacles
        analysis += "\n\n#### 3. Overcoming Key Obstacles\n"
        
        if self.obstacles:
            if any(obstacle in ["skill gaps", "credential requirements"] for obstacle in self.obstacles):
                analysis += """
                **Addressing Skill & Credential Gaps:**
                - Conduct a specific gap analysis between current and required capabilities
                - Prioritize development based on impact and acquisition difficulty
                - Create learning pathways that combine formal education and practical application
                - Find opportunities to demonstrate developing skills in current role
                - Build relationships with mentors who can guide skill development
                """
            
            if any(obstacle in ["experience gaps", "network limitations", "visibility/recognition"] for obstacle in self.obstacles):
                analysis += """
                **Addressing Experience & Visibility Gaps:**
                - Seek stretch assignments and projects that build relevant experience
                - Volunteer for cross-functional initiatives to expand your exposure
                - Document and quantify your contributions and achievements
                - Build strategic relationships with decision-makers and influencers
                - Create opportunities to demonstrate capabilities beyond your formal role
                """
            
            if any(obstacle in ["market conditions", "competition", "organizational limitations"] for obstacle in self.obstacles):
                analysis += """
                **Addressing External & Structural Challenges:**
                - Research specific market trends and requirements to stay competitive
                - Develop unique combination of skills or experiences for differentiation
                - Consider alternative paths to your goals through different organizations or approaches
                - Build resilience through multiple options and contingency planning
                - Identify and prepare for emerging opportunities in adjacent areas
                """
            
            if any(obstacle in ["personal circumstances", "work-life balance", "geographic constraints"] for obstacle in self.obstacles):
                analysis += """
                **Addressing Personal & Practical Challenges:**
                - Identify creative alternatives that accommodate your constraints
                - Build support systems that enable your career development
                - Consider phased approaches that gradually move toward your goals
                - Explore remote, flexible, or alternative work arrangements
                - Focus on high-leverage activities that maximize impact within constraints
                """
        else:
            analysis += """
            To preemptively address potential obstacles:
            - Identify what typically derails career progress in your field
            - Build contingency plans for different potential challenges
            - Develop resilience through multiple pathways toward your goals
            - Create support systems to help navigate inevitable obstacles
            - Regularly reassess and adjust your approach based on changing circumstances
            """
        
        # Resource acquisition strategies
        analysis += "\n\n#### 4. Resource Acquisition Strategy\n"
        
        if self.resources_needed:
            if any(resource in ["education", "training", "specific skills"] for resource in self.resources_needed):
                analysis += """
                **Learning & Development Resources:**
                - Research both traditional and alternative education pathways
                - Consider combinations of formal credentials and practical skill development
                - Explore employer-supported education or development opportunities
                - Investigate industry-recognized certifications and their ROI
                - Build learning communities or study groups for mutual support
                """
            
            if any(resource in ["mentorship", "networking", "support system"] for resource in self.resources_needed):
                analysis += """
                **Relationship & Support Resources:**
                - Identify specific types of mentorship or guidance needed
                - Create a strategic networking plan focused on quality relationships
                - Join or create communities related to your aspirations
                - Develop reciprocal value exchanges in professional relationships
                - Build diverse support networks for different needs (technical, emotional, strategic)
                """
            
            if any(resource in ["experience", "information/knowledge"] for resource in self.resources_needed):
                analysis += """
                **Experience & Knowledge Resources:**
                - Create experience acquisition plans through projects or responsibilities
                - Develop systematic approaches to industry and role research
                - Build relationships with people who have your target experiences
                - Create learning systems to organize and apply new knowledge
                - Seek opportunities to apply knowledge through teaching or sharing
                """
            
            if any(resource in ["funding", "time", "technology/tools"] for resource in self.resources_needed):
                analysis += """
                **Practical & Logistical Resources:**
                - Create specific plans for funding development activities
                - Develop time management systems to support career advancement
                - Research tools and technologies that can accelerate your progress
                - Identify resource-efficient approaches to development
                - Consider shared resources or collaborative approaches
                """
        else:
            analysis += """
            To build your resource foundation:
            - Conduct a comprehensive audit of resources needed for your goals
            - Prioritize resource acquisition based on impact and accessibility
            - Identify creative and alternative approaches to resource challenges
            - Build systems to maximize the value of limited resources
            - Create resource acquisition timelines aligned with your career phases
            """
        
        # Progress metrics and milestones
        analysis += """
        
        ### Progress Measurement Framework
        
        Track your career trajectory progress through these key indicators:
        
        #### 1. Development Milestones
        
        **Knowledge & Skills**
        - Formal credentials or certifications acquired
        - Mastery demonstrations through projects or responsibilities
        - Feedback on skill application from trusted observers
        - Ability to teach or mentor others in your skill areas
        
        **Experience & Evidence**
        - Completion of progressively challenging projects or responsibilities
        - Portfolio of achievements and contributions
        - Application of capabilities in diverse contexts
        - Track record of results and impact
        
        #### 2. Advancement Indicators
        
        **Role Evolution**
        - Increasing scope of responsibility
        - Greater autonomy or decision authority
        - More strategic or impactful assignments
        - Higher level stakeholder engagement
        
        **Recognition Markers**
        - Formal advancement or promotion
        - Expanded informal influence
        - Requests for your expertise or contribution
        - Reputation development within organization or industry
        
        #### 3. Opportunity Expansion
        
        **Internal Opportunities**
        - Invitations to strategic initiatives
        - Access to senior leadership or decision-makers
        - Choice of assignments or projects
        - Voice in organizational direction
        
        **External Opportunities**
        - Inbound interest from other organizations
        - Speaking, writing, or contribution invitations
        - Network growth and quality
        - Industry recognition or positioning
        
        #### 4. Satisfaction & Alignment
        
        **Professional Fulfillment**
        - Engagement and energy in your work
        - Sense of growth and development
        - Alignment with your values and purpose
        - Impact that matters to you
        
        **Life Integration**
        - Sustainability of your career pace and demands
        - Balance with other life priorities and goals
        - Financial trajectory alignment with needs
        - Overall life satisfaction and wellbeing
        
        Remember that career development is rarely linear or perfectly predictable. By maintaining both 
        clarity of direction and flexibility of approach, you can navigate effectively toward your 
        long-term aspirations while adapting to changing circumstances and opportunities.
        """
        
        return analysis
    
    def _get_results(self):
        """Get the results of the analysis for other agents to use"""
        
        # Format goals
        short_term = [goal.capitalize() for goal in self.short_term_goals]
        long_term = [goal.capitalize() for goal in self.long_term_goals]
        
        # Format obstacles
        obstacles = [obstacle.capitalize() for obstacle in self.obstacles]
        
        # Format resources
        resources = [resource.capitalize() for resource in self.resources_needed]
        
        # Get top career path
        top_path = None
        if self.path_recommendations:
            top_path = next(iter(self.path_recommendations))
        
        # Format path recommendations
        paths = {}
        for name, details in self.path_recommendations.items():
            paths[name.capitalize()] = {
                "score": details["score"],
                "description": details["description"],
                "milestones": details["progression_milestones"][:3]
            }
        
        # Compile results
        results = {
            "short_term_goals": short_term,
            "long_term_goals": long_term,
            "obstacles": obstacles,
            "resources_needed": resources,
            "recommended_paths": paths,
            "primary_path": top_path.capitalize() if top_path else None
        }
        
        return results