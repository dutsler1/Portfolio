import json
import os
TASKS_FILE = 'tasks.json'

def load_tasks():
    #this function will read tasks from file or return an empty list if file doesnt exist
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r') as file:
                return json.load(file)
        except:
            return []
    else:
        return []
def save_tasks(tasks):
    #this function saves the task to a file
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)
def add_task():
    #this function will add a new task to the list
    tasks = load_tasks()
    name = input("Enter task name: ")
    new_id = tasks[-1]["id"] + 1 if tasks else 1
    new_task = {
        "id": new_id,
        "name": name,
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    

    
def complete_task():
    #this function will mark tasks as completed
    pass
def delete_task():
    #this function will delete a task from the list 
    pass