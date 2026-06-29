"""
Student Record Management System

A menu-driven Python application that manages student records
using CSV and JSON files.

Author: Your Name
"""


# ==============================
# Import Required Libraries
# ==============================

import csv
import json
import logging
import os


# ==============================
# Logging Configuration
# ==============================

logging.basicConfig(
    filename="student_system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ==============================
# Custom Exceptions
# ==============================

class StudentExistsError(Exception):
    """
    Raised when a student registration number already exists.
    """
    pass


class StudentNotFoundError(Exception):
    """
    Raised when a student cannot be found.
    """
    pass


# ==============================
# File Names
# ==============================

CSV_FILE = "students.csv"
JSON_FILE = "students.json"


# ==============================
# Initialize Files
# ==============================

def initialize_files():

    try:

        # Create CSV file if it does not exist

        if not os.path.exists(CSV_FILE):

            with open(CSV_FILE, "w", newline="") as file:

                writer = csv.writer(file)

                writer.writerow(
                    [
                        "Registration Number",
                        "Name",
                        "Age",
                        "Gender"
                    ]
                )


        # Create JSON file if it does not exist

        if not os.path.exists(JSON_FILE):

            with open(JSON_FILE, "w") as file:

                json.dump({}, file)


        logging.info("System files initialized successfully.")


    except Exception as error:

        logging.error(
            f"File initialization error: {error}"
        )


    finally:

        print("System initialization completed.")



# ==============================
# JSON Functions
# ==============================

def load_json_data():

    try:

        with open(JSON_FILE, "r") as file:

            return json.load(file)


    except FileNotFoundError:

        return {}


    except json.JSONDecodeError:

        logging.error("JSON file is corrupted.")

        return {}



def save_json_data(data):

    with open(JSON_FILE, "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )



# ==============================
# Check Student Exists
# ==============================

def student_exists(reg_number):

    try:

        with open(CSV_FILE, "r") as file:

            reader = csv.DictReader(file)


            for student in reader:

                if student["Registration Number"] == reg_number:

                    return True


        return False


    except Exception as error:

        logging.error(
            f"Checking student error: {error}"
        )

        return False


# ==============================
# Save CSV Data
# ==============================

def save_csv_data(students):

    with open(CSV_FILE, "w", newline="") as file:

        fieldnames = [
            "Registration Number",
            "Name",
            "Age",
            "Gender"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(students)


# ==============================
# Add Student Function
# ==============================

def add_student():

    try:

        print("\n====== ADD NEW STUDENT ======")


        reg_number = input(
            "Enter registration number: "
        ).strip()

        if reg_number == "":
            raise ValueError(
                "Registration number cannot be empty."
            )

        
        if student_exists(reg_number):
            raise StudentExistsError(
                "Student already exists."
            )

        
        name = input(
            "Enter student name: "
        ).strip()


        if name == "":

            raise ValueError(
                "Name cannot be empty."
            )


        age = int(
            input("Enter age: ")
        )


        if age <= 0:

            raise ValueError(
                "Age must be greater than zero."
            )


        gender = input(
            "Enter gender: "
        ).strip()


        address = input(
            "Enter address: "
        ).strip()


        contact = input(
            "Enter contact: "
        ).strip()


        program = input(
            "Enter program: "
        ).strip()



        # Save basic details to CSV

        with open(
            CSV_FILE,
            "a",
            newline=""
        ) as file:


            writer = csv.writer(file)


            writer.writerow(
                [
                    reg_number,
                    name,
                    age,
                    gender
                ]
            )



        # Save additional details to JSON

        students = load_json_data()


        students[reg_number] = {

            "address": address,

            "contact": contact,

            "program": program

        }


        save_json_data(students)



        logging.info(
            f"Student {reg_number} added."
        )


        print(
            "\nStudent added successfully!"
        )


    except StudentExistsError as error:

        logging.error(str(error))

        print(error)



    except ValueError as error:

        logging.error(str(error))

        print(error)



    except Exception as error:

        logging.error(
            f"Unexpected error: {error}"
        )

        print(
            "An unexpected error occurred."
        )


    finally:

        print(
            "Add student operation completed."
        )


# ==============================
# View All Students
# ==============================

def view_students():

    try:

        print("\n====== ALL STUDENTS ======")

        students_extra = load_json_data()


        with open(CSV_FILE, "r") as file:

            reader = csv.DictReader(file)

            found = False


            for student in reader:

                found = True

                reg_number = student["Registration Number"]


                print("\n-------------------------")

                print(
                    "Registration Number:",
                    reg_number
                )

                print(
                    "Name:",
                    student["Name"]
                )

                print(
                    "Age:",
                    student["Age"]
                )

                print(
                    "Gender:",
                    student["Gender"]
                )


                # Display JSON details

                if reg_number in students_extra:

                    print(
                        "Address:",
                        students_extra[reg_number]["address"]
                    )

                    print(
                        "Contact:",
                        students_extra[reg_number]["contact"]
                    )

                    print(
                        "Program:",
                        students_extra[reg_number]["program"]
                    )


            if not found:

                print("No student records found.")


        logging.info(
            "Viewed all student records."
        )


    except FileNotFoundError:

        print(
            "Student files not found."
        )

        logging.error(
            "Student files missing."
        )


    except Exception as error:

        print(
            "An error occurred while viewing students."
        )

        logging.error(
            f"View students error: {error}"
        )


    finally:

        print(
            "View operation completed."
        )


# ==============================
# Search Student
# ==============================

def search_student():

    try:

        print("\n====== SEARCH STUDENT ======")


        reg_number = input(
            "Enter registration number: "
        ).strip()


        if reg_number == "":

            raise ValueError(
                "Registration number cannot be empty."
            )


        found_student = None


        with open(CSV_FILE, "r") as file:

            reader = csv.DictReader(file)


            for student in reader:

                if student["Registration Number"] == reg_number:

                    found_student = student

                    break



        if found_student is None:

            raise StudentNotFoundError(
                "Student record not found."
            )



        # Get extra details from JSON

        students_extra = load_json_data()



        print("\n-------------------------")

        print(
            "Registration Number:",
            found_student["Registration Number"]
        )

        print(
            "Name:",
            found_student["Name"]
        )

        print(
            "Age:",
            found_student["Age"]
        )

        print(
            "Gender:",
            found_student["Gender"]
        )



        if reg_number in students_extra:

            print(
                "Address:",
                students_extra[reg_number]["address"]
            )

            print(
                "Contact:",
                students_extra[reg_number]["contact"]
            )

            print(
                "Program:",
                students_extra[reg_number]["program"]
            )


        logging.info(
            f"Student {reg_number} searched successfully."
        )



    except StudentNotFoundError as error:

        print(error)

        logging.error(
            str(error)
        )


    except ValueError as error:

        print(error)

        logging.error(
            str(error)
        )


    except Exception as error:

        print(
            "An unexpected error occurred."
        )

        logging.error(
            f"Search error: {error}"
        )


    finally:

        print(
            "Search operation completed."
        )


# ==============================
# Update Student
# ==============================

def update_student():

    try:

        print("\n====== UPDATE STUDENT ======")


        reg_number = input(
            "Enter registration number: "
        ).strip()


        if reg_number == "":

            raise ValueError(
                "Registration number cannot be empty."
            )



        students = []


        found = False



        # Read CSV records

        with open(CSV_FILE, "r") as file:

            reader = csv.DictReader(file)


            for student in reader:


                if student["Registration Number"] == reg_number:

                    found = True


                    print(
                        "\nEnter new details:"
                    )


                    new_name = input(
                        "New name: "
                    ).strip()


                    new_age = int(
                        input("New age: ")
                    )


                    new_gender = input(
                        "New gender: "
                    ).strip()



                    student["Name"] = new_name

                    student["Age"] = new_age

                    student["Gender"] = new_gender



                students.append(student)




        if not found:

            raise StudentNotFoundError(
                "Student not found."
            )



        # Save updated CSV

        save_csv_data(students)



        # Update JSON details

        students_extra = load_json_data()



        if reg_number in students_extra:


            new_address = input(
                "New address: "
            ).strip()


            new_contact = input(
                "New contact: "
            ).strip()


            new_program = input(
                "New program: "
            ).strip()



            students_extra[reg_number] = {

                "address": new_address,

                "contact": new_contact,

                "program": new_program

            }


            save_json_data(
                students_extra
            )



        logging.info(
            f"Student {reg_number} updated successfully."
        )


        print(
            "Student updated successfully!"
        )



    except StudentNotFoundError as error:

        print(error)

        logging.error(
            str(error)
        )



    except ValueError as error:

        print(error)

        logging.error(
            str(error)
        )



    except Exception as error:

        print(
            "An error occurred while updating."
        )

        logging.error(
            f"Update error: {error}"
        )



    finally:

        print(
            "Update operation completed."
        )

# ==============================
# Delete Student
# ==============================

def delete_student():

    try:

        print("\n====== DELETE STUDENT ======")

        reg_number = input(
            "Enter registration number: "
        ).strip()


        if reg_number == "":

            raise ValueError(
                "Registration number cannot be empty."
            )


        students = []

        found = False



        # Read CSV and remove student

        with open(CSV_FILE, "r") as file:

            reader = csv.DictReader(file)


            for student in reader:

                if student["Registration Number"] == reg_number:

                    found = True

                else:

                    students.append(student)



        if not found:

            raise StudentNotFoundError(
                "Student record not found."
            )



        # Rewrite CSV without deleted student

        save_csv_data(students)



        # Remove JSON details

        students_extra = load_json_data()


        if reg_number in students_extra:

            del students_extra[reg_number]

            save_json_data(students_extra)



        logging.info(
            f"Student {reg_number} deleted successfully."
        )


        print(
            "Student deleted successfully!"
        )



    except StudentNotFoundError as error:

        print(error)

        logging.error(
            str(error)
        )



    except ValueError as error:

        print(error)

        logging.error(
            str(error)
        )



    except Exception as error:

        print(
            "An error occurred while deleting."
        )

        logging.error(
            f"Delete error: {error}"
        )


    finally:

        print(
            "Delete operation completed."
        )



# ==============================
# Main Menu
# ==============================

def main_menu():


    while True:


        print("\n================================")
        print(" STUDENT RECORD MANAGEMENT SYSTEM")
        print("================================")

        print("1. Add New Student")

        print("2. View All Students")

        print("3. Search Student")

        print("4. Update Student")

        print("5. Delete Student")

        print("6. Exit")


        choice = input(
            "Enter your choice: "
        )



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

            logging.info(
                "System closed."
            )
            

            print(
                "Goodbye!"
            )

            break



        else:

            print(
                "Invalid choice. Try again."
            )



# ==============================
# Program Execution
# ==============================


initialize_files()

main_menu()