"""
CareerAI Report Builder
-----------------------
Builds the final report dictionary.
"""


def build_report(
    score,
    suggestions,
    detected_skills,
    missing_skills,
    emails,
    phone_found,
    linkedin_found,
    github_found,
    education_found,
    project_found,
    experience_found,
):
    """
    Build the final report dictionary.
    """

    return {
        "score": score,
        "suggestions": suggestions,
        "detected_skills": detected_skills,
        "missing_skills": missing_skills,
        "emails": emails,
        "email_found": bool(emails),
        "phone_found": phone_found,
        "linkedin_found": linkedin_found,
        "github_found": github_found,
        "education_found": education_found,
        "project_found": project_found,
        "experience_found": experience_found,
    }