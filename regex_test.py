import re

text = """
John Doe
Email: john.doe@gmail.com
Phone: +91 9876543210
"""

if re.search(r"\S+@\S+\.\S+", text):
    print("Email Found")
else:
    print("Email Not Found")