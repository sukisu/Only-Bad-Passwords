""" Python File to generate password JSON if it doesn't exist and then generates bad password"""
import os

from lib.generate_password import generate_password
from lib.get_json import write_json

file_path = '/lib/passwords.json'

def main():
    if not os.path.exists(file_path):
        write_json()
        password = generate_password()
        return password
    else:
        password = generate_password()
        return password

if __name__ == '__main__':
    print(main())

