def calculate_score(analysis):

    score = 0

    if analysis["email_found"]:
        score += 10

    if analysis["phone_found"]:
        score += 10

    if analysis["linkedin_found"]:
        score += 10

    if analysis["github_found"]:
        score += 10

    if analysis["detected_skills"]:
        score += 15

    if analysis["education_found"]:
        score += 15

    if analysis["project_found"]:
        score += 15

    if analysis["experience_found"]:
        score += 15

    return min(score, 100)