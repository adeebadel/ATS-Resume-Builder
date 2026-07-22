"""
CareerAI Resume Parser
----------------------
Extracts text from PDF and DOCX resumes.
"""

import logging
import os

import pdfplumber
from docx import Document

logger = logging.getLogger(__name__)


def extract_text(file_path):
    """
    Detect file type and extract text.

    Args:
        file_path (str): Path to the uploaded resume.

    Returns:
        str: Extracted resume text.
    """

    if not os.path.exists(file_path):
        logger.error("File does not exist: %s", file_path)
        return ""

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return extract_pdf(file_path)

    if extension == ".docx":
        return extract_docx(file_path)

    logger.warning("Unsupported file type: %s", extension)
    return ""


def extract_pdf(file_path):
    """
    Extract text from a PDF file.
    """

    extracted_pages = []

    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    extracted_pages.append(page_text.strip())

    except Exception:
        logger.exception("Failed to parse PDF.")
        return ""

    return "\n".join(extracted_pages).strip()


def extract_docx(file_path):
    """
    Extract text from a DOCX file.
    """

    paragraphs = []

    try:
        document = Document(file_path)

        for paragraph in document.paragraphs:
            text = paragraph.text.strip()

            if text:
                paragraphs.append(text)

    except Exception:
        logger.exception("Failed to parse DOCX.")
        return ""

    return "\n".join(paragraphs).strip()