from admin_features import add_student, get_student, update_student, delete_student, upload_task, class_recording

def admin_panel():
    while True:
        print("\n===================================================")
        print("             ADMIN PANEL")
        print("=====================================================")
        print("1. Add Student")
        print("2. Get Student")
        print("3. Update Studeent")
        print("4. Delete Student")
        print("5. Upload Tasks")
        print("6. Class Recordings")
        print("7. Exit/ Go Back")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            get_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            upload_task()
        elif choice == '6':
            class_recording()
        elif choice == '7':
            break
        else:
            print("Invalid choice, Try Again.")