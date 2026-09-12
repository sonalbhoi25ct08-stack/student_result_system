import csv
import os
FILE = "Student_results.csv"

def add_result():
    roll_num = input("Enter Roll No: ")
    name = input("Enter your name: ")
    course = input("Enter your course: ")
    print("Enter Subject Marks in between 0-100")
    m1 = int(input("marks 1: "))
    m2 = int(input("marks 2: "))
    m3 = int(input("marks 3: "))
    m4 = int(input("marks 4: "))
    m5 = int(input("marks 5: "))
    marks = [m1, m2, m3, m4, m5]
    return marks, course, roll_num, name

def calculate_result(marks, course, roll_num, name):
    total = sum(marks)
    percentage = total / 5
    if percentage >= 90: grade = "A Pass"
    elif percentage >= 75: grade = "B Pass"
    elif percentage >= 60: grade = "C Pass"
    elif percentage >= 40: grade = "D Pass"
    else: grade = "F Fail"
    print(f"\nRoll: {roll_num} | Name: {name} | Total: {total} | {percentage}% | {grade}")
    new = not os.path.exists(FILE)
    with open(FILE, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new: w.writerow(["Roll No","Name","Course","Total","Percentage","Grade"])
        w.writerow([roll_num,name,course,total,percentage,grade])

def get_result():
    roll = input("\nEnter Roll No: ")
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if row[0] == roll:
                    print(f"\nRoll: {row[0]}, Name: {row[1]}, Total: {row[3]}, Per: {row[4]}%, Grade: {row[5]}")
                    return
        print(" Invalid Roll No.")
    except FileNotFoundError:
        print("Data do not exist")

def show_all_data():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            for row in csv.reader(f):
                print(row)
    except FileNotFoundError:
        print("Data do not exist")


while True:
    print("\n -------STUDENT RESULT MANAGEMENT SYSTEM-------")
    print("1. Add Student Result")
    print("2. Get Student Result")
    print("3. Show All Student Result")
    print("4. Exit")
    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        n = int(input("Enter number of students: "))
        for i in range(n):
            marks, course, roll_num, name = add_result()
            calculate_result(marks, course, roll_num, name)
    elif choice == 2:
        get_result()
    elif choice == 3:
        show_all_data()
    elif choice == 4:
        break
    else:
        print("Invalid Choice")