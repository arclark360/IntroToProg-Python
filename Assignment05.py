# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dict and exceptions to work with data
# Change Log: (Who, When, What)
#   Alexander Reese Clark,11/13/2023,Updating Registration Program with Dict and Error Handling
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = """
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
"""
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
student_first_name: str = ""  # Holds the first name of a student entered by the user.
student_last_name: str = ""  # Holds the last name of a student entered by the user.
course_name: str = ""  # Holds the name of a course entered by the user.
csv_data: str = ""  # Holds combined string data separated by a comma.
file_obj = None  # Holds a reference to an opened file.
menu_choice: str = ""  # Hold the choice made by the user.
student_data: dict[str, str, str]  # Holds a dictionary value of student information for the JSON
students: list[dict[str, str, str]] = []  # Holds the list of dictionary's for the JSON

# At the start of the program it reads the json file and stores the student info.  If a file does not exist an error
# check will create the file for the user.  If the file is in the wrong format it will notify the user to check the
# file.
while True:
    try:
        file_obj = open(FILE_NAME, "r")
        students = json.load(file_obj)
        break
    except FileNotFoundError as e:
        print("JSON File not found, creating JSON file")
        file_obj = open(FILE_NAME, "w")
        json.dump(students, file_obj)
    except json.JSONDecodeError as e:
        print("File is not in right format and can't load students, please review file for error")
        break
    except Exception as e:
        print("Undefined Error")
        print(e, e.__doc__, type(e), sep="\n")
        break
    finally:
        file_obj.close()

# Begins the while loop for the program and won't close till option 4 is chosen
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Option 1 Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        # While loop and error handling to ensure user enters an accurate first name
        while True:
            try:
                student_first_name = input("Enter the student's first name: ")
                if not student_first_name.isalpha():
                    raise ValueError("first name must be alphabetic")
                break
            except ValueError as e:
                print(e)
        # While loop and error handling to ensure user enters an accurate last name
        while True:
            try:
                student_last_name = input("Enter the student's last name: ")
                if not student_last_name.isalpha():
                    raise ValueError("last name must be alphabetic")
                break
            except ValueError as e:
                print(e)
        course_name = input("Please enter the name of the course: ")
        # Stores user input as a dictionary item in the students list
        student_data = {"first_name": student_first_name, "last_name": student_last_name, "course_name": course_name}
        students.append(student_data)
        continue

    # Option 2 Present the current data of both the list and a string version of the list
    elif menu_choice == "2":
        print("\nThe current data is:")
        print(f"List Data: {students}")
        print("String Format:")
        for single_student in students:
            print(f"{single_student["first_name"]},{single_student["last_name"]},{single_student["course_name"]}")
        continue

    # Option 3 Save the data to a file
    elif menu_choice == "3":
        # Error handling setup to catch any errors that might occur when writing to the file that will notify the user
        # an error occurred and the data wasn't saved
        try:
            file_obj = open(FILE_NAME, "w")
            json.dump(students, file_obj)
            file_obj.close()
            for single_student in students:
                print(
                    f"You have registered {single_student["first_name"]} {single_student["last_name"]} for {single_student["course_name"]}.")
            continue
        except Exception as e:
            print("Undefined Error Data was not saved")
            print(e, e.__doc__, type(e), sep="\n")

    # Option 4 Stop the loop
    elif menu_choice == "4":
        break

    # Option 5 Catch-all
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
