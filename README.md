# CareerAI

## Overview

CareerAI is a Flask-based ATS Resume Analyzer that helps users upload resumes, extract text, analyze content, detect skills, and provide suggestions for improvement.

---

## Features

- Upload PDF and DOCX resumes
- Resume text extraction
- ATS Resume Score
- Skill Detection
- Missing Skills Detection
- Email Detection
- Phone Detection
- LinkedIn Detection
- GitHub Detection
- Resume Suggestions

---

## Tech Stack

- Python
- Flask
- HTML
- CSS
- Regex
- pdfplumber
- python-docx

---

## Installation

```bash
git clone <repository-url>

cd CareerAI

pip install -r requirements.txt

python app.py
```

---

## Usage

1. Open the website.

2. Upload your resume.

3. View your ATS score.

4. Review detected skills and suggestions.

---

## Future Improvements

- AI Resume Feedback
- Resume Rewriter
- User Login
- Database
- Resume History
- Cloud Deployment

## Project Structure

```text
CareerAI
│
├── app.py
├── config.py
│
├── analyzer
│   ├── analyzer.py
│   ├── regex.py
│   ├── scorer.py
│   ├── report.py
│   └── skills.py
│
├── resume_parser
│   └── parser.py
│
├── templates
│
├── static
│
└── tests
```