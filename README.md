# 🚀 CareerAI

**CareerAI** is a Flask-based Resume Analyzer and ATS (Applicant Tracking System) Checker that helps users evaluate their resumes, identify missing information, and compare their skills with a job description.

It analyzes uploaded resumes, calculates an ATS score, detects technical skills, and provides actionable suggestions to improve job readiness.

---

## ✨ Features

- 📄 Upload PDF and DOCX resumes
- 📊 ATS Resume Score (0–100)
- 💻 Automatic Skill Detection
- 🎯 Resume vs Job Description Matching
- 📈 Match Percentage Calculation
- ❤️ Resume Health Indicator
- 📧 Email Detection
- 📱 Phone Number Detection
- 🔗 LinkedIn Detection
- 🐙 GitHub Detection
- 💡 Resume Improvement Suggestions
- 🎨 Clean and Responsive UI

---

## 🛠️ Tech Stack

### Backend

- Python 3
- Flask

### Frontend

- HTML5
- CSS3
- Jinja2 Templates

### Libraries

- pdfplumber
- python-docx
- Werkzeug
- Regular Expressions (re)

---

## 📂 Project Structure

```text
CareerAI/
│
├── analyzer/
│   ├── analyzer.py
│   ├── health.py
│   ├── regex.py
│   └── skills.py
│
├── matcher/
│   └── job_matcher.py
│
├── resume_parser/
│   └── parser.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── uploads/
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/CareerAI.git
```

Move into the project

```bash
cd CareerAI
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 📸 Screenshots

### Home Page

>

```
assets/home.png
```

---

### Resume Analysis


```
assets/result.png
```

---

### Job Match



```
assets/job_match.png
```

---

## 📋 How It Works

1. Upload a resume (PDF or DOCX).
2. Paste a job description.
3. CareerAI extracts the resume text.
4. Skills are automatically detected.
5. ATS score is calculated.
6. Resume health is evaluated.
7. Resume skills are compared with the job description.
8. Suggestions are generated to improve the resume.

---

## 📈 Current Features

- ATS Resume Analysis
- Resume Health Score
- Job Skill Matching
- Resume Suggestions
- Contact Information Detection
- Skill Detection
- PDF Parsing
- DOCX Parsing

---

## 🔮 Future Improvements

- AI Resume Feedback
- AI Cover Letter Generator
- AI Resume Rewriter
- Resume Keyword Optimizer
- Interview Question Generator
- User Authentication
- Resume History
- Downloadable PDF Reports
- Dashboard Analytics
- Dark Mode

---

## 🎯 Learning Outcomes

This project helped me learn:

- Flask Web Development
- Modular Python Architecture
- HTML & CSS Integration
- Jinja2 Templates
- File Upload Handling
- PDF & DOCX Parsing
- Regular Expressions
- Git & GitHub Workflow
- Software Project Structure
- Resume Parsing Concepts

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is released under the MIT License.

---

## 👨‍💻 Author

**Mohammed Ainan Adeeb**

B.Tech CSE (Data Science)

Python Developer | AI Enthusiast | Aspiring AI Engineer

GitHub: https://github.com/adeebadel

LinkedIn: 

## 📸 Screenshots

### 🏠 Home Page

![Home](assets/home.png)

---

### 📊 Resume Analysis

![Analysis](assets/analysis.png)

---

### 🎯 Job Match

![Job Match](assets/job_match.png)

---

### 💡 Resume Suggestions

![Suggestions](assets/suggestions.png)