import sqlite3

def welcome():
    print("Welcome to the Patient Management System.")
    return input("Do you want to continue? (Y to continue/anything else to exit) ").upper() == "Y"

def create_table():
    with sqlite3.connect('patients.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                            patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            patient_fname VARCHAR(30),
                            patient_sname VARCHAR(30),
                            city TEXT,
                            patient_DOB TEXT,
                            Tel_no TEXT,
                            email TEXT)''')
    print("Table created successfully.")

def insert_patient():
    with sqlite3.connect('patients.db') as conn:
        cursor = conn.cursor()

        while True:
            patient_fname = input("Enter patient's first name: ")
            patient_sname = input("Enter patient's surname: ")
            city = input("Enter patient's city: ")
            patient_DOB = input("Enter patient's date of birth: ")
            Tel_no = input("Enter patient's telephone number: ")
            email = input("Enter patient's email: ")

            cursor.execute('''INSERT INTO patients 
                              (patient_fname, patient_sname, city, patient_DOB, Tel_no, email) 
                              VALUES (?, ?, ?, ?, ?, ?)''', 
                              (patient_fname, patient_sname, city, patient_DOB, Tel_no, email))

            if input("Do you want to enter another patient? (Y to continue/anything else to exit) ").upper() != "Y":
                break
    print("Patient inserted successfully.")

def retrieve_patients():
    with sqlite3.connect('patients.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM patients')
        for row in cursor.fetchall():
            print(row)

def delete_patient():
    with sqlite3.connect('patients.db') as conn:
        cursor = conn.cursor()
        patient_fname = input("Enter the first name of the patient to delete: ")
        cursor.execute('DELETE FROM patients WHERE patient_fname = ?', (patient_fname,))
    print("Patient deleted successfully.")

def main_menu():
    print("\nMain Menu")
    print("1. Create Table")
    print("2. Insert Patient")
    print("3. Retrieve Patients")
    print("4. Delete Patient")
    print("5. Exit")
    return input("Enter your choice (1-5): ")

def main():
    if welcome():
        while True:
            choice = main_menu()
            if choice == '1':
                create_table()
            elif choice == '2':
                insert_patient()
            elif choice == '3':
                retrieve_patients()
            elif choice == '4':
                delete_patient()
            elif choice == '5':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice, please try again.")
    else:
        print("Exiting the program.")

if __name__ == "__main__":
    main()
