import re
from analyzer.skills import COMMON_SKILLS


def analyze_resume(text):

    score = 0
    suggestions = []

    text = text.lower()

    # -----------------------------
    # Contact Information
    # -----------------------------

    emails = re.findall(r"\S+@\S+\.\S+", text)

    phone = re.search(r"(\+?\d[\d\s-]{8,}\d)", text)

    linkedin = "linkedin.com" in text

    github = "github.com" in text

    # -----------------------------
    # Skills Detection
    # -----------------------------

    detected_skills = []
    missing_skills = []

    for skill in COMMON_SKILLS:

        if skill in text:
            detected_skills.append(skill)

        else:
            missing_skills.append(skill)

    # -----------------------------
    # ATS Score
    # -----------------------------

    if "education" in text:
        score += 15
    else:
        suggestions.append("Add an Education section.")

    if "project" in text:
        score += 15
    else:
        suggestions.append("Add Projects.")

    if "experience" in text:
        score += 15
    else:
        suggestions.append("Add Work Experience.")

    if emails:
        score += 10
    else:
        suggestions.append("Add a professional email address.")

    if phone:
        score += 10
    else:
        suggestions.append("Add your phone number.")

    if linkedin:
        score += 10
    else:
        suggestions.append("Add your LinkedIn profile.")

    if github:
        score += 10
    else:
        suggestions.append("Add your GitHub profile.")

    if detected_skills:
        score += 15
    else:
        suggestions.append("Add more technical skills.")

    score = min(score, 100)

    return (
        score,
        suggestions,
        detected_skills,
        missing_skills,
        emails,
        bool(phone),
        linkedin,
        github
    )