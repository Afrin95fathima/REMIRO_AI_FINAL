import streamlit as st

class NetworkAgent:
    """
    Network Agent - Connection Architect
    Develops strategic networking plans and relationship cultivation strategies
    """
    
    def __init__(self):
        self.name = "Connection Architect"
        self.description = "Strategic networking and relationship development advisor"
        self.questions = [
            "How would you describe your current professional network? (Size, diversity, strength of connections, etc.)",
            "What challenges or hesitations do you experience when it comes to networking or building professional relationships?",
            "Are there specific types of people or organizations you'd like to connect with to advance your career goals?",
            "How do you typically maintain professional relationships over time?"
        ]
        self.current_question_index = 0
        self.responses = []
        self.network_status = None  # "strong", "moderate", "limited"
        self.networking_challenges = []
        self.target_connections = []
        self.relationship_maintenance = []
        self.networking_style = None  # "proactive", "responsive", "selective"
        self.analysis_complete = False
    
    def get_introduction(self):
        """Get the introduction message for this agent"""
        return f"""
        ## Network & Relationships Assessment
        
        I'm your **{self.name}**, {self.description}. I'll help you develop strategic approaches 
        to building and leveraging professional relationships that can accelerate your career growth.
        
        Understanding your current network, networking style, and relationship goals will help 
        create a personalized plan for expanding your professional connections in meaningful ways.
        
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
            final_analysis = self._generate_network_analysis()
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
        
        # First question: Current network assessment
        if question_index == 0:
            # Analyze network strength
            strong_keywords = ["strong", "extensive", "large", "robust", "well-developed", "diverse", 
                             "well-connected", "established", "many connections", "good network"]
            
            moderate_keywords = ["moderate", "decent", "growing", "developing", "building", 
                              "mixed", "some connections", "okay", "fair", "average"]
            
            limited_keywords = ["limited", "small", "minimal", "beginning", "few", "sparse", 
                             "starting", "need to expand", "not extensive", "weak", "poor"]
            
            # Count the occurrences of each category
            strong_count = sum(1 for keyword in strong_keywords if keyword in message_lower)
            moderate_count = sum(1 for keyword in moderate_keywords if keyword in message_lower)
            limited_count = sum(1 for keyword in limited_keywords if keyword in message_lower)
            
            # Determine network status based on keyword frequency
            if strong_count > moderate_count and strong_count > limited_count:
                self.network_status = "strong"
            elif limited_count > strong_count and limited_count > moderate_count:
                self.network_status = "limited"
            else:
                self.network_status = "moderate"
            
            # Analyze networking style
            proactive_keywords = ["reach out", "initiate", "connect", "introduce myself", "approach", "active",
                               "regularly", "consistently", "organized", "strategic", "intentional"]
            
            responsive_keywords = ["respond", "when invited", "if asked", "when necessary", "occasionally",
                               "sometimes", "if needed", "when opportunities arise"]
            
            selective_keywords = ["selective", "careful", "quality over quantity", "meaningful", "specific",
                               "targeted", "deliberate", "intentional"]
            
            # Count the occurrences of each style
            proactive_count = sum(1 for keyword in proactive_keywords if keyword in message_lower)
            responsive_count = sum(1 for keyword in responsive_keywords if keyword in message_lower)
            selective_count = sum(1 for keyword in selective_keywords if keyword in message_lower)
            
            # Determine networking style based on keyword frequency
            if proactive_count > responsive_count and proactive_count > selective_count:
                self.networking_style = "proactive"
            elif responsive_count > proactive_count and responsive_count > selective_count:
                self.networking_style = "responsive"
            elif selective_count > proactive_count and selective_count > responsive_count:
                self.networking_style = "selective"
            else:
                # Default if no clear pattern
                self.networking_style = "balanced"
        
        # Second question: Networking challenges
        elif question_index == 1:
            # Common networking challenge keywords
            challenge_keywords = {
                "confidence issues": ["shy", "intimidated", "awkward", "nervous", "uncomfortable", "anxiety", "confidence", "insecure"],
                "conversation starters": ["small talk", "conversation", "what to say", "topics", "questions", "starting", "breaking the ice"],
                "authenticity concerns": ["authentic", "genuine", "fake", "pretend", "natural", "forced", "myself", "real"],
                "time constraints": ["time", "busy", "schedule", "finding time", "workload", "balance", "bandwidth"],
                "follow-up difficulties": ["follow up", "follow-up", "following up", "next steps", "maintaining", "consistent"],
                "value proposition clarity": ["value", "offer", "contribute", "benefit", "worth", "imposing", "bothering"],
                "strategic focus": ["strategic", "targeted", "purpose", "goal", "direction", "focus", "plan", "random"],
                "online networking": ["online", "virtual", "digital", "social media", "linkedin", "remote", "platform"],
                "formal event discomfort": ["events", "conferences", "formal", "large groups", "crowds", "networking events"],
                "reciprocity concerns": ["give", "take", "reciprocate", "mutual", "one-sided", "transactional", "genuine"]
            }
            
            for challenge, keywords in challenge_keywords.items():
                for keyword in keywords:
                    if keyword in message_lower and challenge not in self.networking_challenges:
                        self.networking_challenges.append(challenge)
                        break
        
        # Third question: Target connections
        elif question_index == 2:
            # Common target connection types
            target_keywords = {
                "industry leaders": ["leaders", "executives", "experts", "authorities", "influencers", "thought leaders"],
                "peers & colleagues": ["peers", "colleagues", "similar role", "same field", "counterparts"],
                "mentors": ["mentors", "advisors", "guides", "experienced", "senior"],
                "cross-functional contacts": ["cross-functional", "other departments", "different teams", "diverse roles"],
                "hiring managers": ["hiring managers", "recruiters", "talent acquisition", "hr professionals"],
                "potential clients": ["clients", "customers", "prospects", "business opportunities"],
                "subject matter experts": ["experts", "specialists", "technical", "specialized knowledge"],
                "entrepreneurs": ["entrepreneurs", "founders", "startup", "business owners", "ceos"],
                "community leaders": ["community", "nonprofit", "social impact", "public service"],
                "international contacts": ["global", "international", "overseas", "different countries", "abroad"]
            }
            
            for target, keywords in target_keywords.items():
                for keyword in keywords:
                    if keyword in message_lower and target not in self.target_connections:
                        self.target_connections.append(target)
                        break
        
        # Fourth question: Relationship maintenance
        elif question_index == 3:
            # Common relationship maintenance strategies
            maintenance_keywords = {
                "regular check-ins": ["check in", "regular", "periodic", "consistent", "touch base", "stay in touch"],
                "social media engagement": ["social media", "online", "linkedin", "twitter", "platform", "posts", "like", "comment"],
                "value sharing": ["share", "articles", "resources", "opportunities", "information", "value", "helpful"],
                "event attendance": ["events", "conferences", "meetups", "gatherings", "industry events", "professional groups"],
                "personal connection": ["personal", "genuine", "authentic", "real", "beyond work", "meaningful"],
                "collaborative projects": ["collaborate", "projects", "work together", "joint", "cooperation"],
                "mentoring/support": ["mentor", "support", "help", "guidance", "advice", "contribute"],
                "celebration & recognition": ["celebrate", "congratulate", "recognition", "achievements", "milestones", "success"],
                "organized system": ["system", "crm", "organize", "track", "schedule", "reminder", "database"],
                "community building": ["community", "group", "bringing people together", "introductions", "connecting others"]
            }
            
            for strategy, keywords in maintenance_keywords.items():
                for keyword in keywords:
                    if keyword in message_lower and strategy not in self.relationship_maintenance:
                        self.relationship_maintenance.append(strategy)
                        break
    
    def _get_next_question(self):
        """Get the next question to ask"""
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            return f"**{self.questions[self.current_question_index]}**"
        else:
            return None
    
    def _generate_network_analysis(self):
        """Generate a network analysis based on the responses"""
        
        # Ensure we have some basic data
        if not self.network_status:
            self.network_status = "moderate"
        
        if not self.networking_style:
            self.networking_style = "balanced"
        
        if not self.networking_challenges:
            self.networking_challenges = ["strategic focus", "time constraints"]
        
        if not self.target_connections:
            self.target_connections = ["industry leaders", "peers & colleagues"]
        
        if not self.relationship_maintenance:
            self.relationship_maintenance = ["regular check-ins", "value sharing"]
        
        # Generate the analysis
        analysis = f"""
        ## Network & Relationship Strategy
        
        Based on our conversation, I've analyzed your networking approach and relationships to create 
        a personalized strategy for building professional connections that advance your career goals.
        
        ### Your Networking Profile
        
        #### Current Network Status
        You appear to have a **{self.network_status} professional network** right now. """
        
        # Add details based on network status
        if self.network_status == "strong":
            analysis += "This suggests you've already established valuable connections across your field and potentially beyond."
        elif self.network_status == "moderate":
            analysis += "This suggests you have some established connections but opportunity for strategic expansion."
        else:  # limited
            analysis += "This suggests you're early in your network-building journey with significant room for growth."
        
        # Add networking style analysis
        analysis += f"\n\n#### Networking Style\nYour approach to networking appears to be primarily **{self.networking_style}**. "
        
        if self.networking_style == "proactive":
            analysis += "You tend to initiate connections and actively work to expand your network."
        elif self.networking_style == "responsive":
            analysis += "You typically engage when opportunities present themselves rather than creating them."
        elif self.networking_style == "selective":
            analysis += "You focus on quality connections over quantity, being intentional about who you connect with."
        else:  # balanced
            analysis += "You show a flexible approach, adapting your networking style to different situations."
        
        # Networking challenges
        analysis += "\n\n#### Networking Challenges\n"
        
        if self.networking_challenges:
            analysis += "You've identified these challenges in your networking efforts:"
            for challenge in self.networking_challenges:
                analysis += f"\n- **{challenge.capitalize()}**"
        else:
            analysis += "You haven't identified specific networking challenges."
        
        # Target connections
        analysis += "\n\n#### Desired Connections\n"
        
        if self.target_connections:
            analysis += "You're interested in connecting with:"
            for connection in self.target_connections:
                analysis += f"\n- **{connection.capitalize()}**"
        else:
            analysis += "You haven't specified particular types of connections you're seeking."
        
        # Relationship maintenance
        analysis += "\n\n#### Relationship Maintenance Approach\n"
        
        if self.relationship_maintenance:
            analysis += "Your current relationship maintenance strategies include:"
            for strategy in self.relationship_maintenance:
                analysis += f"\n- **{strategy.capitalize()}**"
        else:
            analysis += "You haven't mentioned specific strategies for maintaining relationships."
        
        # Personalized networking strategy
        analysis += """
        
        ### Strategic Networking Plan
        
        Based on your profile, here's a personalized approach to expanding and leveraging your professional network:
        """
        
        # Network expansion strategy based on current status
        analysis += "\n#### Network Development Strategy\n"
        
        if self.network_status == "strong":
            analysis += """
            **Refinement Strategy for Strong Network:**
            
            Your established network puts you in an excellent position to focus on quality and strategic connections:
            
            1. **Network Audit**: Evaluate your current connections to identify potential gaps in key areas
            
            2. **Relationship Deepening**: Focus on strengthening valuable existing relationships rather than just adding new contacts
            
            3. **Strategic Introductions**: Leverage your connections to facilitate targeted introductions to specific high-value contacts
            
            4. **Thought Leadership**: Position yourself as a connector and resource within your network
            
            5. **Reciprocity Focus**: Look for meaningful ways to provide value to your existing network
            """
        elif self.network_status == "moderate":
            analysis += """
            **Enhancement Strategy for Moderate Network:**
            
            Your foundation gives you a solid base to build upon with a balanced approach:
            
            1. **Strategic Expansion**: Target specific connection types that align with your career goals
            
            2. **Visibility Increase**: Participate more actively in relevant professional communities
            
            3. **Relationship Formalization**: Convert informal connections into more structured professional relationships
            
            4. **Networking Rhythm**: Establish regular practices for connection outreach and follow-up
            
            5. **Value Exchange Clarity**: Develop clear understanding of the mutual benefits in your key relationships
            """
        else:  # limited
            analysis += """
            **Growth Strategy for Limited Network:**
            
            Focus on establishing a strong foundation with a targeted approach:
            
            1. **Foundation Building**: Start with connections in your immediate professional circle
            
            2. **Low-Pressure Contexts**: Utilize structured events and platforms that facilitate easier introductions
            
            3. **Skill Development**: Practice networking in supportive environments to build confidence
            
            4. **Clear Narratives**: Develop concise, compelling ways to introduce yourself and your goals
            
            5. **Progressive Expansion**: Begin with closer connections and gradually extend to wider networks
            """
        
        # Addressing specific challenges
        analysis += "\n#### Overcoming Your Networking Challenges\n"
        
        for challenge in self.networking_challenges[:3]:  # Limit to top 3 challenges
            if challenge == "confidence issues":
                analysis += """
                **For Confidence Challenges:**
                - Prepare concise personal introductions for different contexts
                - Start with smaller, more intimate networking settings
                - Focus on being curious about others rather than impressing them
                - Practice specific conversation openers and questions
                - Celebrate small networking victories to build momentum
                """
            elif challenge == "conversation starters":
                analysis += """
                **For Conversation Initiation:**
                - Prepare 3-5 versatile, open-ended questions that work in most professional settings
                - Research event attendees or specific people before meetings
                - Use shared contexts as natural conversation openings
                - Practice the "comment, question, reveal" conversation pattern
                - Focus on quality listening to generate natural follow-ups
                """
            elif challenge == "time constraints":
                analysis += """
                **For Time Management in Networking:**
                - Schedule specific "networking blocks" in your calendar
                - Prioritize connections using a tiered approach
                - Leverage asynchronous networking through targeted online engagement
                - Combine networking with other activities (e.g., professional development)
                - Use technology to streamline follow-ups and relationship management
                """
            elif challenge == "follow-up difficulties":
                analysis += """
                **For Follow-Up Consistency:**
                - Create templates for different types of follow-up communications
                - Implement a simple system to track connection points and follow-ups
                - Schedule immediate post-meeting time to send follow-ups
                - Use calendar reminders for periodic check-ins
                - Develop a personalized cadence for different relationship types
                """
            elif challenge == "strategic focus":
                analysis += """
                **For Strategic Networking:**
                - Define specific networking goals tied to career objectives
                - Create a "relationship map" of target connections
                - Develop criteria for evaluating networking opportunities
                - Analyze your current network for gaps and redundancies
                - Plan targeted approaches for high-value potential connections
                """
            elif challenge == "value proposition clarity":
                analysis += """
                **For Value Proposition Clarity:**
                - Identify your unique skills, knowledge, and resources
                - Prepare specific examples of how you've helped others professionally
                - Practice articulating your expertise concisely
                - Ask trusted colleagues about your perceived professional strengths
                - Develop different value framings for different audience types
                """
        
        # Connection strategies for target groups
        analysis += "\n#### Connection Strategies for Your Target Groups\n"
        
        for target in self.target_connections[:3]:  # Limit to top 3 targets
            if target == "industry leaders":
                analysis += """
                **Connecting with Industry Leaders:**
                - Engage thoughtfully with their content (articles, posts, talks)
                - Offer specific, informed insights rather than generic comments
                - Attend smaller events where they're speaking or participating
                - Consider offering assistance on projects or initiatives they're leading
                - Build relationships with their team members or close associates first
                """
            elif target == "peers & colleagues":
                analysis += """
                **Building Peer Relationships:**
                - Join professional communities and special interest groups
                - Initiate knowledge-sharing sessions or informal meetups
                - Collaborate on projects or problem-solving initiatives
                - Create or participate in peer mentoring circles
                - Share relevant opportunities and resources consistently
                """
            elif target == "mentors":
                analysis += """
                **Developing Mentor Relationships:**
                - Research potential mentors thoroughly before reaching out
                - Make specific, reasonable requests rather than open-ended ones
                - Demonstrate how you've already applied advice or insights they've shared publicly
                - Be explicit about what you admire about their work or career
                - Follow up with outcomes and appreciation when they provide guidance
                """
            elif target == "hiring managers":
                analysis += """
                **Connecting with Hiring Managers:**
                - Focus on relationship-building before you need a job
                - Engage in industry discussions where they participate
                - Request informational interviews about their field or company
                - Demonstrate knowledge of their organization's challenges and opportunities
                - Position yourself as a resource, not just a potential candidate
                """
            elif target == "cross-functional contacts":
                analysis += """
                **Building Cross-Functional Relationships:**
                - Volunteer for cross-departmental projects and task forces
                - Attend learning sessions about other functional areas
                - Invite cross-functional peers for informal knowledge exchange
                - Express genuine curiosity about their work challenges and perspectives
                - Look for opportunities to collaborate on shared organizational goals
                """
        
        # Relationship maintenance enhancement
        analysis += "\n#### Relationship Nurturing Strategy\n"
        
        existing_strategies = set(self.relationship_maintenance)
        recommended_strategies = []
        
        # Add complementary strategies to what they're already doing
        if "regular check-ins" not in existing_strategies:
            recommended_strategies.append("regular check-ins")
        
        if "value sharing" not in existing_strategies:
            recommended_strategies.append("value sharing")
        
        if "personal connection" not in existing_strategies:
            recommended_strategies.append("personal connection")
        
        if "organized system" not in existing_strategies:
            recommended_strategies.append("organized system")
        
        analysis += """
        Build on your current approaches with these relationship maintenance strategies:
        """
        
        for strategy in recommended_strategies[:3]:  # Limit to top 3 new strategies
            if strategy == "regular check-ins":
                analysis += """
                - **Structured Check-In System:** Develop a tiered system for relationship maintenance:
                  * Tier 1 (Key relationships): Every 4-8 weeks
                  * Tier 2 (Important connections): Quarterly
                  * Tier 3 (General network): Every 6 months
                """
            elif strategy == "value sharing":
                analysis += """
                - **Value-First Approach:** Consistently share relevant resources, opportunities, and insights:
                  * Personalize shared content to specific interests
                  * Frame shares with context on why you thought of them
                  * Follow up to see if the shared resource was useful
                """
            elif strategy == "personal connection":
                analysis += """
                - **Authentic Connection Development:** Move beyond purely transactional interactions:
                  * Note personal interests and important life events
                  * Reference previous conversations to show attentiveness
                  * Share appropriate personal context to deepen relationships
                """
            elif strategy == "organized system":
                analysis += """
                - **Relationship Management System:** Implement a simple tracking approach:
                  * Document key information about contacts (interests, history, goals)
                  * Set reminders for follow-ups and check-ins
                  * Track conversation topics and action items
                """
        
        # Networking platform strategy
        analysis += """
        
        ### Digital & In-Person Networking Integration
        
        Maximize your networking effectiveness with this integrated approach:
        """
        
        # Tailor platform recommendations based on their style and status
        if self.networking_style == "proactive":
            analysis += """
            
            **Digital Presence Strategy (Proactive Approach):**
            - **Content Creation:** Develop a consistent rhythm of original content sharing
            - **Community Leadership:** Initiate and moderate professional discussions
            - **Connection Campaigns:** Plan periodic focused connection expansion efforts
            - **Event Organization:** Host virtual roundtables or discussions in your area of expertise
            
            **In-Person Strategy (Proactive Approach):**
            - **Speaking Opportunities:** Seek panel or presentation slots at relevant events
            - **Strategic Event Selection:** Choose events where you can take visible roles
            - **Hosting Initiatives:** Organize small gatherings for targeted professional groups
            - **Active Introduction:** Set specific goals for new connections at each event
            """
        elif self.networking_style == "responsive":
            analysis += """
            
            **Digital Presence Strategy (Responsive Approach):**
            - **Engagement Focus:** Develop a sustainable rhythm for commenting and responding
            - **Selective Visibility:** Participate more actively in fewer, high-value communities
            - **Response Preparation:** Create frameworks for different types of online engagement
            - **Notification Optimization:** Ensure you're alerted to relevant connection opportunities
            
            **In-Person Strategy (Responsive Approach):**
            - **Structured Events:** Favor formats with built-in interaction opportunities
            - **Preparation Emphasis:** Research attendees and prepare specific talking points
            - **Arrival Timing:** Come early to events when energy is high and groups aren't formed
            - **Question Preparation:** Develop thoughtful questions for speakers or group discussions
            """
        else:  # selective or balanced
            analysis += """
            
            **Digital Presence Strategy (Selective Approach):**
            - **Quality Engagement:** Focus on substantive interaction over frequent activity
            - **Targeted Visibility:** Become known in specific communities aligned with goals
            - **Thought Leadership:** Share deeper insights in your areas of expertise
            - **Relationship Depth:** Develop more meaningful online exchanges with fewer people
            
            **In-Person Strategy (Selective Approach):**
            - **Research-Driven Selection:** Choose events based on specific attendees or outcomes
            - **Pre-Scheduled Meetings:** Arrange one-on-one conversations during larger events
            - **Depth Over Breadth:** Aim for fewer but more meaningful conversations
            - **Strategic Positioning:** Seek roles that naturally facilitate quality interactions
            """
        
        # Final networking success principles
        analysis += """
        
        ### Core Networking Principles
        
        Regardless of specific tactics, remember these fundamental principles:
        
        1. **Authentic Connection:** Focus on genuine relationships rather than transactional interactions
        
        2. **Value Creation:** Approach networking with a "give first" mentality
        
        3. **Consistent Presence:** Show up regularly in your professional communities
        
        4. **Thoughtful Curation:** Be intentional about which relationships to deepen
        
        5. **Long-Term Perspective:** Build relationships before you need them
        
        Remember that effective networking is about building a web of mutually beneficial relationships that create value for all involved. The strongest networks develop gradually through consistent, authentic engagement rather than through forced or purely strategic interactions.
        """
        
        return analysis
    
    def _get_results(self):
        """Get the results of the analysis for other agents to use"""
        
        # Format challenges
        challenges = [challenge.capitalize() for challenge in self.networking_challenges]
        
        # Format targets
        targets = [target.capitalize() for target in self.target_connections]
        
        # Format maintenance strategies
        maintenance = [strategy.capitalize() for strategy in self.relationship_maintenance]
        
        # Compile results
        results = {
            "network_status": self.network_status.capitalize() if self.network_status else "Moderate",
            "networking_style": self.networking_style.capitalize() if self.networking_style else "Balanced",
            "networking_challenges": challenges,
            "target_connections": targets,
            "relationship_maintenance": maintenance
        }
        
        return results