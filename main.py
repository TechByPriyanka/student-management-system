from admin import admin_panel

print("\n**********************************************")
print(" Welcome to Student Management System ")
print("************************************************")

while True:
    print("\n who are you?")
    print("1. Admin")
    print("2. Student")
    print("3. Exit Program")

    role = input("Enter option (1-3): ")   

    if role == '1':
        admin_panel()
    elif role == '2':
        print("student_panel()")
    elif role == '3':
        print("Exiting the program.")
    else:
        print("Invalid option.")