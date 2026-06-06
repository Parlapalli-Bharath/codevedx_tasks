import os

FILE_NAME = "students.txt"

# Create File
def create_file():
    if not os.path.exists(FILE_NAME):
        open(FILE_NAME, "w").close()
        print("File created successfully.")
    else:
        print("File already exists.")

# Add Records
def add_record():
    with open(FILE_NAME, "a") as file:
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        file.write(f"{roll},{name},{marks}\n")

    print("Record added successfully.")

# View Records
def view_records():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()

            if not data:
                print("No records found.")
                return

            print("\n--- Student Records ---")
            for line in data:
                roll, name, marks = line.strip().split(",")
                print(f"Roll No: {roll}")
                print(f"Name   : {name}")
                print(f"Marks  : {marks}")
                print("-" * 25)

    except FileNotFoundError:
        print("File does not exist.")

# Search Record
def search_record():
    roll_no = input("Enter Roll Number to search: ")

    try:
        with open(FILE_NAME, "r") as file:
            found = False

            for line in file:
                roll, name, marks = line.strip().split(",")

                if roll == roll_no:
                    print("\nRecord Found")
                    print("Roll No:", roll)
                    print("Name   :", name)
                    print("Marks  :", marks)
                    found = True
                    break

            if not found:
                print("Record not found.")

    except FileNotFoundError:
        print("File does not exist.")

# Count Records
def count_records():
    try:
        with open(FILE_NAME, "r") as file:
            count = len(file.readlines())

        print("Total Records:", count)

    except FileNotFoundError:
        print("File does not exist.")

# Delete File
def delete_file():
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)
        print("File deleted successfully.")
    else:
        print("File not found.")

# Main Menu
while True:
    print("\n===== FILE HANDLING & DATA PROCESSING SYSTEM =====")
    print("1. Create File")
    print("2. Add Record")
    print("3. View Records")
    print("4. Search Record")
    print("5. Count Records")
    print("6. Delete File")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_file()

    elif choice == "2":
        add_record()

    elif choice == "3":
        view_records()

    elif choice == "4":
        search_record()

    elif choice == "5":
        count_records()

    elif choice == "6":
        delete_file()

    elif choice == "7":
        print("Program exited successfully.")
        break

    else:
        print("Invalid choice. Please try again.")
