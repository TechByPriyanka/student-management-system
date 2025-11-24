import pymysql

def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        database="student",
        password="root",
        cursorclass=pymysql.cursors.DictCursor
    ) 

# import pymysql

# conn= pymysql.connect(
#         host="localhost",
#         user="root",
#         database="student",
#         password="root"
#     ) 
# print("Connected to MySQL...")