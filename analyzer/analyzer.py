import re
from analyzer.skills import COMMON_SKILLS
from analyzer.regex import (
    EMAIL_PATTERN,
    PHONE_PATTERN,
    LINKEDIN_PATTERN,
    GITHUB_PATTERN
)


def analyze_resume(text):

    score = 0
    suggestions = []

    text = text.lower()

    # -----------------------------
    # Contact Information
    # -----------------------------

    emails = re.findall(EMAIL_PATTERN, text)

    phone_found = bool(
    re.search(PHONE_PATTERN, text)
    )
    linkedin_found = bool(
    re.search(LINKEDIN_PATTERN, text)
    )

    github_found = bool(
    re.search(GITHUB_PATTERN, text)
    )

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

    if phone_found:
        score += 10
    else:
        suggestions.append("Add your phone number.")

    if linkedin_found:
        score += 10
    else:
        suggestions.append("Add your LinkedIn profile.")

    if github_found:
        score += 10
    else:
        suggestions.append("Add your GitHub profile.")

    if detected_skills:
        score += 15
    else:
        suggestions.append("Add more technical skills.")

    score = min(score, 100)

    analysis = {
        "score": score,
        "suggestions": suggestions,
        "detected_skills": detected_skills,
        "missing_skills": missing_skills,
        "emails": emails,
        "email_found": len(emails) > 0,
        "phone_found": phone_found,
        "linkedin_found": linkedin_found,
        "github_found": github_found
    }

    return analysis