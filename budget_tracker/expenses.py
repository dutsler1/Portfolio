import json
import os
from datetime import datetime
expenses_file = 'expenses.json'
def load_expenses():
#this function will load functions from the JSON file
    if os.path.exists(expenses_file):
        try:
            with open(expenses_file, 'r') as file:
                return json.load(file)
        except:
            return []
    else:
        return []
def save_expenses(expenses):
    #this function will save expenses to the JSON file
    with open(expenses, 'w') as file:
        json.dump(expenses, file)
def add_expense():
    #this function allows a new expense to be added
    expenses = load_expenses()
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    new_id = expenses[-1]["id"] + 1 if expenses else 1
    expense_category = input("Enter expense category: ")
    date = datetime.now().strftime("%Y-%m-%d")
    new_expense = {
        "id": new_id,
        "name": name,
        "amount": amount,
        "category": expense_category,
        "date": date
    }
    expenses.append(new_expense)
    save_expenses(expenses)
    