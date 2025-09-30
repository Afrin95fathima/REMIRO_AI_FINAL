# 🚀 Remiro AI - AI-Powered Career Guidance Platform# 🚀 Remiro AI - AI-Powered Career Guidance Platform# Remiro AI - AI-Powered Career Guidance Platform



## Overview



Remiro AI is a comprehensive career guidance platform that leverages artificial intelligence to provide personalized career analysis, strategy development, and action planning. The system uses a multi-agent architecture to analyze different aspects of career development and provide holistic recommendations.## OverviewRemiro AI is an advanced career guidance platform that provides personalized career counseling through a 12D agent analysis system orchestrated by a Master Agent. The platform is built with Python and Streamlit, offering an interactive chat interface for comprehensive career assessment and planning.



## ✨ Features



- **15-Agent Analysis System**: Comprehensive evaluation across multiple career dimensionsRemiro AI is a comprehensive career guidance platform that leverages artificial intelligence to provide personalized career analysis, strategy development, and action planning. The system uses a multi-agent architecture to analyze different aspects of career development and provide holistic recommendations.## Features

- **Personalized Career Strategy**: Tailored recommendations based on individual profile

- **Interactive Q&A Interface**: Engaging conversation-based assessment

- **Professional Reports**: Download career reports in HTML, PDF, and Word formats

- **Progress Tracking**: Real-time progress monitoring throughout the analysis## ✨ Features- **Single Chat Interface**: Conversational, interactive, and supportive interface similar to ChatGPT or Gemini

- **Modern UI**: Clean, professional interface with responsive design

- **Master Agent Orchestration**: Central controller that manages the user experience and 12D agent system

## 🏗️ Architecture

- **15-Agent Analysis System**: Comprehensive evaluation across multiple career dimensions- **12D Analysis System**: Twelve specialized agents that analyze different aspects of the user's career profile

### Core Components

- **Personalized Career Strategy**: Tailored recommendations based on individual profile- **Personalized Career Roadmap**: Custom career path recommendations based on comprehensive assessment

- **Master Agent**: Orchestrates the entire analysis process

- **Specialized Agents**: 15 domain-specific agents for focused analysis- **Interactive Q&A Interface**: Engaging conversation-based assessment- **User Data Persistence**: Storing and recalling user data across sessions

- **UI Layer**: Streamlit-based interactive interface

- **Report Generator**: Multi-format report generation system- **Professional Reports**: Download career reports in HTML, PDF, and Word formats- **Downloadable Reports**: Option to download personalized career guidance reports



### Agent Categories- **Progress Tracking**: Real-time progress monitoring throughout the analysis



#### Phase 1: Self-Discovery- **Modern UI**: Clean, professional interface with responsive design## 12D Agent System

- Skills Agent - Technical and soft skills assessment

- Values Agent - Personal values and priorities analysis

- Personality Agent - Work style and personality evaluation

- Interests Agent - Passion and interest mapping## 🏗️ ArchitectureThe platform includes these specialized agents:



#### Phase 2: Career Strategy

- Purpose Agent - Life purpose and meaning exploration

- Aspirations Agent - Career goals and aspirations### Core Components1. **Personality Agent**: Analyzes personality traits and work style preferences

- Industry Agent - Market trends and industry analysis

- Work Environment Agent - Preferred work settings2. **Interests Agent**: Maps interests to viable career domains



#### Phase 3: Practical Planning- **Master Agent**: Orchestrates the entire analysis process3. **Aspirations Agent**: Helps define career vision and goals

- Financial Agent - Compensation and financial strategy

- Learning Agent - Development and skill building- **Specialized Agents**: 15 domain-specific agents for focused analysis4. **Skills Agent**: Audits current skills and identifies gaps

- Career Trajectory Agent - Career progression planning

- Role Fit Agent - Job compatibility assessment- **UI Layer**: Streamlit-based interactive interface5. **Motivations & Values Agent**: Identifies core career motivators



#### Phase 4: Integration- **Report Generator**: Multi-format report generation system6. **Cognitive Abilities Agent**: Analyzes thinking patterns and problem-solving styles

- Network Agent - Professional networking strategy

- Identity Agent - Personal branding and identity7. **Learning Preferences Agent**: Determines optimal learning strategies

- Career Roadmap Agent - Comprehensive action planning

### Agent Categories8. **Physical Context Agent**: Analyzes ideal work environment needs

## 🚀 Quick Start

9. **Strengths & Weaknesses Agent**: Inventories core strengths and development areas

### Prerequisites

#### Phase 1: Self-Discovery10. **Emotional Intelligence Agent**: Assesses EQ and interpersonal effectiveness

- Python 3.8 - 3.11 (recommended)

- pip package manager- Skills Agent - Technical and soft skills assessment11. **Track Record Agent**: Synthesizes past experiences into a career narrative



### Installation- Values Agent - Personal values and priorities analysis12. **Constraints Agent**: Addresses real-world limitations and practicalities



1. Clone the repository:- Personality Agent - Work style and personality evaluation

```bash

git clone https://github.com/Afrin95fathima/REMIRO_AI_FINAL.git- Interests Agent - Passion and interest mapping## Project Structure

cd REMIRO_AI_FINAL

```



2. Create a virtual environment (recommended):#### Phase 2: Career Strategy```

```bash

# On Windows- Purpose Agent - Life purpose and meaning explorationRemiro AI/

python -m venv venv

venv\Scripts\activate- Aspirations Agent - Career goals and aspirations│



# On macOS/Linux- Industry Agent - Market trends and industry analysis├── app.py                 # Main Streamlit application entry point

python -m venv venv

source venv/bin/activate- Work Environment Agent - Preferred work settings│

```

├── agents/                # Agent modules

3. Install dependencies:

#### Phase 3: Practical Planning│   ├── master_agent.py    # Master Agent orchestrator

**Option A: Standard Installation**

```bash- Financial Agent - Compensation and financial strategy│   ├── skills_agent.py    # Skills & Competency Architect

pip install -r requirements.txt

```- Learning Agent - Development and skill building│   ├── values_agent.py    # Principle Navigator



**Option B: If Option A fails (Minimal Installation)**- Career Trajectory Agent - Career progression planning│   ├── financial_agent.py # Financial Strategist

```bash

pip install -r requirements-minimal.txt- Role Fit Agent - Job compatibility assessment│   ├── learning_agent.py  # Learning Style Analyst

```

│   ├── industry_agent.py  # Industry Specialist

**Option C: Manual Installation (If both above fail)**

```bash#### Phase 4: Integration│   ├── network_agent.py   # Relationship Builder

pip install streamlit

pip install pandas>=1.3.0- Network Agent - Professional networking strategy│   ├── role_fit_agent.py  # Role Match Specialist

pip install google-generativeai

pip install reportlab- Identity Agent - Personal branding and identity│   ├── work_environment_agent.py # Workplace Ecology Specialist

pip install python-docx

pip install requests python-dotenv pillow- Career Roadmap Agent - Comprehensive action planning│   ├── identity_agent.py  # Personal Brand Strategist

```

│   ├── purpose_agent.py   # Meaning Architect

4. Run the application:

```bash## 🚀 Quick Start│   ├── career_trajectory_agent.py # Strategic Pathway Designer

streamlit run app.py

```│



5. Open your browser and navigate to `http://localhost:8501`### Prerequisites├── utils/                 # Utility modules



### Troubleshooting Installation│   ├── news_service.py    # Career news service



#### Windows Users - Pandas Installation Issues- Python 3.8 or higher│   ├── session_state.py   # Session management



If you encounter build errors with pandas, try:- pip package manager│   └── ui_helpers.py      # UI components and helpers



1. **Use pre-compiled wheels:**│

```bash

pip install --only-binary=all pandas### Installation├── data/                  # User data storage

```

│

2. **Use conda instead of pip:**

```bash1. Clone the repository:├── static/                # Static assets

conda install pandas streamlit

pip install google-generativeai reportlab python-docx```bash│   ├── css/               # Stylesheets

```

git clone https://github.com/Afrin95fathima/REMIRO_AI_FINAL.git│   └── images/            # Images

3. **Install Visual Studio Build Tools (if needed):**

- Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/cd REMIRO_AI_FINAL│

- Install "C++ build tools" workload

```├── requirements.txt       # Project dependencies

#### Common Solutions

└── README.md              # Documentation

1. **Update pip first:**

```bash2. Install dependencies:

python -m pip install --upgrade pip

``````bash```



2. **Clear pip cache:**pip install -r requirements.txt

```bash

pip cache purge```## Installation

```



3. **Use conda for scientific packages:**

```bash3. Run the application:1. Clone the repository

conda install pandas numpy streamlit

pip install google-generativeai reportlab python-docx```bash   ```

```

streamlit run app.py   git clone https://github.com/yourusername/remiro-ai.git

4. **Python version compatibility:**

- Recommended: Python 3.8 - 3.11```   cd remiro-ai

- Avoid Python 3.12 (some packages may not be compatible yet)

   ```

#### Alternative Installation Methods

4. Open your browser and navigate to `http://localhost:8501`

**Using conda (Recommended for Windows):**

```bash2. Create a virtual environment

conda create -n remiro python=3.10

conda activate remiro## 📁 Project Structure   ```

conda install streamlit pandas numpy

pip install google-generativeai reportlab python-docx requests python-dotenv pillow   python -m venv venv

```

```   source venv/bin/activate  # On Windows: venv\Scripts\activate

**Using Docker (Universal solution):**

```dockerfileREMIRO_AI_FINAL/   ```

# Create Dockerfile with this content:

FROM python:3.10-slim├── agents/                     # AI agent modules



WORKDIR /app│   ├── master_agent.py        # Main orchestrator3. Install dependencies

COPY requirements-minimal.txt .

RUN pip install -r requirements-minimal.txt│   ├── skills_agent.py        # Skills assessment   ```



COPY . .│   ├── values_agent.py        # Values analysis   pip install -r requirements.txt

EXPOSE 8501

│   ├── personality_agent.py   # Personality evaluation   ```

CMD ["streamlit", "run", "app.py"]

```│   ├── interests_agent.py     # Interest mapping



Then run:│   ├── purpose_agent.py       # Purpose exploration4. Set up your environment variables

```bash

docker build -t remiro-ai .│   ├── aspirations_agent.py   # Goal setting   - Create a `.env` file in the root directory

docker run -p 8501:8501 remiro-ai

```│   ├── industry_agent.py      # Industry analysis   - Add your Google Gemini API key:



## 📁 Project Structure│   ├── work_environment_agent.py # Environment preferences     ```



```│   ├── financial_agent.py     # Financial planning     GEMINI_API_KEY=your_api_key_here

REMIRO_AI_FINAL/

├── agents/                     # AI agent modules│   ├── learning_agent.py      # Learning strategy     ```

│   ├── master_agent.py        # Main orchestrator

│   ├── skills_agent.py        # Skills assessment│   ├── career_trajectory_agent.py # Career progression

│   ├── values_agent.py        # Values analysis

│   ├── personality_agent.py   # Personality evaluation│   ├── role_fit_agent.py      # Role compatibility## Running the Application

│   ├── interests_agent.py     # Interest mapping

│   ├── purpose_agent.py       # Purpose exploration│   ├── network_agent.py       # Networking strategy

│   ├── aspirations_agent.py   # Goal setting

│   ├── industry_agent.py      # Industry analysis│   ├── identity_agent.py      # Personal branding```

│   ├── work_environment_agent.py # Environment preferences

│   ├── financial_agent.py     # Financial planning│   └── career_roadmap_agent.py # Action planningstreamlit run app.py

│   ├── learning_agent.py      # Learning strategy

│   ├── career_trajectory_agent.py # Career progression├── utils/                      # Utility modules```

│   ├── role_fit_agent.py      # Role compatibility

│   ├── network_agent.py       # Networking strategy│   ├── gemini_api.py          # AI API integration

│   ├── identity_agent.py      # Personal branding

│   └── career_roadmap_agent.py # Action planning│   ├── news_service.py        # Career news service## Deployment

├── utils/                      # Utility modules

│   ├── gemini_api.py          # AI API integration│   ├── session_state.py       # Session management

│   ├── news_service.py        # Career news service

│   ├── session_state.py       # Session management│   └── ui_helpers.py          # UI helper functions### Streamlit Cloud

│   └── ui_helpers.py          # UI helper functions

├── data/                       # User data storage├── data/                       # User data storage

├── app.py                      # Main application entry point

├── requirements.txt            # Standard dependencies├── app.py                      # Main application entry point1. Push your code to a GitHub repository

├── requirements-minimal.txt    # Minimal dependencies

├── .gitignore                 # Git ignore rules├── requirements.txt            # Python dependencies2. Log in to [Streamlit Cloud](https://streamlit.io/cloud)

└── README.md                  # Project documentation

```├── .gitignore                 # Git ignore rules3. Create a new app pointing to your repository



## 🔧 Configuration└── README.md                  # Project documentation4. Set the necessary secrets:



### Environment Variables```   - `GEMINI_API_KEY`



Create a `.env` file in the root directory with the following variables:



```env## 🔧 Configuration### Docker Deployment

GEMINI_API_KEY=your_gemini_api_key_here

```



### API Key Setup### Environment Variables1. Build the Docker image



1. Get a Google Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)   ```

2. Replace the API key in `app.py` or set it as an environment variable

Create a `.env` file in the root directory with the following variables:   docker build -t remiro-ai .

## 💻 Usage

   ```

1. **Start the Application**: Run `streamlit run app.py`

2. **User Consent**: Provide consent for data collection```env

3. **Profile Setup**: Enter basic information (name, experience level)

4. **Agent Interaction**: Answer questions from 15 specialized agentsGEMINI_API_KEY=your_gemini_api_key_here2. Run the container

5. **Progress Tracking**: Monitor completion status (0/15 to 15/15)

6. **Final Report**: Receive comprehensive career strategy```   ```

7. **Download**: Get reports in HTML, PDF, or Word format

   docker run -p 8501:8501 -e GEMINI_API_KEY=your_api_key_here remiro-ai

## 📊 Output

### API Key Setup   ```

### Career Analysis Report Includes:



- **Executive Summary**: Key insights and recommendations

- **Skill Assessment**: Current capabilities and development areas1. Get a Google Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)## Environment Variables

- **Values Alignment**: Career-value compatibility analysis

- **Personality Profile**: Work style and preferences2. Replace the API key in `app.py` or set it as an environment variable

- **Career Recommendations**: Specific role and industry suggestions

- **18-Month Action Plan**: Phased implementation strategy- `GEMINI_API_KEY`: Google Gemini API key for AI functionality (Current: AIzaSyBJO45DfjO2BvOLvVTZKwyAfxLzqUycWjs)

- **Financial Strategy**: Compensation and benefits guidance

- **Personal Branding**: Professional identity development## 💻 Usage│   ├── constraints_agent.py

- **Success Metrics**: Measurable goals and milestones

│   └── career_roadmap_agent.py

## 🛠️ Technology Stack

1. **Start the Application**: Run `streamlit run app.py`│

- **Frontend**: Streamlit (Python web framework)

- **Backend**: Python 3.8+2. **User Consent**: Provide consent for data collection├── utils/                 # Utility modules

- **AI Engine**: Google Gemini Pro

- **Report Generation**: ReportLab (PDF), python-docx (Word)3. **Profile Setup**: Enter basic information (name, experience level)│   ├── session_state.py   # Manages Streamlit session state

- **Data Processing**: Pandas, NumPy

- **UI Styling**: Custom CSS with professional theme4. **Agent Interaction**: Answer questions from 15 specialized agents│   ├── ui_helpers.py      # UI component helpers



## 📈 Scalability5. **Progress Tracking**: Monitor completion status (0/15 to 15/15)│   └── news_service.py    # Career news service



The system is designed to be:6. **Final Report**: Receive comprehensive career strategy│

- **Modular**: Easy to add new agents or features

- **Extensible**: Support for additional AI models7. **Download**: Get reports in HTML, PDF, or Word format├── data/                  # User data storage

- **Configurable**: Customizable agent sequences and parameters

- **Maintainable**: Clean code structure with proper documentation│   └── user_profiles/     # Individual user data files



## 🤝 Contributing## 📊 Output│



1. Fork the repository├── static/                # Static assets

2. Create a feature branch (`git checkout -b feature/AmazingFeature`)

3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)### Career Analysis Report Includes:│   ├── css/               # Custom CSS

4. Push to the branch (`git push origin feature/AmazingFeature`)

5. Open a Pull Request│   └── images/            # Images and icons



## 📄 License- **Executive Summary**: Key insights and recommendations│



This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.- **Skill Assessment**: Current capabilities and development areas├── templates/             # HTML templates for reports



## 👥 Support- **Values Alignment**: Career-value compatibility analysis│



For support, email support@remiro-ai.com or create an issue in the GitHub repository.- **Personality Profile**: Work style and preferences├── requirements.txt       # Project dependencies



## 🎯 Roadmap- **Career Recommendations**: Specific role and industry suggestions│



- [ ] Mobile-responsive design improvements- **18-Month Action Plan**: Phased implementation strategy└── README.md              # Project documentation

- [ ] Additional AI model integration

- [ ] Advanced analytics dashboard- **Financial Strategy**: Compensation and benefits guidance```

- [ ] API endpoint development

- [ ] Multi-language support- **Personal Branding**: Professional identity development

- [ ] Integration with job platforms

- **Success Metrics**: Measurable goals and milestones## Installation

---



**Made with ❤️ by the Remiro AI Team**
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