"""
Python File to write top 100,000 pwned passwords to a password JSON file.
"""
import requests
import json

# URL source
url = "https://www.ncsc.gov.uk/static-assets/documents/PwnedPasswordsTop100k.json"
file_path = '/lib/passwords.json'

def write_json():
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        compromised_passwords = []


        for i, entry in enumerate(data):
            compromised_passwords.append(entry)

        with open('passwords.json', 'w') as file:
            json.dump(compromised_passwords, file, indent=4)

        return "Passwords have been written to passwords.json"

    else:
        return f"Failed to retrieve data: {response.status_code}"