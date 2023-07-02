#!/usr/local/bin/python3
from tqdm import tqdm
import zipfile
import random
import concurrent.futures
from itertools import permutations

def generate_password(n):
    """Generate a password with n digits."""
    password = ''.join(random.choices('0123456789', k=n))
    return password


def generate_password_list(n, y):
    """Generate a list of passwords with n digits."""
    passwords = []
    perm = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], n)
    for i in list(perm)[:y]:
        passwords.append(str(''.join(map(str, i))))
    return passwords


def check_password(password, zip_file):
    try:
        zip_file.extractall(pwd=password.encode())
        return password
    except RuntimeError:
        return None


def decode(filename, y, n):
    try:
        zip_file = zipfile.ZipFile(filename)
    except:
        print("File not zip, exiting...\n")
        exit(0)
    passwords = generate_password_list(n, y)
    with tqdm(total=n, unit='password') as pbar:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(check_password, generate_password(y), zip_file) for _ in range(n)]
            # futures = [executor.submit(check_password, password, zip_file)
                    #    for password in passwords] # Not working

            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                pbar.update(1)
                if result:
                    pbar.close()
                    return result

    return 0


def main():
    protected_file = input("Zip file: ")
    y = int(input("Number of digits in the password: "))
    n = int(input("Number of passwords to check: "))
    print("\n\n")
    print("Password retrieved:", decode(protected_file, y, n))



if __name__ == '__main__':
    main()