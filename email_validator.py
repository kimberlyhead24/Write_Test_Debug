import re
def validate(email):
    pattern = "^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)*@[^@.]+(\.[^@.]+)*\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None
