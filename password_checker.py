# Password Strength Checker

import re

def check_password_strength(password):
    # Conditions for password rules
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[@$!%*?&]", password) is None

    # Count how many rules are broken
    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    score = errors.count(True)

    # Decide strength based on score
    if score == 0:
        return "Strong password ✅"
    elif score <= 2:
        return "Medium password ⚠️"
    else:
        return "Weak password ❌"

# Ask user for input
password = input("Enter a password to check: ")
print(check_password_strength(password))
