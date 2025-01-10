import re


def validate_name(name):
    return name.isalpha()


def validate_contact(contact):
    return bool(re.fullmatch(r"\d{10}", contact))


def validate_email(email):
    return bool(re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email))


def validate_password(password):
    return bool(re.fullmatch(r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}", password))
