

students = {}   # Main dictionary to store student data


# 1. Add Student
def add_student(student_id, name, subjects):
    if student_id in students:
        print("Student ID already exists!")
    else:
        students[student_id] = {
            "name": name,
            "subjects": set(subjects)    # Store subjects in a set
        }
        print("Student added successfully!")


# 2. Display All Students
def display_students():
    if not students:
        print("No students found.")
        return
    
    for sid, info in students.items():
        print("\nStudent ID:", sid)
        print("Name:", info["name"])
        print("Subjects:", ", ".join(info["subjects"]))


# 3. Search a Student
def search_student(student_id):
    if student_id in students:
        info = students[student_id]
        print("\nStudent found!")
        print("Name:", info["name"])
        print("Subjects:", ", ".join(info["subjects"]))
    else:
        print("Student not found!")



add_student("101", "Raksha", ["Maths", "Science", "English"])
add_student("102", "Anu", ["Kannada", "Maths"])

display_students()

search_student("101")
