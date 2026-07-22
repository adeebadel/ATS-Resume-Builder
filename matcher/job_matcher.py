"""
CareerAI Job Matcher
--------------------
Compares resume skills with job description skills.
"""


def match_resume_to_job(resume_skills, job_skills):
    """
    Compare resume skills against job skills.

    Args:
        resume_skills (list): Skills detected in the resume.
        job_skills (list): Skills extracted from the job description.

    Returns:
        tuple:
            matched_skills (list)
            missing_skills (list)
            match_percentage (int | None)
    """

    # Normalize resume skills
    resume_set = {
        skill.strip().lower()
        for skill in resume_skills
        if skill.strip()
    }

    # Normalize job skills and remove duplicates
    normalized_job_skills = []
    seen = set()

    for skill in job_skills:

        clean_skill = skill.strip().lower()

        if clean_skill and clean_skill not in seen:
            normalized_job_skills.append(clean_skill)
            seen.add(clean_skill)

    # No recognizable skills found in Job Description
    if not normalized_job_skills:
        return [], [], None

    matched_skills = []
    missing_skills = []

    for skill in normalized_job_skills:

        if skill in resume_set:
            matched_skills.append(skill.title())
        else:
            missing_skills.append(skill.title())

    match_percentage = round(
        (len(matched_skills) / len(normalized_job_skills)) * 100
    )

    return (
        matched_skills,
        missing_skills,
        match_percentage,
    )