import expenses

while True:
    print("1. add expense\n2. view expenses\n3. view expense by category\n4. total spent\n5. exit")
    user_choice = input("Choose and option ")
    if user_choice == "1":
        expenses.add_expense()
    elif user_choice == "2":
        expenses.view_expenses()
    elif user_choice == "3":
        expenses.view_by_category()
    elif user_choice == "4":
        expenses.total_spent()
    elif user_choice == "5":
        print("goodbye!")
        break
    else:
        print("invalid choice")


