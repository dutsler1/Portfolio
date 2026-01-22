import functions

print("Welcome to the Basic Calculator!")

while True:
    print("select the operation you intend to do: ")
    print("1 for addition ")
    print("2 for subtraction ")
    print("3 for multiplication ")
    print("4 for division ")
    print("5 for power ")
    print("6 to exit ")
    user_input = input("Enter choice(1/2/3/4/5/6): ")
    if user_input =='6':
        print("goodbye")
        break
    elif user_input in ('1','2','3','4','5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
