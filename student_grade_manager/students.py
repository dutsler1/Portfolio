import json
import os
import grades
students_file = 'students.json'

def load_students():
    if os.path.exists(students_file):
        try:
            with open(students_file, 'r') as file:
                return json.load(file)
        except:
            return []
    else:
        return []
    
def save_students(students):
    with open(students_file, 'w') as file:
        json.dump(students, file)

def add_student():
    students = load_students()
    name = input("Enter student name: ")
    student_id = students[-1]["id"] + 1 if students else 1
    new_student = {
        "id": student_id,
        "name": name,
        "grades": {}
    }
    students.append(new_student)
    students.sort(key=lambda student: student['name'])
    save_students(students)

def view_all_students():
    students = load_students()
    if not students:
        print("No students found.")
        return
    for student in students:
        print(f"({student['id']}) {student['name']} - Grades: {student['grades']}")
    
#def sort_students_by_grade()
#def remove_student()