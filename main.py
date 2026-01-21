import chars
import password_generator

print("Create a password between 10 and 16 characters using 1 uppercase letter, 1 lowercase letter and one special character:")
print("if you would like to auto generate a password type Y")

user_password = input("Enter your password or Y to auto generate: ")
if user_password.upper() == 'Y':
    print("Your generated password is:" , password_generator.random_password())
else:
    print("incorrect")