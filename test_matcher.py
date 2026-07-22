from matcher.job_matcher import match_resume_to_job

resume = [
    "python",
    "flask",
    "git",
    "html"
]

job = [
    "python",
    "docker",
    "sql",
    "flask",
    "git"
]

matched, missing, percentage = match_resume_to_job(resume, job)

print("Matched Skills:", matched)
print("Missing Skills:", missing)
print("Match Percentage:", percentage)