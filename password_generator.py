import random
import chars
#generates a random password based on the character sets defined in chars.py
def random_password(min_length=10,max_length=16):
    password = ''
    # length of the password will be randomly chosen based on the min length and max lenght set in the parameters
    length = random.randint(min_length, max_length)
    for i in range(length):
        password += random.choice(chars.password_string)
    return password

if __name__ == "__main__":
    print(random_password())