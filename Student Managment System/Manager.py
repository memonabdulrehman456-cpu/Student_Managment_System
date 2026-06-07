import os 
from Student import student as std
from datetime import datetime as dt
def log_function(func):
    def wrapper(*args, **kwargs):
        with open("log.txt", "a") as log_file:
            log_file.write(f"{dt.now()}: Called function '{func.__name__}'\n")
        return func(*args, **kwargs)
    return wrapper
class manager:
    def __init__(self ,filename="students.txt"):
        self.filename=filename
    @log_function
    def get_next_roll(self):
        if not os.path.exists(self.filename):
            return 1
        with open(self.filename, "r") as file:
            lines = file.readlines()
            return len(lines) + 1
    @log_function
    def add_student(self, name, fname, phone):
        roll = self.get_next_roll()
        student_obj = std(roll, name, fname, phone)
        with open(self.filename, "a") as file:
            file.write(str(student_obj) + "\n")
            print("Student added successfully!")
    @log_function
    def view_students(self):
        if not os.path.exists(self.filename):
            print("No students found.")
            return
        with open(self.filename, "r") as file:
            students = file.readlines()
            if not students:
                print("No students found.")
                return
            print("\n=== Student List ===\n")
            for student in students:
                student_info = student.strip().split(",")
                print(f"Rollno:{student_info[0]}")
                print(f"Name:{student_info[1]}")
                print(f"Father's Name:{student_info[2]}")
                print(f"Phone:{student_info[3]}")
    @log_function
    def search_student(self, roll):

        if not os.path.exists(self.filename):

            print("No data found!")
            return

        with open(self.filename, "r") as f:

            data = f.readlines()

        found = False

        for line in data:

            student_data = line.strip().split(",")

            if int(student_data[0]) == roll:

                print("\n===== Student Found =====")

                print("Roll Number :", student_data[0])
                print("Name        :", student_data[1])
                print("Father Name :", student_data[2])
                print("Phone       :", student_data[3])

                found = True
                break

        if not found:

            print("Student not found!")

    

    @log_function
    def update_student(self, roll, name, fname, phone):

        if not os.path.exists(self.filename):

            print("No data found!")
            return

        with open(self.filename, "r") as f:

            data = f.readlines()

        new_data = []

        found = False

        for line in data:

            student_data = line.strip().split(",")

            if int(student_data[0]) == roll:

                updated_line = f"{roll},{name},{fname},{phone}\n"

                new_data.append(updated_line)

                found = True

            else:

                new_data.append(line)

        with open(self.filename, "w") as f:

            f.writelines(new_data)

        if found:

            print("Student updated successfully!")

        else:

            print("Student not found!")

    

    @log_function
    def delete_student(self, roll):

        if not os.path.exists(self.filename):

            print("No data found!")
            return

        with open(self.filename, "r") as f:

            data = f.readlines()

        new_data = []

        found = False

        for line in data:

            student_data = line.strip().split(",")

            if int(student_data[0]) == roll:

                found = True
                continue

            new_data.append(line)

        with open(self.filename, "w") as f:

            f.writelines(new_data)

        if found:

            print("Student deleted successfully!")

        else:

            print("Student not found!")   