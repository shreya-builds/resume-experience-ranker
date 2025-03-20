# Resume Experience Ranker

An AI-powered tool that intelligently analyzes and reranks your professional experiences to create targeted resumes for specific job postings. Using CrewAI agents, this tool helps you present the most relevant experiences for each job application.

## 🎯 What It Does

- **Experience Analysis**: Analyzes up to 20 experience bullets from your various professional roles
- **Job Requirement Matching**: Compares your experiences with job posting requirements
- **Smart Ranking**: Prioritizes and selects the most relevant experiences for the specific job
- **ATS Optimization**: Ensures your resume is optimized for Applicant Tracking Systems
- **Automated Customization**: Creates a tailored resume with the most impactful experiences

## 🤖 How It Works

The system uses three specialized AI agents:

1. **Resume Analyzer**
   - Analyzes your experience bullets against job requirements
   - Identifies keyword matches and gaps
   - Evaluates experience alignment
   - Suggests specific improvements

2. **Resume Editor**
   - Transforms content to match job requirements
   - Optimizes keywords from the job posting
   - Enhances experience descriptions
   - Creates ATS-friendly formatting

3. **Resume Quality Controller**
   - Verifies keyword optimization
   - Ensures all job requirements are addressed
   - Validates formatting and structure
   - Performs final quality checks

## 📋 Prerequisites

- Python 3.8+
- OpenAI API key
- Your experience bullets in PDF format
- Job posting in text format

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/shreya-builds/resume-experience-ranker.git
cd resume-experience-ranker
```

2. Install dependencies:
```bash
pip install python-dotenv crewai pyyaml openai PyPDF2
```

3. Create a `.env` file with your OpenAI API key:
```env
MODEL=o1-mini
OPENAI_API_KEY=your_api_key_here
```

## 💻 Usage

1. Prepare your files:
   - Save your experience bullets in a PDF file
   - Save the job posting in a text file
   - Place both files on your desktop

2. Update file paths in `main.py` if needed

3. Run the script:
```bash
python src/resumebuild/main.py
```

4. Get your optimized resume:
   - Analysis report of your experiences
   - Ranked and selected experience bullets
   - Updated resume in `updated_resume.txt`

## 📁 Project Structure

```
resumebuild/
├── src/
│   └── resumebuild/
│       ├── config/
│       │   ├── agents.yaml    # AI agent configurations
│       │   └── tasks.yaml     # Task definitions
│       └── main.py           # Main script
├── .env                      # Environment variables
└── README.md                # Documentation
```

## ✨ Features

- **Smart Experience Selection**: Automatically selects the most relevant experiences
- **Keyword Optimization**: Enhances content with job-specific keywords
- **ATS Compatibility**: Ensures resume passes ATS systems
- **Format Preservation**: Maintains professional formatting
- **Customization**: Creates unique resumes for each job application

## 🤝 Contributing

Feel free to:
- Open issues
- Submit pull requests
- Suggest improvements
- Share feedback

## 📝 Note

This tool helps optimize your resume but should be used alongside your judgment. Always review and adjust the output to ensure it accurately represents your experiences.
