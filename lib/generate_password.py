"""
Python file to generate a random password from the password.json file.
"""
import json
import random


def generate_password():
    with open('passwords.json', 'r') as file:
        compromised_passwords = json.load(file)
    return random.choice(compromised_passwords)
