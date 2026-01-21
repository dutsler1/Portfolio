import chars
import password_generator
print("Create a password between 10 and 16 characters using 1 uppercase letter, 1 lowercase letter and one special character:")
print("if you would like to auto generate a password type Y")

user_password = input("Enter your password or Y to auto generate:")
#if lowercase is used it will still be accepted
if user_password.upper() == 'Y':
    print("Your generated password is:" , password_generator.random_password())
#ensures the password meets the length requirements of 10-16 characters
elif chars.min_length > len(user_password):
    print("password must be at least 10 characters")
elif chars.max_length < len(user_password):
    print("password must be less than 16 characters")
#checks to make sure password contains special characters, uppercase and lowercase letters
elif not any(char in chars.SPECIAL_CHARACTERS for char in user_password):
    print("password must contain a special character")
elif not any(char in chars.UPPERCASE_LETTERS for char in user_password):
    print("password must contain one uppercase letter")
elif not any(char in chars.LOWERCASE_LETTERS for char in user_password):
    print("password must contain one lowercase letter")
else:
    print(user_password, "is a valid password")
