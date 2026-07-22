import re

from analyzer.health import get_resume_health
from analyzer.regex import (
    EMAIL_PATTERN,
    PHONE_PATTERN,
    LINKEDIN_PATTERN,
    GITHUB_PATTERN,
)
from analyzer.skills import COMMON_SKILLS, extract_skills


def contains_keyword(text, keywords):
    """
    Check whether any keyword exists as a whole word.
    """
    return any(
        re.search(rf"\b{re.escape(word)}\b", text)
        for word in keywords
    )


def analyze_resume(text):
    """
    Analyze a resume and return a structured ATS analysis.
    """

    original_text = text
    normalized_text = text.lower()

    score = 0
    suggestions = []

    # ==========================================
    # Contact Information
    # ==========================================

    emails = re.findall(
        EMAIL_PATTERN,
        original_text
    )

    phone_found = bool(
        re.search(PHONE_PATTERN, original_text)
    )

    linkedin_found = bool(
        re.search(LINKEDIN_PATTERN, original_text)
    )

    github_found = bool(
        re.search(GITHUB_PATTERN, original_text)
    )

    # ==========================================
    # Skills Detection
    # ==========================================

    detected_skills = extract_skills(original_text)

    detected_set = set(detected_skills)

    missing_skills = [
        skill
        for skill in COMMON_SKILLS
        if skill not in detected_set
    ]

    # ==========================================
    # Education
    # ==========================================

    if contains_keyword(
        normalized_text,
        [
            "education",
            "b.tech",
            "bachelor",
            "master",
            "m.tech",
            "degree",
            "university",
            "college",
        ],
    ):
        score += 15
    else:
        suggestions.append(
            "Add an Education section."
        )

    # ==========================================
    # Projects
    # ==========================================

    if contains_keyword(
        normalized_text,
        [
            "project",
            "projects",
            "portfolio",
        ],
    ):
        score += 15
    else:
        suggestions.append(
            "Add Projects."
        )

    # ==========================================
    # Experience
    # ==========================================

    if contains_keyword(
        normalized_text,
        [
            "experience",
            "internship",
            "employment",
            "work history",
        ],
    ):
        score += 20
    else:
        suggestions.append(
            "Add Work Experience."
        )

    # ==========================================
    # Email
    # ==========================================

    if emails:
        score += 10
    else:
        suggestions.append(
            "Add a professional email address."
        )

    # ==========================================
    # Phone
    # ==========================================

    if phone_found:
        score += 10
    else:
        suggestions.append(
            "Add your phone number."
        )

    # ==========================================
    # LinkedIn
    # ==========================================

    if linkedin_found:
        score += 5
    else:
        suggestions.append(
            "Add your LinkedIn profile."
        )

    # ==========================================
    # GitHub
    # ==========================================

    if github_found:
        score += 5
    else:
        suggestions.append(
            "Add your GitHub profile."
        )

    # ==========================================
    # Skills
    # ==========================================

    if detected_skills:
        score += 20
    else:
        suggestions.append(
            "Add more technical skills."
        )

    # ==========================================
    # Final Score
    # ==========================================

    score = min(score, 100)

    health = get_resume_health(score)

    # ==========================================
    # Final Analysis Dictionary
    # ==========================================

    analysis = {
        "score": score,
        "health": health,
        "suggestions": list(dict.fromkeys(suggestions)),
        "detected_skills": detected_skills,
        "missing_skills": missing_skills,
        "emails": emails,
        "email_found": bool(emails),
        "phone_found": phone_found,
        "linkedin_found": linkedin_found,
        "github_found": github_found,
    }

    return analysis