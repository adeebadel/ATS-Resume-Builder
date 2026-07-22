from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from resume_parser.parser import extract_text
from analyzer.analyzer import analyze_resume
from analyzer.health import get_resume_health
from analyzer.skills import extract_skills
from matcher.job_matcher import match_resume_to_job
from config import Config

import logging
import os

app = Flask(__name__)
app.config.from_object(Config)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ALLOWED_EXTENSIONS = {"pdf", "docx"}


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files.get("resume")

    if file is None:
        return "Please upload a resume."

    if file.filename == "":
        return "No file selected."

    if not allowed_file(file.filename):
        return "Only PDF and DOCX files are allowed."

    filename = secure_filename(file.filename)

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    try:

        # Save Resume
        file.save(filepath)

        # Extract Resume Text
        resume_text = extract_text(filepath)

        if not resume_text.strip():
            return "Unable to read the uploaded resume."

        # Get Job Description
        job_description = request.form.get(
            "job_description",
            ""
        )

        # Resume Analysis
        analysis = analyze_resume(resume_text)

        analysis["health"] = get_resume_health(
            analysis["score"]
        )

        # Extract Skills from Job Description
        job_skills = extract_skills(job_description)

        # Match Resume with Job Description
        matched_skills, missing_job_skills, match_percentage = (
            match_resume_to_job(
                analysis["detected_skills"],
                job_skills
            )
        )

        match_result = {
            "matched_skills": matched_skills,
            "missing_skills": missing_job_skills,
            "match_percentage": match_percentage,
        }

        logger.info("=" * 50)
        logger.info("Resume Score : %s/100", analysis["score"])
        logger.info("Detected Skills : %s", analysis["detected_skills"])
        logger.info("Job Skills : %s", job_skills)
        logger.info("Matched Skills : %s", matched_skills)
        logger.info("Missing Skills : %s", missing_job_skills)
        logger.info("Job Match : %s%%", match_percentage)
        logger.info("=" * 50)

        return render_template(
            "result.html",
            analysis=analysis,
            match_result=match_result
        )

    except Exception as error:
        logger.exception("Resume processing failed.")
        return f"Error processing resume: {error}"

    finally:
        if os.path.exists(filepath):
            os.remove(filepath)


if __name__ == "__main__":
    app.run(debug=False)