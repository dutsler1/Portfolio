import functions

print("Welcome to the Basic Calculator!")
#while true will create a infinite loop so the user can keep using the calculator until they select opton 6 to exit
while True:
    print("select the operation you intend to do: ")
    print("1 for addition ")
    print("2 for subtraction ")
    print("3 for multiplication ")
    print("4 for division ")
    print("5 for power ")
    print("6 to exit ")
    # gets the user input to select which operation to perform 
    user_input = input("Enter choice(1/2/3/4/5/6): ")
    if user_input =='6':
        print("goodbye")
        # if user selects 6 the loop will end and program will exit
        break
    elif user_input in ('1','2','3','4','5'):
        # gets 2 numbers from the user by utilizing float to allow for decimal points
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if user_input =='1':
            print(functions.add(num1, num2))
        elif user_input =='2':
            print(functions.subtract(num1, num2))
        elif user_input =='3':
            print(functions.multiply(num1, num2))
        elif user_input == '4':
            print(functions.divide(num1, num2))
        elif user_input == '5':
            print(functions.power(num1, num2))
   #if user inputs anything other than valid options program prints invalid input
    else:
        print("Invalid Input")


