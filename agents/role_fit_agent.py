import streamlit as st

class RoleFitAgent:
    """
    Role Fit Agent - Role Compatibility Advisor
    Analyzes role fit and provides strategic positioning advice for target roles
    """
    
    def __init__(self):
        self.name = "Role Compatibility Advisor"
        self.description = "Job role fit analyst and positioning strategist"
        self.questions = [
            "What specific job roles or titles are you most interested in pursuing?",
            "What aspects of your work do you find most energizing or engaging on a day-to-day basis?",
            "What parts of your work tend to drain your energy or feel like a poor fit for your natural strengths?",
            "In your ideal role, what percentage of your time would you spend on different activities (e.g., individual work, collaboration, creative tasks, analytical tasks, etc.)?"
        ]
        self.current_question_index = 0
        self.responses = []
        self.target_roles = []
        self.energizing_activities = []
        self.draining_activities = []
        self.ideal_allocation = {}
        self.role_fit_scores = {}
        self.analysis_complete = False
    
    def get_introduction(self):
        """Get the introduction message for this agent"""
        return f"""
        ## Role Fit Assessment
        
        I'm your **{self.name}**, {self.description}. I'll help you evaluate how well different 
        roles align with your natural strengths, work preferences, and desired work style.
        
        Understanding role fit is crucial for finding positions where you'll thrive naturally 
        rather than having to constantly adapt to misaligned expectations or activities.
        
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
            final_analysis = self._generate_role_fit_analysis()
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
        
        # First question: Target roles
        if question_index == 0:
            # Common job roles by category
            role_keywords = {
                # Technical roles
                "software engineer": ["software engineer", "developer", "programmer", "coder", "software development"],
                "data scientist": ["data scientist", "data analyst", "analytics", "machine learning", "ml engineer"],
                "product manager": ["product manager", "product owner", "product development", "product management"],
                "ux designer": ["ux designer", "ui designer", "user experience", "interface designer", "ux/ui"],
                "data engineer": ["data engineer", "data architecture", "database", "data infrastructure"],
                "devops engineer": ["devops", "site reliability", "infrastructure", "platform engineer"],
                
                # Business roles
                "marketing manager": ["marketing manager", "marketing specialist", "digital marketing", "brand manager"],
                "business analyst": ["business analyst", "business intelligence", "bi analyst"],
                "project manager": ["project manager", "project lead", "project coordinator", "program manager"],
                "sales representative": ["sales", "account executive", "business development", "sales rep"],
                "financial analyst": ["financial analyst", "finance", "investment analyst", "financial planning"],
                "operations manager": ["operations manager", "operations", "process manager", "operational"],
                
                # Creative roles
                "content creator": ["content creator", "content writer", "blogger", "content specialist"],
                "graphic designer": ["graphic designer", "designer", "visual designer", "creative designer"],
                "video producer": ["video producer", "filmmaker", "video editor", "videographer"],
                "creative director": ["creative director", "art director", "creative lead"],
                
                # Leadership roles
                "team leader": ["team leader", "team lead", "supervisor", "manager"],
                "director": ["director", "head of", "senior manager"],
                "executive": ["executive", "c-suite", "chief", "ceo", "cto", "cfo", "coo"],
                
                # Other professional roles
                "consultant": ["consultant", "advisor", "specialist"],
                "researcher": ["researcher", "research scientist", "research analyst"],
                "educator": ["teacher", "instructor", "educator", "trainer", "professor"],
                "healthcare professional": ["doctor", "nurse", "therapist", "healthcare", "medical"]
            }
            
            for role, keywords in role_keywords.items():
                for keyword in keywords:
                    if keyword in message_lower and role not in self.target_roles:
                        self.target_roles.append(role)
                        break
        
        # Second question: Energizing activities
        elif question_index == 1:
            # Work activity keywords
            energizing_activity_keywords = {
                "problem solving": ["problem solving", "solve problems", "puzzles", "challenges", "figure out", "troubleshoot"],
                "creative work": ["creative", "design", "create", "innovative", "imagination", "artistic", "new ideas"],
                "analytical tasks": ["analysis", "analyzing", "analytical", "data", "patterns", "research", "investigate"],
                "strategic planning": ["strategy", "planning", "vision", "big picture", "future", "roadmap", "direction"],
                "people management": ["manage", "leading", "supervise", "mentoring", "coaching", "developing people", "team"],
                "collaboration": ["collaborate", "teamwork", "working with others", "cross-functional", "group", "together"],
                "independent work": ["independent", "solo", "on my own", "autonomy", "self-directed", "freedom"],
                "client interaction": ["client", "customer", "user", "stakeholder", "presenting", "consulting"],
                "teaching/mentoring": ["teach", "mentor", "guide", "explain", "instruct", "share knowledge", "training"],
                "writing": ["writing", "documentation", "content", "reports", "communication"],
                "technical work": ["technical", "coding", "programming", "hands-on", "building", "development", "engineering"],
                "project coordination": ["coordination", "organizing", "project management", "planning", "scheduling"]
            }
            
            for activity, keywords in energizing_activity_keywords.items():
                for keyword in keywords:
                    if keyword in message_lower and activity not in self.energizing_activities:
                        self.energizing_activities.append(activity)
                        break
        
        # Third question: Draining activities
        elif question_index == 2:
            # Work activity keywords (same as energizing but for draining context)
            draining_activity_keywords = {
                "problem solving": ["problem solving", "solve problems", "puzzles", "challenges", "figure out", "troubleshoot"],
                "creative work": ["creative", "design", "create", "innovative", "imagination", "artistic", "new ideas"],
                "analytical tasks": ["analysis", "analyzing", "analytical", "data", "patterns", "research", "investigate"],
                "strategic planning": ["strategy", "planning", "vision", "big picture", "future", "roadmap", "direction"],
                "people management": ["manage", "leading", "supervise", "mentoring", "coaching", "developing people", "team"],
                "collaboration": ["collaborate", "teamwork", "working with others", "cross-functional", "group", "together"],
                "independent work": ["independent", "solo", "on my own", "autonomy", "self-directed", "freedom"],
                "client interaction": ["client", "customer", "user", "stakeholder", "presenting", "consulting"],
                "teaching/mentoring": ["teach", "mentor", "guide", "explain", "instruct", "share knowledge", "training"],
                "writing": ["writing", "documentation", "content", "reports", "communication"],
                "technical work": ["technical", "coding", "programming", "hands-on", "building", "development", "engineering"],
                "project coordination": ["coordination", "organizing", "project management", "planning", "scheduling"],
                "administrative tasks": ["administrative", "paperwork", "forms", "bureaucracy", "routine", "repetitive"],
                "meetings": ["meetings", "calls", "status updates", "check-ins"],
                "conflict resolution": ["conflict", "difficult conversations", "disagreements", "tension", "disputes"]
            }
            
            for activity, keywords in draining_activity_keywords.items():
                for keyword in keywords:
                    if keyword in message_lower and activity not in self.draining_activities:
                        self.draining_activities.append(activity)
                        break
        
        # Fourth question: Ideal time allocation
        elif question_index == 3:
            # Try to extract percentages and activities
            # This is a simplified approach, a real implementation would use more sophisticated NLP
            import re
            
            # Define common activities to look for
            activities = [
                "individual work", "solo work", "independent work",
                "collaboration", "teamwork", "working with others", "team",
                "creative tasks", "creative work", "designing", "innovation",
                "analytical tasks", "analysis", "data", "research",
                "meetings", "communication", "discussions",
                "planning", "strategy", "strategic", "thinking",
                "client interaction", "customer", "external",
                "management", "supervising", "leadership",
                "technical work", "coding", "programming", "engineering",
                "writing", "documentation", "content",
                "administrative", "admin", "paperwork"
            ]
            
            # Look for patterns like "X% on Y" or "X percent on Y"
            percentage_patterns = re.findall(r'(\d+)(?:%|\s*percent)\s+(?:on|for|doing|in|with)?\s+([^,.]+)', message_lower)
            
            # Process found patterns
            for percentage, activity_phrase in percentage_patterns:
                # Try to match the activity phrase to our known activities
                matched_activity = None
                for known_activity in activities:
                    if known_activity in activity_phrase:
                        matched_activity = known_activity
                        break
                
                # If no match found, use a general categorization based on key terms
                if not matched_activity:
                    if any(term in activity_phrase for term in ["individual", "solo", "independent", "alone"]):
                        matched_activity = "individual work"
                    elif any(term in activity_phrase for term in ["team", "collab", "others", "group"]):
                        matched_activity = "collaboration"
                    elif any(term in activity_phrase for term in ["creat", "design", "innov", "art"]):
                        matched_activity = "creative tasks"
                    elif any(term in activity_phrase for term in ["analy", "data", "research", "logic"]):
                        matched_activity = "analytical tasks"
                    elif any(term in activity_phrase for term in ["meet", "discuss", "call"]):
                        matched_activity = "meetings"
                    elif any(term in activity_phrase for term in ["plan", "strat", "think", "vision"]):
                        matched_activity = "planning and strategy"
                    elif any(term in activity_phrase for term in ["client", "customer", "user", "external"]):
                        matched_activity = "client interaction"
                    elif any(term in activity_phrase for term in ["manage", "lead", "supervis", "direct"]):
                        matched_activity = "management"
                    elif any(term in activity_phrase for term in ["tech", "code", "program", "engineer"]):
                        matched_activity = "technical work"
                    else:
                        matched_activity = "other activities"
                
                # Store the percentage allocation
                self.ideal_allocation[matched_activity] = int(percentage)
    
    def _get_next_question(self):
        """Get the next question to ask"""
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            return f"**{self.questions[self.current_question_index]}**"
        else:
            return None
    
    def _evaluate_role_fit(self):
        """
        Evaluate the fit between user preferences and common roles
        This is a simplified model - a real implementation would be more sophisticated
        """
        # Role activity profiles (typical percentage of time spent on different activities)
        role_profiles = {
            "software engineer": {
                "technical work": 60,
                "problem solving": 20,
                "collaboration": 10,
                "meetings": 5,
                "planning and strategy": 5
            },
            "data scientist": {
                "analytical tasks": 50,
                "technical work": 20,
                "problem solving": 15,
                "collaboration": 10,
                "communication": 5
            },
            "product manager": {
                "meetings": 30,
                "planning and strategy": 30,
                "collaboration": 20,
                "analytical tasks": 10,
                "communication": 10
            },
            "ux designer": {
                "creative work": 40,
                "analytical tasks": 20,
                "collaboration": 20,
                "client interaction": 10,
                "meetings": 10
            },
            "marketing manager": {
                "planning and strategy": 30,
                "analytical tasks": 20,
                "creative work": 20,
                "collaboration": 15,
                "meetings": 15
            },
            "business analyst": {
                "analytical tasks": 40,
                "meetings": 20,
                "communication": 15,
                "problem solving": 15,
                "collaboration": 10
            },
            "project manager": {
                "project coordination": 40,
                "meetings": 25,
                "collaboration": 15,
                "problem solving": 10,
                "client interaction": 10
            },
            "team leader": {
                "people management": 40,
                "meetings": 20,
                "planning and strategy": 20,
                "problem solving": 10,
                "administrative tasks": 10
            },
            "consultant": {
                "analytical tasks": 30,
                "client interaction": 30,
                "problem solving": 20,
                "communication": 15,
                "meetings": 5
            },
            "content creator": {
                "writing": 50,
                "creative work": 30,
                "research": 10,
                "collaboration": 5,
                "client interaction": 5
            }
        }
        
        # Calculate fit scores for roles the user is interested in
        # If no specific roles mentioned, evaluate all common roles
        roles_to_evaluate = self.target_roles if self.target_roles else list(role_profiles.keys())
        
        for role in roles_to_evaluate:
            # Skip if role profile isn't defined
            if role not in role_profiles:
                continue
            
            # Initialize score components
            activity_alignment = 0
            preference_alignment = 0
            time_allocation_alignment = 0
            
            # Activity alignment - does the role involve energizing activities and avoid draining ones?
            role_activities = set(role_profiles[role].keys())
            
            # Award points for each energizing activity that matches role activities
            for activity in self.energizing_activities:
                # Check for exact match or related activities
                if activity in role_activities:
                    activity_alignment += 20  # Direct match
                elif any(act.split()[0] in activity for act in role_activities):
                    activity_alignment += 10  # Partial match
            
            # Penalize for each draining activity that matches role activities
            for activity in self.draining_activities:
                if activity in role_activities:
                    activity_alignment -= 20
                elif any(act.split()[0] in activity for act in role_activities):
                    activity_alignment -= 10
            
            # Scale activity alignment to 0-100
            min_score = -20 * len(role_activities)  # Worst case: all activities are draining
            max_score = 20 * len(role_activities)   # Best case: all activities are energizing
            activity_alignment = max(0, min(100, 50 + (activity_alignment / max_score) * 50))
            
            # Time allocation alignment - does the role's typical allocation match desired allocation?
            if self.ideal_allocation:
                time_differences = 0
                matching_activities = 0
                
                for activity, percentage in role_profiles[role].items():
                    # Find the closest matching activity in the user's ideal allocation
                    matching_user_activity = None
                    for user_activity in self.ideal_allocation:
                        if activity in user_activity or user_activity in activity:
                            matching_user_activity = user_activity
                            break
                    
                    # If a match was found, calculate the percentage difference
                    if matching_user_activity:
                        user_percentage = self.ideal_allocation[matching_user_activity]
                        time_differences += abs(percentage - user_percentage)
                        matching_activities += 1
                
                # Calculate time allocation alignment score (0-100)
                if matching_activities > 0:
                    # Lower differences = better alignment
                    avg_difference = time_differences / matching_activities
                    time_allocation_alignment = max(0, 100 - avg_difference * 2)  # 2 points per % difference
                else:
                    time_allocation_alignment = 50  # Neutral if no matching activities
            else:
                time_allocation_alignment = 50  # Neutral if no ideal allocation provided
            
            # Calculate overall fit score (weighted average)
            overall_fit = (activity_alignment * 0.6) + (time_allocation_alignment * 0.4)
            
            # Store the fit score
            self.role_fit_scores[role] = {
                "overall": int(overall_fit),
                "activity_alignment": int(activity_alignment),
                "time_allocation_alignment": int(time_allocation_alignment)
            }
    
    def _generate_role_fit_analysis(self):
        """Generate a role fit analysis based on the responses"""
        
        # First evaluate role fit
        self._evaluate_role_fit()
        
        # If no target roles specified, focus on the top-fitting roles
        if not self.target_roles and self.role_fit_scores:
            # Sort roles by fit score
            sorted_roles = sorted(self.role_fit_scores.items(), key=lambda x: x[1]["overall"], reverse=True)
            # Take top 3 as focus roles
            self.target_roles = [role for role, _ in sorted_roles[:3]]
        
        # Generate the analysis
        analysis = f"""
        ## Role Fit Analysis
        
        Based on our conversation, I've analyzed how different roles align with your natural working style, 
        preferences, and strengths to identify where you're likely to thrive with the least friction.
        
        ### Your Work Style Profile
        
        #### Activities That Energize You
        """
        
        if self.energizing_activities:
            for activity in self.energizing_activities[:5]:  # Limit to top 5
                analysis += f"\n- **{activity.capitalize()}**"
        else:
            analysis += "\nYou haven't identified specific energizing activities."
        
        analysis += "\n\n#### Activities That Drain You"
        
        if self.draining_activities:
            for activity in self.draining_activities[:5]:  # Limit to top 5
                analysis += f"\n- **{activity.capitalize()}**"
        else:
            analysis += "\nYou haven't identified specific draining activities."
        
        analysis += "\n\n#### Your Ideal Work Allocation"
        
        if self.ideal_allocation:
            for activity, percentage in sorted(self.ideal_allocation.items(), key=lambda x: x[1], reverse=True):
                analysis += f"\n- **{activity.capitalize()}**: {percentage}%"
        else:
            analysis += "\nYou haven't specified your ideal time allocation across activities."
        
        # Role fit analysis
        analysis += "\n\n### Role Fit Assessment\n"
        
        if self.target_roles and self.role_fit_scores:
            # Sort target roles by fit score
            sorted_roles = sorted(
                [(role, self.role_fit_scores.get(role, {"overall": 0})) 
                 for role in self.target_roles if role in self.role_fit_scores],
                key=lambda x: x[1]["overall"],
                reverse=True
            )
            
            for role, scores in sorted_roles:
                analysis += f"""
                #### {role.capitalize()} - {scores["overall"]}% Overall Fit
                
                **Alignment Analysis:**
                - **Activity Alignment**: {scores["activity_alignment"]}% - How well this role's typical activities match what energizes you
                - **Time Allocation Alignment**: {scores["time_allocation_alignment"]}% - How well this role's typical time distribution matches your preferences
                
                """
                
                # Add strengths and challenges for this role based on scores
                analysis += "**Natural Strengths for This Role:**\n"
                
                # Identify strengths based on energizing activities that match role activities
                role_profiles = {
                    "software engineer": ["technical work", "problem solving", "analytical tasks"],
                    "data scientist": ["analytical tasks", "problem solving", "technical work"],
                    "product manager": ["planning and strategy", "collaboration", "client interaction"],
                    "ux designer": ["creative work", "analytical tasks", "client interaction"],
                    "marketing manager": ["creative work", "planning and strategy", "analytical tasks"],
                    "business analyst": ["analytical tasks", "problem solving", "strategic planning"],
                    "project manager": ["project coordination", "collaboration", "planning and strategy"],
                    "team leader": ["people management", "collaboration", "planning and strategy"],
                    "consultant": ["analytical tasks", "problem solving", "client interaction"],
                    "content creator": ["creative work", "writing", "independent work"]
                }
                
                # Get typical activities for this role
                role_activities = role_profiles.get(role, [])
                
                # Find overlaps with energizing activities
                strengths = []
                for activity in self.energizing_activities:
                    if activity in role_activities or any(ra in activity for ra in role_activities):
                        strengths.append(activity)
                
                if strengths:
                    for strength in strengths[:3]:  # Limit to top 3
                        analysis += f"- Your energy for **{strength}** aligns well with this role's requirements\n"
                else:
                    analysis += "- No specific strengths identified based on your responses\n"
                
                analysis += "\n**Potential Challenges:**\n"
                
                # Identify challenges based on draining activities that match role activities
                challenges = []
                for activity in self.draining_activities:
                    if activity in role_activities or any(ra in activity for ra in role_activities):
                        challenges.append(activity)
                
                if challenges:
                    for challenge in challenges[:3]:  # Limit to top 3
                        analysis += f"- Your aversion to **{challenge}** may create friction in this role\n"
                else:
                    analysis += "- No specific challenges identified based on your responses\n"
        else:
            analysis += "\nInsufficient information to generate specific role fit assessments."
        
        # Role optimization strategies
        analysis += """
        
        ### Role Optimization Strategies
        
        Here are approaches to enhance your fit and satisfaction in your target roles:
        """
        
        if self.target_roles:
            # Provide strategies for the top target role
            top_role = self.target_roles[0] if self.target_roles else "your target role"
            
            analysis += f"""
            #### Crafting Your Ideal Version of {top_role.capitalize()}
            
            **Job Crafting Strategies:**
            
            1. **Task Emphasis:** Negotiate to increase time on activities that energize you:
               - Identify specific energizing tasks that add value to the organization
               - Demonstrate how increasing your focus in these areas benefits outcomes
               - Propose gradual shifts in responsibility that align with organizational needs
            
            2. **Role Partnership:** Develop complementary relationships with colleagues:
               - Find team members who enjoy tasks you find draining
               - Create mutually beneficial task exchanges where both parties focus on strengths
               - Formalize these arrangements through team workflow discussions
            
            3. **Development Focus:** Enhance skills that make energizing activities more valuable:
               - Identify specialized capabilities that justify more time on preferred tasks
               - Develop unique expertise that makes you the natural choice for these activities
               - Connect your preferred work style to measurable business outcomes
            
            4. **Boundary Management:** Create protective structures for focus and recovery:
               - Establish clear boundaries around draining activities (time blocks, limits)
               - Build in recovery periods after necessarily draining tasks
               - Use productivity systems that optimize your energy management
            """
        
        # General strategies for improving role fit
        analysis += """
        
        #### Universal Role Fit Enhancement
        
        Regardless of your specific role, these strategies can improve alignment:
        
        1. **Energy Tracking:** Monitor which specific tasks and contexts give or drain energy
           - Keep a simple energy log for 1-2 weeks
           - Look for patterns related to task type, collaboration context, and timing
           - Use insights to restructure your day around energy patterns
        
        2. **Micro-Negotiation:** Have ongoing conversations about role evolution
           - Focus on small, incremental shifts rather than major role changes
           - Frame discussions around enhanced contribution, not just personal preference
           - Look for win-win opportunities that benefit both you and the organization
        
        3. **Complementary Skill Building:** Develop techniques to manage draining activities
           - Learn specific methods to make necessary but draining tasks more efficient
           - Create templates, systems and routines for recurring draining activities
           - Consider whether certain draining tasks could be automated or delegated
        
        4. **Strategic Positioning:** Align role evolution with organizational priorities
           - Connect your natural strengths to emerging organizational needs
           - Demonstrate the ROI of allocating your time to energy-giving activities
           - Build a narrative about your distinctive contribution that aligns with your preferences
        
        Remember that perfect role fit is rarely achieved through finding an ideal pre-existing role. Instead, it typically emerges through a process of ongoing alignment and adaptation between you and your organization as you establish your unique value proposition.
        """
        
        return analysis
    
    def _get_results(self):
        """Get the results of the analysis for other agents to use"""
        
        # Format target roles
        roles = [role.capitalize() for role in self.target_roles]
        
        # Format activities
        energizing = [activity.capitalize() for activity in self.energizing_activities]
        draining = [activity.capitalize() for activity in self.draining_activities]
        
        # Format role fit scores
        fit_scores = {}
        for role, score in self.role_fit_scores.items():
            fit_scores[role.capitalize()] = score
        
        # Compile results
        results = {
            "target_roles": roles,
            "energizing_activities": energizing,
            "draining_activities": draining,
            "ideal_allocation": self.ideal_allocation,
            "role_fit_scores": fit_scores
        }
        
        return results