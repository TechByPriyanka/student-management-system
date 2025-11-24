from db_connection import get_db_connection

#----Feature 1: ADD STUDENT ----
def add_student():
    print("\n--- Add New Student ---")
    try:
        st_id = int(input("Enter Student ID: "))
        st_name = input("Enter Student Name: ")
        st_age = int(input("Enter Student Age: "))  
        st_year = int(input("Enter year: "))
        st_dept = input("Enter Department: ")

        #2. conn to db
        conn = get_db_connection()
        cursor = conn.cursor()

        #3. write query and execute
        sql_query = "INSERT INTO student (s_id, s_name, s_age, s_year, s_dept) VALUES (%s,%s,%s,%s,%s)" 
        values = (st_id, st_name, st_age, st_year, st_dept)
        cursor.execute(sql_query, values)
        #cursor.execute("INSERT INTO student (stu_admNo, stu_name, stu_age, stu_year, stu_dept) VALUES (%s,%s,%s,%s,%s)", (s_id, s_name, s_age, s_year, s_dept))

        #4. Save changes
        conn.commit()
        print("Success: Student added to database!")
    
    except Exception as e:
        #print(f"Error: Something went wrong: {e}")
        print("Error Details --", e)
    finally:
        #5. Close connection
        if 'conn' in locals() and conn.open:
            cursor.close()
            conn.close()

#-----Feature 2: GET STUDENT ------
def get_student():
    print("\n--- Get Student Details---")
    try:
        search_id = int(input("Enter Student Id to search: "))

        #2. conn to db
        conn = get_db_connection()
        cursor = conn.cursor()

        #3. write query and execute
        sql_query = "SELECT * FROM student WHERE s_id = %s" 
        cursor.execute(sql_query,(search_id,))
        data = cursor.fetchone()

        if data:
            print("\n STUDENT FOUND:")
            print(f"ID: {data['s_id']}")
            print(f"Name: {data['s_name']}")
            print(f"Age: {data['s_age']}")
            print(f"Year: {data['s_year']}")
            print(f"Dept: {data['s_dept']}")
        else:
            print("No student found with that ID.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        #5. Close connection
        if 'conn' in locals() and conn.open:
            cursor.close()
            conn.close()   

#-----Feature 3: UPDATE STUDENT ------
def update_student():
    print("\n--- Update Student ---")
    try:
        update_id = int(input("Enter Student ID to update his/her details: "))

        print("What do you want to update?")
        print("1. Name")
        print("2. Age")
        print("3. Year")
        print("4. Department")
        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            new_value = input("Enter new name: ")
            sql = "UPDATE STUDENT SET s_name = %s where s_id = %s"
        elif choice == 2:
            new_value = input("Enter new Age: ")
            sql = "UPDATE STUDENT SET s_age = %s where s_id = %s"
        elif choice == 3:
            new_value = input("Enter new Year: ")
            sql = "UPDATE STUDENT SET s_year = %s where s_id = %s"
        elif choice == 4:
            new_value = input("Enter new Department: ")
            sql = "UPDATE STUDENT SET s_dept = %s where s_id = %s"
        else:
            print("Invalid choice.")

        conn = get_db_connection()
        cursor = conn.cursor()
        values = (new_value, update_id)
        cursor.execute(sql, values)
        conn.commit()

        if cursor.rowcount > 0:
            print("Success: Student Details Updated!")
        else:
            print("Error: Student ID not found.")

    except Exception as e:
        print(f"Error: Something went wrong: {e}")
    # finally:
        # if 'cursor' in locals and cursor:
        #     cursor.close()
        # if 'conn' in locals and conn:
        #     conn.close()

#-----Feature 4: DELETE STUDENT ------
def delete_student():
    print("\n--- Delete Student ---")
    try:
        delete_id =int(input("Enter Student ID to delete: "))
        conn = get_db_connection()
        cursor = conn.cursor()

        sql = "DELETE FROM student where s_id = %s"
        cursor.execute(sql,(delete_id))
        conn.commit()

        if cursor.rowcount>0:
            print("Success: Student deleted successfully.")
        else:
            print("ID not found, nothing deleted.")

    except Exception as e:
        print(f"Something went wrong: {e}")
    # finally:
    #     if 'cursor' in locals and cursor:
    #         cursor.close()
    #     if 'conn' in locals and conn:
    #         conn.close()

#-----Feature 5: UPLOAD TASK ------

def upload_task():
    print("\n--- Upload Task ---")
    try:
        task_id = int(input("Enter Task ID: "))
        task_topic = input("Enter Task Name: ")
        task_doc = input("Enter Task link: ")
        task_issued_date = input("Enter issued date (YYYY-MM-DD): ")
        
        #2. conn to db
        conn = get_db_connection()
        cursor = conn.cursor()

        #3. write query and execute
        sql_query = "INSERT INTO tasks (task_id, task_topic, task_doc, task_issued_date) VALUES (%s,%s,%s,%s)" 
        values = (task_id, task_topic, task_doc, task_issued_date)
        cursor.execute(sql_query, values)

        #4. Save changes
        conn.commit()
        print("Success: Task uploaded in database!")
    
    except Exception as e:
        print("Error Details --", e)
    finally:
        #5. Close connection
        if 'conn' in locals() and conn.open:
            cursor.close()
            conn.close()

#-----Feature 6: UPLOAD TASK RECORDING ------

def task_recording():
    print("\n--- Add Task Recording ---")
    try:
        r_id = int(input("Enter Recording ID: "))
        r_topic = input("Enter Recording Name: ")
        r_link = input("Enter Recording link: ")
        
        #2. conn to db
        conn = get_db_connection()
        cursor = conn.cursor()

        #3. write query and execute
        sql_query = "INSERT INTO recordings (r_id, r_topic, r_link) VALUES (%s,%s,%s)" 
        values = (r_id, r_topic, r_link)
        cursor.execute(sql_query, values)

        #4. Save changes
        conn.commit()
        print("Success: Recording added to database!")
    
    except Exception as e:
        #print(f"Error: Something went wrong: {e}")
        print("Error Details --", e)
    finally:
        #5. Close connection
        if 'conn' in locals() and conn.open:
            cursor.close()
            conn.close()