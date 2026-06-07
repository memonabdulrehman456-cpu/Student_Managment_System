from Student import student as std
from Manager import manager as mng
manager = mng()
while True:
    print("\n==== Student Management System ====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        roll = manager.get_next_roll()
        name = input("Enter student name: ")
        fname = input("Enter father's name: ")  
        phone = int(input("Enter phone number: "))
        manager.add_student(name, fname, phone)
    elif choice == '2':
        manager.view_students()
    elif choice == '3':
        try:
            rollno = int(input("Enter roll number to search: "))
            manager.search_student(rollno)
        except ValueError:
            print("Invalid input. Please enter a valid roll number.")
    elif choice == '4':
        try:
            rollno = int(input("Enter roll number to update: "))
            name = input("Enter new student name: ")
            fname = input("Enter new father's name: ")
            phone = int(input("Enter new phone number: "))
            manager.update_student(rollno, name, fname, phone)
        except ValueError:
            print("Invalid input. Please enter a valid roll number.")
    elif choice == '5':
        try:
            rollno = int(input("Enter roll number to delete: "))
            manager.delete_student(rollno)
        except ValueError:
            print("Invalid input. Please enter a valid roll number.")
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
        