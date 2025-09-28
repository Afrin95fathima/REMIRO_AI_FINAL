import streamlit as st

class CareerRoadmapAgent:
    """
    Career Path & Roadmap Generator Agent
    Synthesizes insights from all agents to create personalized career roadmaps
    """
    
    def __init__(self):
        self.name = "Career Path & Roadmap Generator"
        self.description = "Synthesizes all insights to create your personalized career path and development roadmap"
    
    def generate_roadmap(self, analysis_results):
        """Generate a comprehensive career roadmap based on all agent results"""
        
        # Extract key insights from each agent's results
        # In a real implementation, this would involve more sophisticated data processing
        
        # Default values in case certain agent results are missing
        personality_insights = analysis_results.get("personality", {})
        interests_insights = analysis_results.get("interests", {})
        skills_insights = analysis_results.get("skills", {})
        aspirations_insights = analysis_results.get("aspirations", {})
        
        # Extract work preferences from personality results
        work_preferences = personality_insights.get("work_preferences", {
            "social_style": "balanced",
            "structure_style": "moderately structured",
            "innovation_style": "balanced innovation"
        })
        
        # Extract top interests and related fields
        top_interests = interests_insights.get("top_interests", ["investigative", "artistic", "social"])
        related_fields = interests_insights.get("related_fields", [
            "research", "technology", "design", "education", "healthcare"
        ])
        
        # Extract skills information (if available)
        current_skills = skills_insights.get("current_skills", ["communication", "analysis", "problem solving"])
        skill_gaps = skills_insights.get("skill_gaps", ["leadership", "technical expertise"])
        
        # Extract career aspirations (if available)
        career_vision = aspirations_insights.get("career_vision", "A fulfilling career that leverages your strengths")
        short_term_goals = aspirations_insights.get("short_term_goals", ["Skill development", "Career exploration"])
        long_term_goals = aspirations_insights.get("long_term_goals", ["Career advancement", "Work-life balance"])
        
        # Generate suitable career roles based on all insights
        suitable_roles = self._generate_suitable_roles(
            work_preferences, 
            top_interests, 
            related_fields,
            current_skills
        )
        
        # Generate career path with short and long-term perspectives
        career_path = self._generate_career_path(
            suitable_roles,
            short_term_goals,
            long_term_goals
        )
        
        # Generate development roadmap with concrete steps
        development_roadmap = self._generate_development_roadmap(
            suitable_roles[0] if suitable_roles else "your preferred career path",
            current_skills,
            skill_gaps
        )
        
        # Combine everything into a comprehensive roadmap
        roadmap = f"""
        # Your Personalized Career Roadmap
        
        ## Recommended Career Roles
        
        Based on our comprehensive analysis, these career paths align well with your personality, 
        interests, skills, and aspirations:
        
        {self._format_career_roles(suitable_roles)}
        
        ## Your Career Path
        
        {career_path}
        
        ## Development Roadmap
        
        {development_roadmap}
        
        ## Next Steps
        
        1. **Explore in Depth**: Research the recommended roles to understand day-to-day responsibilities, required qualifications, and growth potential.
        
        2. **Connect with Professionals**: Reach out to people in these fields for informational interviews to gain insider perspectives.
        
        3. **Skill Development Plan**: Begin acquiring the key skills identified in your development roadmap through courses, projects, or volunteer work.
        
        4. **Experimentation**: Look for low-risk ways to try aspects of these roles, such as small projects, shadowing, or workshops.
        
        5. **Reflect and Refine**: Periodically revisit this roadmap and refine it based on new experiences and evolving preferences.
        
        Remember that career development is rarely linear. This roadmap provides direction, but remain open to unexpected opportunities and detours along the way!
        """
        
        return roadmap
    
    def _generate_suitable_roles(self, work_preferences, top_interests, related_fields, current_skills):
        """Generate suitable career roles based on insights"""
        
        # This would ideally use a sophisticated matching algorithm
        # For now, we'll use a simplified approach with predefined mappings
        
        # Map interests to role categories
        interest_role_mapping = {
            "realistic": ["engineer", "technician", "trades professional", "environmental specialist"],
            "investigative": ["researcher", "analyst", "scientist", "technology specialist"],
            "artistic": ["designer", "creator", "writer", "developer"],
            "social": ["educator", "counselor", "healthcare provider", "hr professional"],
            "enterprising": ["manager", "entrepreneur", "consultant", "sales professional"],
            "conventional": ["organizer", "administrator", "coordinator", "specialist"]
        }
        
        # Get potential role categories based on top interests
        potential_roles = []
        for interest in top_interests[:2]:  # Use top two interests
            if interest in interest_role_mapping:
                potential_roles.extend(interest_role_mapping[interest])
        
        # Refine roles based on work preferences
        refined_roles = []
        
        # Social style preference
        if work_preferences.get("social_style") == "collaborative":
            refined_roles.extend([role for role in potential_roles if role in 
                                ["manager", "educator", "counselor", "consultant"]])
        elif work_preferences.get("social_style") == "independent":
            refined_roles.extend([role for role in potential_roles if role in 
                                ["researcher", "analyst", "writer", "developer"]])
        
        # Structure style preference
        if work_preferences.get("structure_style") == "structured":
            refined_roles.extend([role for role in potential_roles if role in 
                                ["engineer", "administrator", "coordinator", "specialist"]])
        elif work_preferences.get("structure_style") == "flexible":
            refined_roles.extend([role for role in potential_roles if role in 
                                ["entrepreneur", "creator", "consultant", "designer"]])
        
        # Combine with related fields to create specific roles
        specific_roles = []
        for field in related_fields[:5]:  # Use top 5 fields
            for role in (refined_roles or potential_roles)[:3]:  # Use refined roles if available, otherwise potential roles
                specific_roles.append(f"{field} {role}")
        
        # Ensure we have enough roles
        if len(specific_roles) < 3:
            # Add some generic roles based on top interests
            for interest in top_interests:
                if interest == "investigative":
                    specific_roles.append("Data Analyst")
                    specific_roles.append("Research Specialist")
                elif interest == "artistic":
                    specific_roles.append("UX Designer")
                    specific_roles.append("Content Creator")
                elif interest == "social":
                    specific_roles.append("Community Manager")
                    specific_roles.append("Training Specialist")
                elif interest == "enterprising":
                    specific_roles.append("Project Manager")
                    specific_roles.append("Business Development Representative")
                elif interest == "conventional":
                    specific_roles.append("Operations Coordinator")
                    specific_roles.append("Systems Administrator")
                elif interest == "realistic":
                    specific_roles.append("Technical Specialist")
                    specific_roles.append("Field Coordinator")
        
        # Remove duplicates and capitalize properly
        specific_roles = list(set(specific_roles))
        specific_roles = [role.title() for role in specific_roles]
        
        # Return top 5 roles
        return specific_roles[:5]
    
    def _format_career_roles(self, roles):
        """Format career roles into a nice bulleted list with descriptions"""
        if not roles:
            return "No specific roles could be identified based on the available information."
        
        formatted_roles = ""
        
        # Simple descriptions for common role types
        role_descriptions = {
            "analyst": "leveraging analytical skills to derive insights from information",
            "researcher": "conducting in-depth investigation to expand knowledge or solve problems",
            "designer": "creating solutions with attention to both function and form",
            "developer": "building and implementing systems or applications",
            "manager": "coordinating people and resources to achieve objectives",
            "specialist": "applying focused expertise in a specific domain",
            "coordinator": "organizing multiple elements to ensure smooth operations",
            "consultant": "providing expert advice to help others improve or solve problems"
        }
        
        for role in roles:
            formatted_roles += f"### {role}\n\n"
            
            # Try to generate a description based on keywords in the role
            role_lower = role.lower()
            description = "This role involves "
            
            # Check for common role types in the description
            described = False
            for role_type, desc in role_descriptions.items():
                if role_type in role_lower:
                    description += desc + " "
                    described = True
            
            # If no common role type found, give a generic description
            if not described:
                description += "applying your skills and interests in a specialized capacity "
            
            # Add context about the field
            for field in ["technology", "healthcare", "education", "business", "science", "arts", "engineering"]:
                if field in role_lower:
                    description += f"within the {field} sector. "
                    break
            else:
                description += "within your field of interest. "
            
            # Add a generic benefit
            description += "This path allows you to leverage your natural strengths while pursuing meaningful work aligned with your values.\n\n"
            
            formatted_roles += description
        
        return formatted_roles
    
    def _generate_career_path(self, suitable_roles, short_term_goals, long_term_goals):
        """Generate a career path with short and long-term perspectives"""
        
        if not suitable_roles:
            return "Based on the available information, a specific career path couldn't be generated."
        
        # Select primary role from suitable roles
        primary_role = suitable_roles[0]
        
        career_path = f"""
        ### Short-Term (1-3 Years)
        
        Focus on building foundational skills and experiences that position you for success as a {primary_role} or in related roles:
        
        1. **Skill Development**: Acquire core competencies through targeted courses, certifications, or projects.
           * Technical skills specific to {primary_role}
           * Relevant soft skills like {", ".join(["communication", "collaboration", "problem-solving"][:2])}
        
        2. **Experience Building**: 
           * Seek entry-level positions, internships, or volunteer opportunities in related areas
           * Develop small personal or professional projects that showcase relevant skills
           * Join relevant professional organizations or online communities
        
        3. **Network Development**:
           * Connect with professionals in your target field
           * Attend industry events or webinars
           * Participate in relevant online discussions or forums
        
        ### Long-Term (5-10+ Years)
        
        As you gain experience and refine your interests, your career path could evolve in several directions:
        
        1. **Specialization Path**: Become a recognized expert in a specific niche within your field
           * Advanced certifications and possibly graduate education
           * Thought leadership through speaking, writing, or research
           * Senior specialist or technical leadership roles
        
        2. **Management Path**: Leverage your expertise to lead teams and larger initiatives
           * Development of leadership and strategic planning skills
           * Progression from team lead to department or organizational leadership
           * Broader business acumen development
        
        3. **Entrepreneurial Path**: Apply your expertise to create new ventures or consulting opportunities
           * Development of business and entrepreneurial skills
           * Building a personal brand and professional network
           * Creating innovative solutions in your area of expertise
        
        The most fulfilling path will likely combine elements of these directions in a way that aligns with your evolving interests and life priorities.
        """
        
        return career_path
    
    def _generate_development_roadmap(self, primary_role, current_skills, skill_gaps):
        """Generate a development roadmap with concrete steps"""
        
        # This would ideally use a knowledge base of skills for different roles
        # For now, we'll use a simplified approach
        
        # Generate skills needed for the primary role
        role_lower = primary_role.lower()
        needed_skills = []
        
        # Technical skills based on role keywords
        if "data" in role_lower or "analyst" in role_lower:
            needed_skills.extend(["SQL", "Data Visualization", "Statistical Analysis", "Excel/Spreadsheets"])
        elif "design" in role_lower:
            needed_skills.extend(["Design Software", "UI/UX Principles", "Visual Communication", "Prototyping"])
        elif "develop" in role_lower or "engineer" in role_lower:
            needed_skills.extend(["Programming Languages", "Version Control", "Testing", "Technical Documentation"])
        elif "research" in role_lower or "scientist" in role_lower:
            needed_skills.extend(["Research Methodologies", "Data Analysis", "Technical Writing", "Experimental Design"])
        elif "manage" in role_lower or "coordinator" in role_lower:
            needed_skills.extend(["Project Management", "Team Leadership", "Stakeholder Communication", "Budget Planning"])
        elif "market" in role_lower:
            needed_skills.extend(["Market Analysis", "Campaign Management", "Digital Marketing Tools", "Content Strategy"])
        else:
            needed_skills.extend(["Industry Knowledge", "Technical Fundamentals", "Project Management", "Analysis"])
        
        # Add universal soft skills
        soft_skills = ["Communication", "Problem Solving", "Collaboration", "Time Management", "Adaptability"]
        
        # Generate learning resources
        learning_resources = {
            "courses": [
                "Relevant online courses on platforms like Coursera, LinkedIn Learning, or Udemy",
                "Industry-specific certifications that validate key skills",
                "Local community college or continuing education programs"
            ],
            "experiences": [
                "Volunteer for projects that build relevant skills",
                "Contribute to open-source or community initiatives",
                "Create personal projects that demonstrate your capabilities",
                "Seek mentorship from experienced professionals"
            ],
            "resources": [
                "Industry-standard books and publications",
                "Professional association resources and events",
                "YouTube channels and podcasts from industry leaders",
                "Online communities and forums for knowledge sharing"
            ]
        }
        
        # Build the development roadmap
        roadmap = f"""
        To prepare for a successful career as a {primary_role} or in related roles, focus on developing these key areas:
        
        ### Essential Skills to Develop
        
        **Technical Skills:**
        """
        
        for skill in needed_skills[:4]:
            roadmap += f"- {skill}\n"
        
        roadmap += "\n**Foundational Soft Skills:**\n"
        
        for skill in soft_skills[:3]:
            roadmap += f"- {skill}\n"
        
        roadmap += """
        ### Learning Pathway
        
        **Recommended Courses and Certifications:**
        """
        
        for resource in learning_resources["courses"]:
            roadmap += f"- {resource}\n"
        
        roadmap += "\n**Hands-On Experience Building:**\n"
        
        for experience in learning_resources["experiences"][:3]:
            roadmap += f"- {experience}\n"
        
        roadmap += "\n**Helpful Resources:**\n"
        
        for resource in learning_resources["resources"][:3]:
            roadmap += f"- {resource}\n"
        
        roadmap += """
        ### Milestones & Timeline
        
        **First 6 Months:**
        - Complete foundational learning in 1-2 core technical skills
        - Build a small portfolio project demonstrating these skills
        - Join relevant professional communities
        
        **6-12 Months:**
        - Obtain entry-level certification or complete comprehensive course
        - Develop or contribute to a more substantial project
        - Begin networking with professionals in target roles
        
        **1-2 Years:**
        - Apply for relevant positions or take on related responsibilities in current role
        - Continue advancing skills through progressive challenges
        - Establish professional presence through sharing knowledge or work
        """
        
        return roadmap