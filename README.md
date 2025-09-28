# Remiro AI - AI-Powered Career Guidance Platform

Remiro AI is an advanced career guidance platform that provides personalized career counseling through a 12D agent analysis system orchestrated by a Master Agent. The platform is built with Python and Streamlit, offering an interactive chat interface for comprehensive career assessment and planning.

## Features

- **Single Chat Interface**: Conversational, interactive, and supportive interface similar to ChatGPT or Gemini
- **Master Agent Orchestration**: Central controller that manages the user experience and 12D agent system
- **12D Analysis System**: Twelve specialized agents that analyze different aspects of the user's career profile
- **Personalized Career Roadmap**: Custom career path recommendations based on comprehensive assessment
- **User Data Persistence**: Storing and recalling user data across sessions
- **Downloadable Reports**: Option to download personalized career guidance reports

## 12D Agent System

The platform includes these specialized agents:

1. **Personality Agent**: Analyzes personality traits and work style preferences
2. **Interests Agent**: Maps interests to viable career domains
3. **Aspirations Agent**: Helps define career vision and goals
4. **Skills Agent**: Audits current skills and identifies gaps
5. **Motivations & Values Agent**: Identifies core career motivators
6. **Cognitive Abilities Agent**: Analyzes thinking patterns and problem-solving styles
7. **Learning Preferences Agent**: Determines optimal learning strategies
8. **Physical Context Agent**: Analyzes ideal work environment needs
9. **Strengths & Weaknesses Agent**: Inventories core strengths and development areas
10. **Emotional Intelligence Agent**: Assesses EQ and interpersonal effectiveness
11. **Track Record Agent**: Synthesizes past experiences into a career narrative
12. **Constraints Agent**: Addresses real-world limitations and practicalities

## Project Structure

```
Remiro AI/
│
├── app.py                 # Main Streamlit application entry point
│
├── agents/                # Agent modules
│   ├── master_agent.py    # Master Agent orchestrator
│   ├── skills_agent.py    # Skills & Competency Architect
│   ├── values_agent.py    # Principle Navigator
│   ├── financial_agent.py # Financial Strategist
│   ├── learning_agent.py  # Learning Style Analyst
│   ├── industry_agent.py  # Industry Specialist
│   ├── network_agent.py   # Relationship Builder
│   ├── role_fit_agent.py  # Role Match Specialist
│   ├── work_environment_agent.py # Workplace Ecology Specialist
│   ├── identity_agent.py  # Personal Brand Strategist
│   ├── purpose_agent.py   # Meaning Architect
│   ├── career_trajectory_agent.py # Strategic Pathway Designer
│
├── utils/                 # Utility modules
│   ├── news_service.py    # Career news service
│   ├── session_state.py   # Session management
│   └── ui_helpers.py      # UI components and helpers
│
├── data/                  # User data storage
│
├── static/                # Static assets
│   ├── css/               # Stylesheets
│   └── images/            # Images
│
├── requirements.txt       # Project dependencies
└── README.md              # Documentation

```

## Installation

1. Clone the repository
   ```
   git clone https://github.com/yourusername/remiro-ai.git
   cd remiro-ai
   ```

2. Create a virtual environment
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables
   - Create a `.env` file in the root directory
   - Add your Google Gemini API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

## Running the Application

```
streamlit run app.py
```

## Deployment

### Streamlit Cloud

1. Push your code to a GitHub repository
2. Log in to [Streamlit Cloud](https://streamlit.io/cloud)
3. Create a new app pointing to your repository
4. Set the necessary secrets:
   - `GEMINI_API_KEY`

### Docker Deployment

1. Build the Docker image
   ```
   docker build -t remiro-ai .
   ```

2. Run the container
   ```
   docker run -p 8501:8501 -e GEMINI_API_KEY=your_api_key_here remiro-ai
   ```

## Environment Variables

- `GEMINI_API_KEY`: Google Gemini API key for AI functionality (Current: AIzaSyBJO45DfjO2BvOLvVTZKwyAfxLzqUycWjs)
│   ├── constraints_agent.py
│   └── career_roadmap_agent.py
│
├── utils/                 # Utility modules
│   ├── session_state.py   # Manages Streamlit session state
│   ├── ui_helpers.py      # UI component helpers
│   └── news_service.py    # Career news service
│
├── data/                  # User data storage
│   └── user_profiles/     # Individual user data files
│
├── static/                # Static assets
│   ├── css/               # Custom CSS
│   └── images/            # Images and icons
│
├── templates/             # HTML templates for reports
│
├── requirements.txt       # Project dependencies
│
└── README.md              # Project documentation
```

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/remiro-ai.git
   cd remiro-ai
   ```

2. Create and activate a virtual environment:
   ```
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```
   streamlit run app.py
   ```

2. Open your browser and navigate to the URL displayed in your terminal (typically http://localhost:8501)

3. Follow the on-screen instructions to:
   - Provide consent for data collection
   - Enter your basic information
   - Select your available time for the session
   - Engage with the career guidance agents

## Deployment

To deploy Remiro AI using Streamlit Cloud:

1. Push your code to GitHub
2. Sign in to [Streamlit Cloud](https://streamlit.io/cloud)
3. Create a new app and connect it to your GitHub repository
4. Configure the app with:
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