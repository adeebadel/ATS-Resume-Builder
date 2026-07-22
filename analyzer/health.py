"""
Resume Health Module
--------------------
Converts an ATS score into a human-readable
resume health label and color.
"""


def get_resume_health(score):
    """
    Returns a dictionary containing the
    resume health label and color.

    Args:
        score (int): Resume ATS score (0-100)

    Returns:
        dict
    """

    if score >= 90:
        return {
            "label": "🟢 Excellent Resume",
            "color": "#16a34a"
        }

    elif score >= 75:
        return {
            "label": "🔵 Good Resume",
            "color": "#2563eb"
        }

    elif score >= 60:
        return {
            "label": "🟠 Average Resume",
            "color": "#f97316"
        }

    else:
        return {
            "label": "🔴 Needs Improvement",
            "color": "#dc2626"
        }