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
    with open(expenses_file, 'w') as file:
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

def view_expenses():
    #displays all expenses
    expenses = load_expenses()
    for expense in expenses:
        print(f"{expense['id']} - {expense['name']} - ${expense['amount']} - {expense['category']} - {expense['date']}")
    
def view_by_category():
    #displays expenses by category
    expenses = load_expenses()
    category = input("Enter category to filter by: ")
    for expense in expenses:
        if expense['category'].lower() == category.lower():
            print(f"{expense['id']} - {expense['name']} - ${expense['amount']} - {expense['date']}")

def total_spent():
    #calculates total amount spent and category specific totals
    expenses = load_expenses()
    total = sum(expense['amount'] for expense in expenses)
    category_total = {}
    for expense in expenses:
        cat = expense['category']
        if cat in category_total:
            category_total[cat] += expense['amount']
        else:
            category_total[cat] = expense['amount']
    for category, amount in category_total.items():
        print(f"{category}: ${amount:.2f}")
    print(f"\nTotal spent: ${total:.2f}")
