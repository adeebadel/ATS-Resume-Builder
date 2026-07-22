import os


class Config:
    """
    CareerAI Configuration
    """

    # ---------------------------------
    # Flask
    # ---------------------------------

    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "careerai-secret-key"
    )

    DEBUG = False

    # ---------------------------------
    # Uploads
    # ---------------------------------

    BASE_DIR = os.path.abspath(
        os.path.dirname(__file__)
    )

    UPLOAD_FOLDER = os.path.join(
        BASE_DIR,
        "static",
        "uploads"
    )

    MAX_CONTENT_LENGTH = 5 * 1024 * 1024

    ALLOWED_EXTENSIONS = {
        "pdf",
        "docx"
    }

    # ---------------------------------
    # Security
    # ---------------------------------

    SESSION_COOKIE_HTTPONLY = True

    SESSION_COOKIE_SAMESITE = "Lax"