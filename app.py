from flask import Flask, render_template, request
from resume_parser.parser import extract_text
from analyzer.analyzer import analyze_resume
from config import Config
import os

app = Flask(__name__)

app.config.from_object(Config)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["resume"]

    # Check if a file was selected
    if file.filename == "":
        return "No file selected."

    # Save uploaded file
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # Extract resume text
    resume_text = extract_text(filepath)

    # Analyze resume
    (
        score,
        suggestions,
        detected_skills,
        missing_skills,
        emails,
        phone_found,
        linkedin_found,
        github_found
    ) = analyze_resume(resume_text)

    # Print results to terminal
    print("\n========== Resume Analysis ==========")

    print(f"\nResume Score: {score}/100")

    print("\nDetected Skills:")
    if detected_skills:
        for skill in detected_skills:
            print("-", skill.title())
    else:
        print("No skills detected.")

    print("\nMissing Skills:")
    if missing_skills:
        for skill in missing_skills:
            print("-", skill.title())
    else:
        print("No missing skills.")

    print("\nEmail(s):")
    if emails:
        for email in emails:
            print("-", email)
    else:
        print("No email found.")

    print("\nPhone:")
    print("Detected" if phone_found else "Not Detected")

    print("\nLinkedIn:")
    print("Detected" if linkedin_found else "Not Detected")

    print("\nGitHub:")
    print("Detected" if github_found else "Not Detected")

    print("\nSuggestions:")
    if suggestions:
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("No suggestions. Great resume!")

    print("\n=====================================")

    return render_template(
        "result.html",
        score=score,
        suggestions=suggestions,
        detected_skills=detected_skills,
        missing_skills=missing_skills,
        emails=emails,
        phone_found=phone_found,
        linkedin_found=linkedin_found,
        github_found=github_found
    )


if __name__ == "__main__":
    app.run(debug=True)