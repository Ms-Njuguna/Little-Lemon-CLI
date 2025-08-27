import re

def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)

def validate_phone(phone):
    pattern = r"^\+?\d{7,15}$"
    return re.match(pattern, phone)