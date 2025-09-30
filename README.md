# 🚀 Remiro AI - AI-Powered Career Guidance Platform# Remiro AI - AI-Powered Career Guidance Platform



## OverviewRemiro AI is an advanced career guidance platform that provides personalized career counseling through a 12D agent analysis system orchestrated by a Master Agent. The platform is built with Python and Streamlit, offering an interactive chat interface for comprehensive career assessment and planning.



Remiro AI is a comprehensive career guidance platform that leverages artificial intelligence to provide personalized career analysis, strategy development, and action planning. The system uses a multi-agent architecture to analyze different aspects of career development and provide holistic recommendations.## Features



## ✨ Features- **Single Chat Interface**: Conversational, interactive, and supportive interface similar to ChatGPT or Gemini

- **Master Agent Orchestration**: Central controller that manages the user experience and 12D agent system

- **15-Agent Analysis System**: Comprehensive evaluation across multiple career dimensions- **12D Analysis System**: Twelve specialized agents that analyze different aspects of the user's career profile

- **Personalized Career Strategy**: Tailored recommendations based on individual profile- **Personalized Career Roadmap**: Custom career path recommendations based on comprehensive assessment

- **Interactive Q&A Interface**: Engaging conversation-based assessment- **User Data Persistence**: Storing and recalling user data across sessions

- **Professional Reports**: Download career reports in HTML, PDF, and Word formats- **Downloadable Reports**: Option to download personalized career guidance reports

- **Progress Tracking**: Real-time progress monitoring throughout the analysis

- **Modern UI**: Clean, professional interface with responsive design## 12D Agent System



## 🏗️ ArchitectureThe platform includes these specialized agents:



### Core Components1. **Personality Agent**: Analyzes personality traits and work style preferences

2. **Interests Agent**: Maps interests to viable career domains

- **Master Agent**: Orchestrates the entire analysis process3. **Aspirations Agent**: Helps define career vision and goals

- **Specialized Agents**: 15 domain-specific agents for focused analysis4. **Skills Agent**: Audits current skills and identifies gaps

- **UI Layer**: Streamlit-based interactive interface5. **Motivations & Values Agent**: Identifies core career motivators

- **Report Generator**: Multi-format report generation system6. **Cognitive Abilities Agent**: Analyzes thinking patterns and problem-solving styles

7. **Learning Preferences Agent**: Determines optimal learning strategies

### Agent Categories8. **Physical Context Agent**: Analyzes ideal work environment needs

9. **Strengths & Weaknesses Agent**: Inventories core strengths and development areas

#### Phase 1: Self-Discovery10. **Emotional Intelligence Agent**: Assesses EQ and interpersonal effectiveness

- Skills Agent - Technical and soft skills assessment11. **Track Record Agent**: Synthesizes past experiences into a career narrative

- Values Agent - Personal values and priorities analysis12. **Constraints Agent**: Addresses real-world limitations and practicalities

- Personality Agent - Work style and personality evaluation

- Interests Agent - Passion and interest mapping## Project Structure



#### Phase 2: Career Strategy```

- Purpose Agent - Life purpose and meaning explorationRemiro AI/

- Aspirations Agent - Career goals and aspirations│

- Industry Agent - Market trends and industry analysis├── app.py                 # Main Streamlit application entry point

- Work Environment Agent - Preferred work settings│

├── agents/                # Agent modules

#### Phase 3: Practical Planning│   ├── master_agent.py    # Master Agent orchestrator

- Financial Agent - Compensation and financial strategy│   ├── skills_agent.py    # Skills & Competency Architect

- Learning Agent - Development and skill building│   ├── values_agent.py    # Principle Navigator

- Career Trajectory Agent - Career progression planning│   ├── financial_agent.py # Financial Strategist

- Role Fit Agent - Job compatibility assessment│   ├── learning_agent.py  # Learning Style Analyst

│   ├── industry_agent.py  # Industry Specialist

#### Phase 4: Integration│   ├── network_agent.py   # Relationship Builder

- Network Agent - Professional networking strategy│   ├── role_fit_agent.py  # Role Match Specialist

- Identity Agent - Personal branding and identity│   ├── work_environment_agent.py # Workplace Ecology Specialist

- Career Roadmap Agent - Comprehensive action planning│   ├── identity_agent.py  # Personal Brand Strategist

│   ├── purpose_agent.py   # Meaning Architect

## 🚀 Quick Start│   ├── career_trajectory_agent.py # Strategic Pathway Designer

│

### Prerequisites├── utils/                 # Utility modules

│   ├── news_service.py    # Career news service

- Python 3.8 or higher│   ├── session_state.py   # Session management

- pip package manager│   └── ui_helpers.py      # UI components and helpers

│

### Installation├── data/                  # User data storage

│

1. Clone the repository:├── static/                # Static assets

```bash│   ├── css/               # Stylesheets

git clone https://github.com/Afrin95fathima/REMIRO_AI_FINAL.git│   └── images/            # Images

cd REMIRO_AI_FINAL│

```├── requirements.txt       # Project dependencies

└── README.md              # Documentation

2. Install dependencies:

```bash```

pip install -r requirements.txt

```## Installation



3. Run the application:1. Clone the repository

```bash   ```

streamlit run app.py   git clone https://github.com/yourusername/remiro-ai.git

```   cd remiro-ai

   ```

4. Open your browser and navigate to `http://localhost:8501`

2. Create a virtual environment

## 📁 Project Structure   ```

   python -m venv venv

```   source venv/bin/activate  # On Windows: venv\Scripts\activate

REMIRO_AI_FINAL/   ```

├── agents/                     # AI agent modules

│   ├── master_agent.py        # Main orchestrator3. Install dependencies

│   ├── skills_agent.py        # Skills assessment   ```

│   ├── values_agent.py        # Values analysis   pip install -r requirements.txt

│   ├── personality_agent.py   # Personality evaluation   ```

│   ├── interests_agent.py     # Interest mapping

│   ├── purpose_agent.py       # Purpose exploration4. Set up your environment variables

│   ├── aspirations_agent.py   # Goal setting   - Create a `.env` file in the root directory

│   ├── industry_agent.py      # Industry analysis   - Add your Google Gemini API key:

│   ├── work_environment_agent.py # Environment preferences     ```

│   ├── financial_agent.py     # Financial planning     GEMINI_API_KEY=your_api_key_here

│   ├── learning_agent.py      # Learning strategy     ```

│   ├── career_trajectory_agent.py # Career progression

│   ├── role_fit_agent.py      # Role compatibility## Running the Application

│   ├── network_agent.py       # Networking strategy

│   ├── identity_agent.py      # Personal branding```

│   └── career_roadmap_agent.py # Action planningstreamlit run app.py

├── utils/                      # Utility modules```

│   ├── gemini_api.py          # AI API integration

│   ├── news_service.py        # Career news service## Deployment

│   ├── session_state.py       # Session management

│   └── ui_helpers.py          # UI helper functions### Streamlit Cloud

├── data/                       # User data storage

├── app.py                      # Main application entry point1. Push your code to a GitHub repository

├── requirements.txt            # Python dependencies2. Log in to [Streamlit Cloud](https://streamlit.io/cloud)

├── .gitignore                 # Git ignore rules3. Create a new app pointing to your repository

└── README.md                  # Project documentation4. Set the necessary secrets:

```   - `GEMINI_API_KEY`



## 🔧 Configuration### Docker Deployment



### Environment Variables1. Build the Docker image

   ```

Create a `.env` file in the root directory with the following variables:   docker build -t remiro-ai .

   ```

```env

GEMINI_API_KEY=your_gemini_api_key_here2. Run the container

```   ```

   docker run -p 8501:8501 -e GEMINI_API_KEY=your_api_key_here remiro-ai

### API Key Setup   ```



1. Get a Google Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)## Environment Variables

2. Replace the API key in `app.py` or set it as an environment variable

- `GEMINI_API_KEY`: Google Gemini API key for AI functionality (Current: AIzaSyBJO45DfjO2BvOLvVTZKwyAfxLzqUycWjs)

## 💻 Usage│   ├── constraints_agent.py

│   └── career_roadmap_agent.py

1. **Start the Application**: Run `streamlit run app.py`│

2. **User Consent**: Provide consent for data collection├── utils/                 # Utility modules

3. **Profile Setup**: Enter basic information (name, experience level)│   ├── session_state.py   # Manages Streamlit session state

4. **Agent Interaction**: Answer questions from 15 specialized agents│   ├── ui_helpers.py      # UI component helpers

5. **Progress Tracking**: Monitor completion status (0/15 to 15/15)│   └── news_service.py    # Career news service

6. **Final Report**: Receive comprehensive career strategy│

7. **Download**: Get reports in HTML, PDF, or Word format├── data/                  # User data storage

│   └── user_profiles/     # Individual user data files

## 📊 Output│

├── static/                # Static assets

### Career Analysis Report Includes:│   ├── css/               # Custom CSS

│   └── images/            # Images and icons

- **Executive Summary**: Key insights and recommendations│

- **Skill Assessment**: Current capabilities and development areas├── templates/             # HTML templates for reports

- **Values Alignment**: Career-value compatibility analysis│

- **Personality Profile**: Work style and preferences├── requirements.txt       # Project dependencies

- **Career Recommendations**: Specific role and industry suggestions│

- **18-Month Action Plan**: Phased implementation strategy└── README.md              # Project documentation

- **Financial Strategy**: Compensation and benefits guidance```

- **Personal Branding**: Professional identity development

- **Success Metrics**: Measurable goals and milestones## Installation



## 🛠️ Technology Stack1. Clone this repository:

   ```

- **Frontend**: Streamlit (Python web framework)   git clone https://github.com/your-username/remiro-ai.git

- **Backend**: Python 3.8+   cd remiro-ai

- **AI Engine**: Google Gemini Pro   ```

- **Report Generation**: ReportLab (PDF), python-docx (Word)

- **Data Processing**: Pandas, NumPy2. Create and activate a virtual environment:

- **UI Styling**: Custom CSS with professional theme   ```

   # On Windows

## 📈 Scalability   python -m venv venv

   venv\Scripts\activate

The system is designed to be:

- **Modular**: Easy to add new agents or features   # On macOS/Linux

- **Extensible**: Support for additional AI models   python3 -m venv venv

- **Configurable**: Customizable agent sequences and parameters   source venv/bin/activate

- **Maintainable**: Clean code structure with proper documentation   ```



## 🤝 Contributing3. Install dependencies:

   ```

1. Fork the repository   pip install -r requirements.txt

2. Create a feature branch (`git checkout -b feature/AmazingFeature`)   ```

3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)

4. Push to the branch (`git push origin feature/AmazingFeature`)## Usage

5. Open a Pull Request

1. Run the Streamlit application:

## 📄 License   ```

   streamlit run app.py

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.   ```



## 👥 Support2. Open your browser and navigate to the URL displayed in your terminal (typically http://localhost:8501)



For support, email support@remiro-ai.com or create an issue in the GitHub repository.3. Follow the on-screen instructions to:

   - Provide consent for data collection

## 🎯 Roadmap   - Enter your basic information

   - Select your available time for the session

- [ ] Mobile-responsive design improvements   - Engage with the career guidance agents

- [ ] Additional AI model integration

- [ ] Advanced analytics dashboard## Deployment

- [ ] API endpoint development

- [ ] Multi-language supportTo deploy Remiro AI using Streamlit Cloud:

- [ ] Integration with job platforms

1. Push your code to GitHub

---2. Sign in to [Streamlit Cloud](https://streamlit.io/cloud)

3. Create a new app and connect it to your GitHub repository

**Made with ❤️ by the Remiro AI Team**4. Configure the app with:
   - Repository: your-username/remiro-ai
   - Branch: main
   - Main file path: app.py

For alternative deployment options:

- **Docker**: A Dockerfile is included for containerized deployment
- **Heroku**: Compatible with Heroku deployment using the Procfile
- **AWS/GCP/Azure**: Deploy as a containerized application or using platform-specific services

## Customization

### Adding or Modifying Agents

To create a new agent or modify an existing one:

1. Create a new Python file in the `agents/` directory
2. Implement the required methods: `__init__`, `get_introduction`, and `process_message`
3. Register the agent in `master_agent.py`

### Styling and Branding

To customize the appearance:

1. Modify the CSS in `static/css/` 
2. Update UI rendering functions in `utils/ui_helpers.py`
3. Replace images in the `static/images/` directory

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- The 12D Agent analysis framework is inspired by comprehensive career guidance methodologies
- Built with [Streamlit](https://streamlit.io/)
- Special thanks to all contributors and testers