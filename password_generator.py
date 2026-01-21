import random
import chars

def random_password(min_length=10,max_length=16):
    #generates a random password
    length = random.randint(min_length, max_length)
    for i in range(length):
        password += random.choice(password_string)
    return password

if __name__ == "__main__":
    print(random_password())