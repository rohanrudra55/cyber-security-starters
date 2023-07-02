#!/usr/local/bin/python3
import random

def generate_password(n):
    """Generate a password with n digits."""
    password = ''.join(random.choices('0123456789', k=n))
    return password


def generate_unique_passwords(n, y):
    """Generate y number of unique passwords with n digits."""
    passwords = set()
    while len(passwords) < y:
        password = generate_password(n)
        passwords.add(password)
    return passwords


def create_password_file(filename,n,y):
    """Write passwords to a file, each on a new line."""
    # Generate unique passwords
    passwords = generate_unique_passwords(n, y)
    with open(filename, 'w') as file:
        for password in passwords:
            file.write(password + '\n')

if __name__ == '__main__':
    # Usage example
    n = 5  # Number of digits in each password
    y = 1000  # Number of passwords to generate
    filename = 'ZIPpasswords.txt'

    create_password_file(filename, n, y)
    print(f"{y} passwords with {n} digits each have been created in the file '{filename}'.")