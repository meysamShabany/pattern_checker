
A Python package for validating various patterns such as phone numbers, emails, and passwords.

# Installation

pip install pattern-checker

# Usage

from pattern_checker import CheckPattern


checker = CheckPattern("09123456789")

print(checker.check_iranian_phone())  # return True


checker = CheckPattern("example@email.com")

print(checker.check_email_pattern())  # return True

# Contributing
Pull requests are welcome. For major changes,
please open an issue first to discuss what you
would like to change.
