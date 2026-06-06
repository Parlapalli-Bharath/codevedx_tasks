# Student Management System

students = []

def add_student():
    roll_no = input("Enter Roll Number: ")

    # Check if roll number already exists
    for student in students:
        if student["roll_no"] == roll_no:
            print("Student with this Roll Number already exists!")
            return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    students.append({
        "roll_no": roll_no,
        "name": name,
        "age": age,
        "course": course
    })

    print("Student added successfully!\n")


def view_students():
    if not students:
        print("No student records found.\n")
        return

    print("\n--- Student Records ---")
    for student in students:
        print(f"Roll No : {student['roll_no']}")
        print(f"Name    : {student['name']}")
        print(f"Age     : {student['age']}")
        print(f"Course  : {student['course']}")
        print("-" * 25)


def search_student():
    roll_no = input("Enter Roll Number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found:")
            print(f"Roll No : {student['roll_no']}")
            print(f"Name    : {student['name']}")
            print(f"Age     : {student['age']}")
            print(f"Course  : {student['course']}")
            return

    print("Student not found!\n")


def update_student():
    roll_no = input("Enter Roll Number to update: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("Leave blank to keep existing value.")

            name = input(f"New Name ({student['name']}): ")
            age = input(f"New Age ({student['age']}): ")
            course = input(f"New Course ({student['course']}): ")

            if name:
                student["name"] = name
            if age:
                student["age"] = age
            if course:
                student["course"] = course

            print("Student updated successfully!\n")
            return

    print("Student not found!\n")


def delete_student():
    roll_no = input("Enter Roll Number to delete: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student deleted successfully!\n")
            return

    print("Student not found!\n")


def menu():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Thank you for using Student Management System!")
            break
        else:
            print("Invalid choice! Please try again.")


# Start Program
menu()
