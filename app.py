from flask import Flask, render_template, request
from resume_parser.parser import extract_text
from analyzer.analyzer import analyze_resume
from config import Config
import os

app = Flask(__name__)

# Load configuration
app.config.from_object(Config)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    # Get uploaded file
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
    analysis = analyze_resume(resume_text)

    # -----------------------------
    # Print Results to Terminal
    # -----------------------------

    print("\n========== Resume Analysis ==========")

    print(f"\nResume Score: {analysis['score']}/100")

    print("\nDetected Skills:")
    if analysis["detected_skills"]:
        for skill in analysis["detected_skills"]:
            print("-", skill.title())
    else:
        print("No skills detected.")

    print("\nMissing Skills:")
    if analysis["missing_skills"]:
        for skill in analysis["missing_skills"]:
            print("-", skill.title())
    else:
        print("No missing skills.")

    print("\nEmail(s):")
    if analysis["emails"]:
        for email in analysis["emails"]:
            print("-", email)
    else:
        print("No email found.")

    print("\nContact Information")
    print("-------------------------")
    print("Email     :", "✅ Found" if analysis["email_found"] else "❌ Missing")
    print("Phone     :", "✅ Found" if analysis["phone_found"] else "❌ Missing")
    print("LinkedIn  :", "✅ Found" if analysis["linkedin_found"] else "❌ Missing")
    print("GitHub    :", "✅ Found" if analysis["github_found"] else "❌ Missing")

    print("\nSuggestions:")
    if analysis["suggestions"]:
        for suggestion in analysis["suggestions"]:
            print("-", suggestion)
    else:
        print("No suggestions. Great resume!")

    print("\n=====================================\n")

    # Send the complete analysis dictionary to HTML
    return render_template(
        "result.html",
        analysis=analysis
    )


if __name__ == "__main__":
    app.run(debug=True)