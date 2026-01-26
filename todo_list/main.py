import tasks


print("Welcome to your to do list")
print("select and option:")
print("1. Add a task\n2. Mark a task as complete\n3. Delete a task\n4. Exit menu")
#while true loops until the user exits program.
while True:
    choice = input("Enter your choice: ")
    if choice == '1':
        tasks.add_task()
    elif choice == '2':
        tasks.complete_task()
    elif choice == '3':
        tasks.delete_task()
    elif choice == '4':
        print('Goodbye!')
        break
    else:
        print("Invalid option, Try again.")
    