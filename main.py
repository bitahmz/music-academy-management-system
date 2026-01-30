from database import create_tables
from student import Student
from teacher import Teacher
from enrollment import Enrollment
from schedule import Schedule

def show_menu():
    print("\n--- Music Academy Management System ---")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Add Teacher")
    print("4. Show Teachers")
    print("5. Enroll Student")
    print("6. Exit")
    print("7.Show weekly schedule")
    print("8.Add class to schedule")

create_tables()
schedule = Schedule() 
schedule.load_from_file()

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Student name: ")
        phone = input("Phone number: ")
        instrument = input("Instrument: ")

        student = Student(name, phone, instrument)
        student.save()
        print("✔ Student added successfully")

    elif choice == "2":
        students = Student.get_all()
        for s in students:
            print(f"ID: {s[0]} | Name: {s[1]} | Phone: {s[2]} | Instrument: {s[3]}")

    elif choice == "3":
        name = input("Teacher name: ")
        instrument = input("Instrument: ")

        teacher = Teacher(name, instrument)
        teacher.save()
        print("✔ Teacher added successfully")

    elif choice == "4":
        teachers = Teacher.get_all()
        for t in teachers:
            print(f"ID: {t[0]} | Name: {t[1]} | Instrument: {t[2]}")

    elif choice == "5":
        student_id = input("Student ID: ")
        teacher_id = input("Teacher ID: ")

        enrollment = Enrollment(student_id, teacher_id)
        enrollment.save()
        print("✔ Enrollment completed")

    elif choice == "6":
        print("Exiting program...")
        break

    elif choice == "7":
        schedule.show_schedule()

    elif choice == "8":
     print("Days:")
    for i, d in enumerate(schedule.days):
        print(f"{i}. {d}")

    day = int(input("Select day (0-4): "))

    print("Time slots:")
    for i, t in enumerate(schedule.times):
        print(f"{i}. {t}")

    time = int(input("Select time (0-3): "))
    info = input("Enter class info (Student - Instrument - Teacher): ")

    schedule.add_class(day, time, info)
    schedule.save_to_file()
    print("Class added and saved.")
else:
    print("❌ Invalid choice")
