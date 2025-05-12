
A Python package for validating various patterns such as phone numbers, emails, and passwords.

# Installation

bash
pip install pattern-checker

# Usage

from pattern_checker import CheckPattern

## Initialize with a value
checker = CheckPattern("09123456789")

## Check Iranian Phone Number
print(checker.check_iranian_phone())  # True

## Check Email
checker = CheckPattern("example@email.com")
print(checker.check_email_pattern())  # True

# Contributing
Pull requests are welcome. For major changes,
please open an issue first to discuss what you
would like to change.
