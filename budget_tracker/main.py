import expenses
print("Add your expenses here!")
print("1. add expense\n2. view expenses'n3.view expense by category\n4. total spent")
user_choice = input("Choose and option")
while True:
    if user_choice == "1":
        expenses.add_expense()
    elif user_choice == "2":
        expenses.view_expenses()
    elif user_choice == "3":
        expenses.view_by_category()
    elif user_choice == "4":
        expenses.total_spent()
    else:
        print("invalid choice")


