"""
CareerAI Skills Database
------------------------
Stores common technical skills and provides
a reusable function to extract skills from text.
"""

COMMON_SKILLS = [

    # ==========================
    # Programming Languages
    # ==========================

    "typescript",
    "javascript",
    "python",
    "java",
    "c++",
    "c#",
    "c",
    "go",
    "rust",
    "php",

    # ==========================
    # Web Development
    # ==========================

    "html",
    "css",
    "bootstrap",
    "tailwind",
    "react",
    "redux",
    "next.js",
    "vue",
    "angular",
    "vite",
    "node.js",
    "express",

    # ==========================
    # Python Frameworks
    # ==========================

    "flask",
    "django",
    "fastapi",
    "streamlit",
    "sqlalchemy",

    # ==========================
    # Databases
    # ==========================

    "sql",
    "mysql",
    "postgresql",
    "sqlite",
    "mongodb",
    "redis",
    "firebase",
    "oracle",
    "supabase",

    # ==========================
    # Version Control
    # ==========================

    "git",
    "github",
    "gitlab",
    "github actions",

    # ==========================
    # Cloud & DevOps
    # ==========================

    "docker",
    "kubernetes",
    "aws",
    "azure",
    "gcp",
    "terraform",
    "nginx",
    "linux",
    "ci/cd",

    # ==========================
    # Data Science
    # ==========================

    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "plotly",
    "scikit-learn",
    "tensorflow",
    "keras",
    "pytorch",
    "opencv",
    "xgboost",
    "lightgbm",

    # ==========================
    # AI / Machine Learning
    # ==========================

    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data analysis",
    "nlp",
    "spacy",
    "nltk",
    "computer vision",
    "llm",
    "transformers",
    "huggingface",
    "langchain",
    "llamaindex",
    "crewai",
    "autogen",
    "ollama",

    # ==========================
    # Data Engineering
    # ==========================

    "spark",
    "hadoop",
    "airflow",

    # ==========================
    # APIs & Tools
    # ==========================

    "rest api",
    "graphql",
    "grpc",
    "postman",
    "figma",
    "jupyter",
    "pycharm",
    "vscode",
    "npm",
    "webpack"
]


def extract_skills(text):
    """
    Returns a list of all common skills
    found in the given text.
    """

    text = text.lower()

    detected_skills = []

    for skill in COMMON_SKILLS:
        if skill in text:
            detected_skills.append(skill)

    return detected_skills