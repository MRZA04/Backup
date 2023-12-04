import sqlite3

# create a connection to the database
con = sqlite3.connect("Students.sqlite")

# create an instance of the cursor based on the connected database
cur = con.cursor()

def check_table_exist(table_name: str):
    """returns True if table name sent as arg exists"""
    # SQL statement checks counts number of table_names in the sqlite_master
    cur.execute(""" SELECT count(name) FROM sqlite_master
    WHERE type='table'
    AND name= ?;
    """, (table_name,))
    count_of_tables = cur.fetchone()[0]
    con.commit()
    if count_of_tables == 1:
        return True
    else:
        return False

def create_student_table():
    """creates a student table"""
    if check_table_exist("student"):
        print("Table exists.")
    else:
        cur.execute("""CREATE TABLE student
        (
        forename text,
        surname text,
        email text
        )
        """)
        con.commit()

def menu_options():
    """menu options"""
    while True:
        print("""
        1. Insert a student record
        2. View all student records
        3. View one student record
        4. Delete one student record
        5. Update one student record
        6. Exit
        """)
        menu_choice = input("Please enter option between 1 and 6: ")
        menu_options = ["1", "2", "3", "4", "5", "6"]
        while menu_choice not in menu_options:
            menu_choice = input("Error! You must choose an option between 1 and 6: ")
        if menu_choice == "1":
            insert_student_record()
        elif menu_choice == "2":
            get_student_records()
        elif menu_choice == "3":
            get_one_student_record()
        elif menu_choice == "4":
            delete_one_student_record()
        elif menu_choice == "5":
            update_one_student_record()
        else:
            print("Good bye")
            con.close()
            exit()
        continue_choice = input("Would you like to exit (Y/N): ").upper()
        if continue_choice == "Y":
            break
    print("Good bye")
    con.close()
    exit()

def insert_student_record():
    """collects data entered by user and sends to insert_student_data function"""
    forename = input("Please enter forename: ")
    surname = input("Please enter surname: ")
    email = input("Please enter email: ")
    # send values as args to insert_student_data()
    insert_student_data(forename, surname, email)
    return

def insert_student_data(forename: str, surname: str, email: str):
    """accepts student data as args and inserts into student table"""
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES (?, ?, ?)", (forename, surname, email))
    con.commit()
    return

def get_student_records():
    """output all student records"""
    cur = con.cursor()
    print("{:<2} {:<12} {:<12} {:<10}".format("ID", "Forename", "Surname", "Email"))
    for row in cur.execute("SELECT rowid, * FROM student"):
        print("{:<2} {:<12} {:<12} {:<10}".format(row[0], row[1], row[2], row[3]))
    return

def get_one_student_record():
    """output one student record"""
    cur = con.cursor()
    student_id = input("Enter the ID of student: ")
    print("{:<2} {:<12} {:<12} {:<10}".format("ID", "Forename", "Surname", "Email"))
    for row in cur.execute("SELECT rowid, * FROM student WHERE rowid=?", (student_id,)):
        print("{:<2} {:<12} {:<12} {:<10}".format(row[0], row[1], row[2], row[3]))
    return

def delete_one_student_record():
    """delete one student from database"""
    cur = con.cursor()
    get_student_records()  # shows all records before delete process
    student_id = input("Enter student to delete: ")
    cur.execute("DELETE from student WHERE rowid=?", (student_id,))
    con.commit()
    get_student_records()  # shows all records after delete process

def update_one_student_record():
    """allows a student record to be altered"""
    get_student_records()  # shows all records before update
    student_id = input("Enter student id for update: ")
    u_forename = input("Enter updated forename: ")
    u_surname = input("Enter updated surname: ")
    u_email = input("Enter updated email: ")
    cur.execute("""UPDATE student
    SET forename = ?, surname = ?, email = ?
    WHERE rowid = ?""", (u_forename, u_surname, u_email, student_id))
    get_student_records()  # shows all records after update

create_student_table()
menu_options()