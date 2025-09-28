import streamlit as st

class WorkEnvironmentAgent:
    """
    Work Environment Agent - Workplace Ecology Specialist
    Analyzes optimal work environment factors for personal thriving
    """
    
    def __init__(self):
        self.name = "Workplace Ecology Specialist"
        self.description = "Work environment alignment advisor"
        self.questions = [
            "How would you describe your ideal physical work environment? (e.g., office setting, remote, hybrid, etc.)",
            "What aspects of company culture matter most to you? (e.g., collaboration, autonomy, recognition, etc.)",
            "What type of management style do you work best under?",
            "What workplace policies or benefits significantly impact your job satisfaction?"
        ]
        self.current_question_index = 0
        self.responses = []
        self.physical_preferences = []
        self.culture_preferences = []
        self.management_preferences = []
        self.policy_priorities = []
        self.environment_scores = {}
        self.analysis_complete = False
    
    def get_introduction(self):
        """Get the introduction message for this agent"""
        return f"""
        ## Work Environment Assessment
        
        I'm your **{self.name}**, {self.description}. I'll help you identify the workplace 
        characteristics and environmental factors where you're most likely to thrive.
        
        Understanding your ideal work environment is crucial for job satisfaction and 
        performance, as the same role can feel entirely different in different settings.
        
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
            final_analysis = self._generate_environment_analysis()
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
        
        # First question: Physical work environment
        if question_index == 0:
            # Physical environment keywords
            physical_keywords = {
                "remote work": ["remote", "wfh", "work from home", "home office", "virtual", "telecommute"],
                "hybrid work": ["hybrid", "flexible location", "part remote", "part office", "split time"],
                "open office": ["open office", "open plan", "collaborative space", "shared space"],
                "private office": ["private office", "own office", "closed office", "personal space", "quiet space"],
                "co-working space": ["co-working", "coworking", "shared workspace", "workspace", "hot desking"],
                "natural light": ["natural light", "windows", "bright", "sunlight", "well-lit"],
                "quiet environment": ["quiet", "low noise", "peaceful", "calm", "minimal distraction"],
                "dynamic environment": ["dynamic", "energetic", "active", "lively", "bustling"],
                "ergonomic setup": ["ergonomic", "comfortable", "standing desk", "proper chair", "setup"],
                "organized space": ["organized", "clean", "tidy", "structured", "minimal"],
                "tech-enabled": ["tech", "technology", "digital tools", "equipment", "well-equipped"],
                "aesthetic environment": ["aesthetic", "beautiful", "design", "decor", "pleasant", "nice"]
            }
            
            for preference, keywords in physical_keywords.items():
                for keyword in keywords:
                    if keyword in message_lower and preference not in self.physical_preferences:
                        self.physical_preferences.append(preference)
                        break
        
        # Second question: Company culture
        elif question_index == 1:
            # Culture preference keywords
            culture_keywords = {
                "collaborative": ["collaborative", "teamwork", "cooperation", "together", "collective"],
                "autonomous": ["autonomous", "independence", "self-directed", "freedom", "own decisions"],
                "innovative": ["innovative", "creative", "cutting-edge", "experimentation", "new ideas"],
                "structured": ["structured", "organized", "clear processes", "established", "systematic"],
                "learning-focused": ["learning", "growth", "development", "education", "skill-building"],
                "mission-driven": ["mission", "purpose", "meaningful", "impact", "values-driven"],
                "performance-oriented": ["performance", "results", "achievement", "metrics", "goals"],
                "work-life balance": ["work-life", "balance", "flexibility", "personal life", "boundaries"],
                "inclusive": ["inclusive", "diverse", "equity", "belonging", "diversity", "representation"],
                "social": ["social", "friendly", "relationships", "community", "connection", "camaraderie"],
                "competitive": ["competitive", "driven", "ambitious", "high-achieving", "excel"],
                "supportive": ["supportive", "nurturing", "caring", "help", "psychological safety"]
            }
            
            for preference, keywords in culture_keywords.items():
                for keyword in keywords:
                    if keyword in message_lower and preference not in self.culture_preferences:
                        self.culture_preferences.append(preference)
                        break
        
        # Third question: Management style
        elif question_index == 2:
            # Management style keywords
            management_keywords = {
                "coaching style": ["coaching", "mentor", "develop", "guide", "advise", "grow"],
                "hands-off/delegative": ["hands-off", "delegative", "trust", "autonomy", "freedom", "independent"],
                "democratic/participative": ["democratic", "participative", "collaborative", "input", "opinions", "voice", "vote"],
                "directive/authoritative": ["directive", "authoritative", "clear direction", "decisive", "strong leadership", "guidance"],
                "results-oriented": ["results", "outcomes", "objectives", "goals", "achievement", "performance"],
                "supportive": ["supportive", "encouraging", "understanding", "caring", "empathetic"],
                "transparent": ["transparent", "honest", "open", "direct", "straightforward", "communication"],
                "visionary": ["visionary", "inspiring", "big picture", "strategic", "future-focused"],
                "detail-oriented": ["detail", "organized", "thorough", "specific", "careful"],
                "adaptive": ["adaptive", "flexible", "situational", "adjustable", "responsive"]
            }
            
            for preference, keywords in management_keywords.items():
                for keyword in keywords:
                    if keyword in message_lower and preference not in self.management_preferences:
                        self.management_preferences.append(preference)
                        break
        
        # Fourth question: Policies and benefits
        elif question_index == 3:
            # Policy and benefit keywords
            policy_keywords = {
                "flexible hours": ["flexible hours", "flex time", "schedule flexibility", "flexible schedule", "own hours"],
                "professional development": ["professional development", "learning", "education", "training", "growth", "courses"],
                "health benefits": ["health", "insurance", "medical", "wellness", "healthcare", "mental health"],
                "paid time off": ["pto", "vacation", "time off", "leave", "holidays", "personal days"],
                "remote work policy": ["remote work", "wfh", "telecommute", "work from home", "location flexibility"],
                "parental leave": ["parental", "maternity", "paternity", "family", "childcare", "children"],
                "retirement benefits": ["retirement", "401k", "pension", "financial future", "savings plan"],
                "recognition programs": ["recognition", "rewards", "appreciation", "acknowledge", "incentives"],
                "career advancement": ["advancement", "promotion", "career path", "growth track", "progression"],
                "collaborative tools": ["tools", "technology", "software", "resources", "equipment"],
                "diversity initiatives": ["diversity", "inclusion", "equity", "belonging", "dei"],
                "compensation": ["compensation", "salary", "pay", "bonus", "financial", "income"]
            }
            
            for priority, keywords in policy_keywords.items():
                for keyword in keywords:
                    if keyword in message_lower and priority not in self.policy_priorities:
                        self.policy_priorities.append(priority)
                        break
    
    def _get_next_question(self):
        """Get the next question to ask"""
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            return f"**{self.questions[self.current_question_index]}**"
        else:
            return None
    
    def _evaluate_environment_fit(self):
        """
        Evaluate fit between user preferences and common work environments
        This is a simplified model - a real implementation would be more sophisticated
        """
        # Environment profiles with characteristics
        environment_profiles = {
            "startup": {
                "physical": ["open office", "co-working space", "dynamic environment", "tech-enabled"],
                "culture": ["innovative", "autonomous", "collaborative", "mission-driven", "learning-focused"],
                "management": ["visionary", "hands-off/delegative", "adaptive", "results-oriented"],
                "policies": ["equity/ownership", "flexible hours", "remote work policy", "collaborative tools"]
            },
            "established tech company": {
                "physical": ["hybrid work", "tech-enabled", "ergonomic setup", "organized space"],
                "culture": ["innovative", "performance-oriented", "structured", "collaborative"],
                "management": ["results-oriented", "democratic/participative", "transparent", "coaching style"],
                "policies": ["health benefits", "professional development", "flexible hours", "remote work policy"]
            },
            "traditional corporate": {
                "physical": ["private office", "organized space", "quiet environment"],
                "culture": ["structured", "performance-oriented", "competitive", "formal"],
                "management": ["directive/authoritative", "detail-oriented", "results-oriented", "hierarchical"],
                "policies": ["health benefits", "retirement benefits", "career advancement", "structured policies"]
            },
            "creative agency": {
                "physical": ["open office", "aesthetic environment", "natural light", "dynamic environment"],
                "culture": ["innovative", "collaborative", "creative", "social"],
                "management": ["democratic/participative", "visionary", "adaptive", "collaborative"],
                "policies": ["flexible hours", "recognition programs", "creative freedom", "collaborative tools"]
            },
            "remote-first company": {
                "physical": ["remote work", "tech-enabled", "flexible location"],
                "culture": ["autonomous", "results-oriented", "structured communication", "trust-based"],
                "management": ["hands-off/delegative", "results-oriented", "transparent", "trust-building"],
                "policies": ["remote work policy", "flexible hours", "collaborative tools", "clear expectations"]
            },
            "nonprofit organization": {
                "physical": ["hybrid work", "organized space", "mission-focused environment"],
                "culture": ["mission-driven", "collaborative", "supportive", "inclusive"],
                "management": ["supportive", "democratic/participative", "transparent", "mission-aligned"],
                "policies": ["work-life balance", "meaningful work", "inclusive practices", "community focus"]
            },
            "small business": {
                "physical": ["intimate space", "multipurpose areas", "personal touches"],
                "culture": ["family-like", "adaptable", "hands-on", "close-knit"],
                "management": ["direct communication", "versatile", "personal", "involved"],
                "policies": ["flexibility", "personal relationships", "direct impact", "multiple roles"]
            }
        }
        
        # Calculate fit scores for different environments
        for env, profile in environment_profiles.items():
            # Initialize score components
            physical_fit = 0
            culture_fit = 0
            management_fit = 0
            policy_fit = 0
            
            # Physical environment alignment
            physical_match_count = sum(1 for pref in self.physical_preferences if pref in profile["physical"])
            physical_mismatch_count = sum(1 for pref in self.physical_preferences if pref not in profile["physical"] and self._is_contradictory(pref, profile["physical"]))
            
            if self.physical_preferences:
                physical_fit = 100 * (physical_match_count / len(self.physical_preferences))
                # Penalize for direct contradictions
                physical_fit = max(0, physical_fit - 20 * physical_mismatch_count)
            else:
                physical_fit = 50  # Neutral if no preferences specified
            
            # Culture alignment
            culture_match_count = sum(1 for pref in self.culture_preferences if pref in profile["culture"])
            culture_mismatch_count = sum(1 for pref in self.culture_preferences if pref not in profile["culture"] and self._is_contradictory(pref, profile["culture"]))
            
            if self.culture_preferences:
                culture_fit = 100 * (culture_match_count / len(self.culture_preferences))
                # Penalize for direct contradictions
                culture_fit = max(0, culture_fit - 20 * culture_mismatch_count)
            else:
                culture_fit = 50  # Neutral if no preferences specified
            
            # Management style alignment
            management_match_count = sum(1 for pref in self.management_preferences if pref in profile["management"])
            management_mismatch_count = sum(1 for pref in self.management_preferences if pref not in profile["management"] and self._is_contradictory(pref, profile["management"]))
            
            if self.management_preferences:
                management_fit = 100 * (management_match_count / len(self.management_preferences))
                # Penalize for direct contradictions
                management_fit = max(0, management_fit - 20 * management_mismatch_count)
            else:
                management_fit = 50  # Neutral if no preferences specified
            
            # Policy alignment
            policy_match_count = sum(1 for pref in self.policy_priorities if pref in profile["policies"])
            policy_mismatch_count = sum(1 for pref in self.policy_priorities if pref not in profile["policies"] and self._is_contradictory(pref, profile["policies"]))
            
            if self.policy_priorities:
                policy_fit = 100 * (policy_match_count / len(self.policy_priorities))
                # Penalize for direct contradictions
                policy_fit = max(0, policy_fit - 20 * policy_mismatch_count)
            else:
                policy_fit = 50  # Neutral if no preferences specified
            
            # Calculate overall fit score (weighted average)
            overall_fit = (physical_fit * 0.2) + (culture_fit * 0.35) + (management_fit * 0.25) + (policy_fit * 0.2)
            
            # Store the fit score
            self.environment_scores[env] = {
                "overall": int(overall_fit),
                "physical_fit": int(physical_fit),
                "culture_fit": int(culture_fit),
                "management_fit": int(management_fit),
                "policy_fit": int(policy_fit)
            }
    
    def _is_contradictory(self, preference, profile_preferences):
        """Check if a preference directly contradicts any preferences in the profile"""
        contradictions = {
            "remote work": ["in-office requirement"],
            "private office": ["open office", "shared workspace"],
            "quiet environment": ["dynamic environment", "high-energy space"],
            "open office": ["private office"],
            "autonomous": ["micromanaged", "directive/authoritative"],
            "structured": ["unstructured", "completely flexible"],
            "hands-off/delegative": ["directive/authoritative", "micromanaged"],
            "directive/authoritative": ["hands-off/delegative", "fully autonomous"]
        }
        
        if preference in contradictions:
            return any(contra in profile_preferences for contra in contradictions[preference])
        return False
    
    def _generate_environment_analysis(self):
        """Generate a work environment analysis based on the responses"""
        
        # First evaluate environment fit
        self._evaluate_environment_fit()
        
        # Generate the analysis
        analysis = f"""
        ## Work Environment Analysis
        
        Based on our conversation, I've analyzed your preferences for physical workspace, company 
        culture, management style, and workplace policies to identify environments where you're 
        likely to thrive.
        
        ### Your Environment Preferences
        
        #### Physical Workspace Preferences
        """
        
        if self.physical_preferences:
            for preference in self.physical_preferences:
                analysis += f"\n- **{preference.capitalize()}**"
        else:
            analysis += "\nYou haven't specified particular physical workspace preferences."
        
        analysis += "\n\n#### Cultural Elements You Value"
        
        if self.culture_preferences:
            for preference in self.culture_preferences:
                analysis += f"\n- **{preference.capitalize()}**"
        else:
            analysis += "\nYou haven't specified particular company culture preferences."
        
        analysis += "\n\n#### Management Styles You Respond To"
        
        if self.management_preferences:
            for preference in self.management_preferences:
                analysis += f"\n- **{preference.capitalize()}**"
        else:
            analysis += "\nYou haven't specified particular management style preferences."
        
        analysis += "\n\n#### Policies & Benefits You Prioritize"
        
        if self.policy_priorities:
            for priority in self.policy_priorities:
                analysis += f"\n- **{priority.capitalize()}**"
        else:
            analysis += "\nYou haven't specified particular policy or benefit priorities."
        
        # Work environment fit assessment
        analysis += "\n\n### Environment Fit Assessment\n"
        
        if self.environment_scores:
            # Sort environments by fit score
            sorted_environments = sorted(self.environment_scores.items(), key=lambda x: x[1]["overall"], reverse=True)
            
            # Show top 3 environments
            for i, (env, scores) in enumerate(sorted_environments[:3]):
                analysis += f"""
                #### {i+1}. {env.capitalize()} - {scores["overall"]}% Overall Fit
                
                **Compatibility Breakdown:**
                - **Physical Environment**: {scores["physical_fit"]}%
                - **Company Culture**: {scores["culture_fit"]}%
                - **Management Style**: {scores["management_fit"]}%
                - **Policies & Benefits**: {scores["policy_fit"]}%
                """
                
                # Add environment characteristics
                analysis += "\n**Key Characteristics:**\n"
                
                # Define typical characteristics for each environment type
                if env == "startup":
                    analysis += """
                    - Fast-paced, dynamic atmosphere with frequent change
                    - Flatter hierarchies with direct access to leadership
                    - Opportunity for significant impact and varied responsibilities
                    - Limited structure with emphasis on agility and innovation
                    - Resource constraints balanced with potential equity upside
                    """
                elif env == "established tech company":
                    analysis += """
                    - Blend of innovation and established processes
                    - Significant resources for tools and professional development
                    - Structured career paths with advancement opportunities
                    - Data-driven decision making with emphasis on scalability
                    - Product-focused with technical excellence expectations
                    """
                elif env == "traditional corporate":
                    analysis += """
                    - Well-defined structures, roles, and advancement paths
                    - Emphasis on professionalism and established protocols
                    - Comprehensive benefits and stability
                    - Hierarchical decision-making with clear approval chains
                    - Brand reputation and established market position
                    """
                elif env == "creative agency":
                    analysis += """
                    - Creative freedom with aesthetic work environments
                    - Project-based work with variety and client interaction
                    - Emphasis on originality and visual/conceptual thinking
                    - Collaborative brainstorming and ideation processes
                    - Portfolio-building opportunities with visible output
                    """
                elif env == "remote-first company":
                    analysis += """
                    - Location independence with flexible work arrangements
                    - Emphasis on written communication and documentation
                    - Results-oriented performance measurement
                    - Digital-first collaboration tools and processes
                    - Self-direction with asynchronous workflows
                    """
                elif env == "nonprofit organization":
                    analysis += """
                    - Mission-aligned work with social impact focus
                    - Values-driven culture with purpose beyond profit
                    - Collaborative decision-making with stakeholder input
                    - Resource optimization with impact measurement
                    - Community connection and service orientation
                    """
                elif env == "small business":
                    analysis += """
                    - Direct impact on business outcomes
                    - Versatile roles with broad responsibilities
                    - Close-knit team with personal relationships
                    - Limited bureaucracy with nimble decision-making
                    - Localized focus with community connections
                    """
        else:
            analysis += "\nInsufficient information to generate specific environment fit assessments."
        
        # Custom environment design
        analysis += """
        
        ### Designing Your Ideal Work Environment
        
        Based on your preferences, here's a framework for creating or identifying your optimal work setting:
        """
        
        # Highlight key physical preferences if specified
        if any(pref in self.physical_preferences for pref in ["remote work", "hybrid work", "private office", "open office"]):
            analysis += "\n#### Physical Setup Priority\n"
            
            if "remote work" in self.physical_preferences:
                analysis += """
                **Remote-First Optimization:**
                - Invest in a proper home office setup with ergonomic furniture
                - Establish clear boundaries between work and personal spaces
                - Create deliberate social connection points to counter isolation
                - Develop routines that provide structure to remote workdays
                """
            elif "hybrid work" in self.physical_preferences:
                analysis += """
                **Hybrid Work Optimization:**
                - Designate specific tasks for office vs. remote days
                - Create consistency in your workspace setup across locations
                - Be intentional about in-person collaboration opportunities
                - Establish clear communication about your location and availability
                """
            elif "private office" in self.physical_preferences or "quiet environment" in self.physical_preferences:
                analysis += """
                **Focus-Oriented Space:**
                - Prioritize organizations with private or quiet workspace options
                - Invest in noise-cancelling technology for open environments
                - Establish clear focus time protocols with colleagues
                - Create visual signals that indicate when you're in deep work mode
                """
            elif "open office" in self.physical_preferences or "dynamic environment" in self.physical_preferences:
                analysis += """
                **Collaborative Space:**
                - Seek environments with well-designed collaborative areas
                - Balance with access to quieter spaces when needed
                - Develop effective focus strategies for open settings
                - Establish team norms around interruption and availability
                """
        else:
            analysis += "\n#### Physical Setup Considerations\n"
            analysis += """
            Create an environment that balances focus and collaboration:
            - Ensure access to both quiet spaces and collaborative areas
            - Optimize for ergonomics and physical comfort
            - Consider lighting, air quality, and aesthetic elements
            - Establish clear boundaries and signals for different work modes
            """
        
        # Highlight key culture preferences if specified
        analysis += "\n#### Cultural Elements to Seek\n"
        
        priority_cultures = []
        if "collaborative" in self.culture_preferences:
            priority_cultures.append("collaborative")
        if "autonomous" in self.culture_preferences:
            priority_cultures.append("autonomous")
        if "innovative" in self.culture_preferences:
            priority_cultures.append("innovative")
        if "learning-focused" in self.culture_preferences:
            priority_cultures.append("learning-focused")
        
        if priority_cultures:
            for culture in priority_cultures[:2]:  # Focus on top 2
                if culture == "collaborative":
                    analysis += """
                    **Collaborative Culture Indicators:**
                    - Team-based project structures and shared goals
                    - Regular brainstorming and co-creation sessions
                    - Recognition for collective achievements
                    - Physical and digital spaces designed for interaction
                    - Leadership that emphasizes teamwork and cooperation
                    """
                elif culture == "autonomous":
                    analysis += """
                    **Autonomy-Supporting Culture Indicators:**
                    - Outcome-focused rather than process-micromanaged
                    - Clear delegation of authority and decision rights
                    - Trust-based rather than control-based management
                    - Self-directed work planning opportunities
                    - Recognition for initiative and independent problem-solving
                    """
                elif culture == "innovative":
                    analysis += """
                    **Innovation-Oriented Culture Indicators:**
                    - Tolerance for calculated risk and learning from failure
                    - Time and resources allocated for experimentation
                    - Cross-functional collaboration and diverse perspectives
                    - Recognition for new ideas and creative solutions
                    - Leadership that champions change and improvement
                    """
                elif culture == "learning-focused":
                    analysis += """
                    **Learning Culture Indicators:**
                    - Regular professional development opportunities
                    - Knowledge sharing as an organizational norm
                    - Growth mindset in feedback and performance discussions
                    - Recognition for skill development and improvement
                    - Resources allocated for continued education
                    """
        else:
            analysis += """
            Look for these fundamental cultural elements:
            - Alignment between stated values and actual behaviors
            - Psychological safety for sharing ideas and concerns
            - Respectful communication across all levels
            - Appropriate balance of structure and flexibility
            """
        
        # Highlight management preferences
        analysis += "\n#### Management Approach Compatibility\n"
        
        if self.management_preferences:
            primary_style = self.management_preferences[0] if self.management_preferences else None
            
            if primary_style:
                analysis += f"""
                **Finding Your {primary_style.capitalize()} Management Match:**
                
                When interviewing potential managers or organizations, listen for these signals:
                """
                
                if "coaching style" in primary_style:
                    analysis += """
                    - How they've helped team members develop new skills
                    - Questions about your growth goals and aspirations
                    - Examples of team member progress and development
                    - Discussion of regular feedback and development conversations
                    """
                elif "hands-off" in primary_style:
                    analysis += """
                    - Discussion of trust and empowerment philosophies
                    - Questions about your self-direction and initiative
                    - Examples of independent projects they've supported
                    - How they balance autonomy with accountability
                    """
                elif "democratic" in primary_style:
                    analysis += """
                    - How decisions are made within the team
                    - Examples of incorporating team input into planning
                    - Questions about your ideas and perspectives
                    - Discussion of collaborative problem-solving approaches
                    """
                elif "directive" in primary_style:
                    analysis += """
                    - Clear articulation of expectations and standards
                    - Examples of how they provide guidance and direction
                    - Questions about how you respond to structured guidance
                    - Discussion of their leadership philosophy and approach
                    """
                elif "results-oriented" in primary_style:
                    analysis += """
                    - Focus on outcomes rather than methods
                    - Discussion of performance metrics and goals
                    - Questions about your achievement history
                    - Examples of how they evaluate and reward results
                    """
        else:
            analysis += """
            When evaluating potential managers:
            - Ask about their leadership philosophy and approach
            - Inquire how they support team member development
            - Discuss their communication style and frequency
            - Explore how they balance guidance with autonomy
            """
        
        # Policy and benefit recommendations
        analysis += "\n#### Policy & Benefit Priorities\n"
        
        if self.policy_priorities:
            top_policies = self.policy_priorities[:3]  # Focus on top 3
            
            analysis += "When evaluating opportunities, prioritize these specific elements:\n"
            
            for policy in top_policies:
                analysis += f"\n**{policy.capitalize()}**\n"
                
                if "flexible hours" in policy:
                    analysis += "- Look for formal flexible work policies rather than unofficial arrangements\n"
                    analysis += "- Ask about core hours vs. flexible time expectations\n"
                    analysis += "- Inquire about how performance is measured in flexible arrangements\n"
                elif "professional development" in policy:
                    analysis += "- Ask about specific budget allocations for learning\n"
                    analysis += "- Inquire about time allowances for development activities\n"
                    analysis += "- Look for examples of how others have grown in the organization\n"
                elif "health benefits" in policy:
                    analysis += "- Compare coverage details across potential employers\n"
                    analysis += "- Consider both physical and mental health support\n"
                    analysis += "- Evaluate wellness programs and preventative care options\n"
                elif "remote work" in policy:
                    analysis += "- Verify if remote work is policy-supported or manager-dependent\n"
                    analysis += "- Ask about equipment and expense support for remote work\n"
                    analysis += "- Inquire about in-person requirements and frequency\n"
                elif "career advancement" in policy:
                    analysis += "- Ask about typical promotion timelines and criteria\n"
                    analysis += "- Look for clear career ladders or advancement frameworks\n"
                    analysis += "- Inquire about internal mobility and growth opportunities\n"
        else:
            analysis += """
            When evaluating policies and benefits:
            - Look beyond headline benefits to usage policies and limitations
            - Consider which benefits you'll actually utilize regularly
            - Ask current employees about the lived experience of policies
            - Evaluate the complete compensation package rather than individual elements
            """
        
        # Assessment strategies
        analysis += """
        
        ### Environmental Assessment Strategies
        
        When evaluating potential work environments, use these approaches to gather accurate information:
        
        1. **Beyond The Tour Questions:**
           - "What does a typical day look like for people in this role?"
           - "How are decisions typically made on this team?"
           - "What behaviors are most recognized and rewarded here?"
           - "How would you describe the unwritten rules of this workplace?"
        
        2. **Current Employee Intelligence:**
           - Connect with team members outside the interview process
           - Look for consistency or discrepancies in how culture is described
           - Ask about both challenges and strengths of the environment
           - Inquire about how long people typically stay and why they leave
        
        3. **Environmental Observation:**
           - Note how people interact during your interview process
           - Observe the physical space for clues about priorities and values
           - Pay attention to communication styles and energy levels
           - Look for signals of the actual (vs. stated) culture
        
        4. **Compatibility Testing:**
           - Consider how interview questions align with stated culture
           - Note whether your questions about environment are welcomed
           - Reflect on your comfort level during interactions
           - Trust your intuition about environment fit
        
        Remember that finding the right environment is as important as finding the right role. Even a perfect position can be undermined by an environment that conflicts with your work style and preferences.
        """
        
        return analysis
    
    def _get_results(self):
        """Get the results of the analysis for other agents to use"""
        
        # Format preferences
        physical = [pref.capitalize() for pref in self.physical_preferences]
        culture = [pref.capitalize() for pref in self.culture_preferences]
        management = [pref.capitalize() for pref in self.management_preferences]
        policies = [policy.capitalize() for policy in self.policy_priorities]
        
        # Format environment scores
        env_scores = {}
        for env, score in self.environment_scores.items():
            env_scores[env.capitalize()] = score
        
        # Get top environment match
        top_environment = None
        top_score = 0
        for env, score in self.environment_scores.items():
            if score["overall"] > top_score:
                top_environment = env
                top_score = score["overall"]
        
        # Compile results
        results = {
            "physical_preferences": physical,
            "culture_preferences": culture,
            "management_preferences": management,
            "policy_priorities": policies,
            "environment_scores": env_scores,
            "top_environment_match": top_environment.capitalize() if top_environment else None
        }
        
        return results