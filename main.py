students = []

# Add Students
def add_student():
    student_id = input("Enter Student ID: ").strip()
    name = input("Enter Student Name: ").strip()

    try:
        age = int(input("Enter Student Age: "))
    except ValueError:
        print("Invalid age! Please enter a number.")
        return
    department = input("Enter Department: ").strip()
    level = input("Enter Level: ").strip()
    email = input("Enter your Email: ").strip()
    phone = input("Enter Phone Number: ").strip()

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "department": department,
        "level": level,
        "email": email,
        "phone": phone
    }
    students.append(student)
    print("Student Added Successfully!")

# View Student
def view_students():
    if not students:
        print("No Students found.")
        return
    print("\n===== Student List =====")

    for student in students:
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Department: {student['department']}")
        print(f"Level: {student['level']}")
        print(f"Email: {student['email']}")
        print(f"Phone: {student['phone']}")
        print("_" * 30)

# Find Student
def find_student():
    student_id = input("Enter Student ID: ")

    found = False

    for student in students:
        if student["id"] == student_id:
            print("\n===== Student Found =====")
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Department: {student['department']}")
            print(f"Level: {student['level']}")
            print(f"Email: {student['email']}")
            print(f"Phone: {student['phone']}")

            found = True
            break
    if not found:
         print(f"Student with ID {student_id} not found.")

# Update Student
def update_student():
       student_id = input("Enter Student ID: ")

       for student in students:
           if student["id"] == student_id:
               print("\n===== Update Student =====")
               print(f"ID: {student['id']}")
               print(f"Name: {student['name']}")
               print(f"Age: {student['age']}")

               new_name = input("Enter new name: ")
               new_age = int(input("Enter new age: "))

               student["name"] = new_name
               student["age"] = new_age

               print("Student Updated Successfully!.")
               return
       print(f"Student with ID {student_id} not found.")

# Delete
def delete_student():
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
         students.remove(student)
         print("Student deleted successfully!.")
         return

    print(f"Student with ID {student_id} not found.")

