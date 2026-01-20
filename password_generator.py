import random
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
DIGITS = '0123456789'
SPECIAL_CHARACTERS = '!@#$%^&*()-_=+[]{}|;:,.<>?/'
password_string = LOWERCASE_LETTERS + UPPERCASE_LETTERS + DIGITS + SPECIAL_CHARACTERS

def random_password(min_length=10,max_length=16):
    #generates a random password
    password_string = LOWERCASE_LETTERS + UPPERCASE_LETTERS + DIGITS + SPECIAL_CHARACTERS
    password = ''
    length = random.randint(min_length, max_length)
    for i in range(length):
        password += random.choice(password_string)
    return password

if __name__ == "__main__":
    print(random_password())