import json
import os
import students
grades_file = 'grades.json'

def load_grades():  
    if os.path.exists(grades_file):
        try:
            with open(grades_file, 'r') as file:
                return json.load(file)
        except:
            return {}
    else:
        return {}

def save_grades(grades):
    with open(grades_file, 'w') as file:
        json.dump(grades, file)

def letter_grade(score):
    if score > 100:
        print('Invalid score. Must be between 0 and 100.')
        return None
    elif score > 90 and score < 95:
        return 'A'
    elif score >= 95:
        return 'A+'
    elif score > 80 and score < 85:
        return 'B'
    elif score >= 85 and score <= 89:   
        return 'B+'
    elif score > 70 and score < 75:
        return 'C'
    elif score >= 75 and score <= 79:
        return 'C+'
    elif score > 60 and score < 65:
        return 'D'
    elif score >= 65 and score <= 69:
        return 'D+'
    elif score >= 0 and score <= 59:
        return 'F'
    else:        print('Invalid score. Must be between 0 and 100.')

def add_grade():
    students_list = students.load_students()
    if not students_list:
        print("Students must be added before adding a grade.")
        return
    