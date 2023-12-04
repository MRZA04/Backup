import sqlite3
import bcrypt
import getpass

con = sqlite3.connect("Timetables.db")
cur = con.cursor()

def create_user_tables():
    """CREATE TABLE TO STORE ACCOUNTS"""
    cur.execute("""CREATE TABLE IF NOT EXISTS user
                (
                        user_email TEXT PRIMARY KEY,
                        user_password   TEXT NOT NULL,
                        user_role   TEXT NOT NULL
                )
                """)
    con.commit()
    return


def create_user_account():
    """Get details and insert record in database"""
    while True:
        user_email      = input ("ENTER USER'S EMAIL: "
                                 ).strip().lower()
        
        hidden_password = getpass.getpass("ENTER USER'S PASSWORD: ")
        plain_password  = hidden_password.strip().encode('utf-8')
        user_password   = hash_password(plain_password)
        
        role_choice     = input ("IS USER ADMIN? [Y], PRESS ENTER FOR DEFAULT: "
                                 ).strip().upper()
        
        if role_choice == "Y":
            user_role = "admin"
        else:
            user_role = "default"
            
        insert_user_account(user_email, user_password, user_role)
        
        print(f"THE FOLLOWING DETAILS HAVE BEEN ENTERED: ",
              f"\nuser_email    ={user_email}",
              f"\nuser_password ={user_password}",
              f"\nuser_role     = {user_role}")
        add_another = input ("WOULD YOU LIKE TO ADD ANOTHJER [Y/N]: ").strip().upper()
        while add_another not in ["Y","N"]:
            add_another = input("INVALID OPTION, CHOOSE [Y/N]: ").strip().upper()
        
        if add_another == "N":
            
            break
    menu()
    return


def hash_password(plain_password:str):
    """HASH AND RETURN USER_PASSWORD"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(plain_password, salt)
    return hashed_password


def insert_user_account(user_email:str, user_password:str, user_role:str):
    """ACCEPTS USER DETAILS AND STORES IN SQLITE DB TABLE"""
    cur.execute("INSERT INTO user VALUES (?, ?, ?)" ,
                    (
                        user_email,
                        user_password,
                        user_role
                    )
                )
    con.commit()
    
    
def check_password():
    """FUNCTION USES BCRYPT TO CHECK IF THE USER IS IN THE DATABASE WITH MATCHING PASSWORD"""
    user_email          = input("ENTER EMAIL ADDRESS FOR USER:l ").strip().lower()
    
    password_check = input(f"ENTER PASSWORD FOR USER <{user_email}>: ").strip().encode('utf-8')
    
    cur.execute(""" SELECT user_password, user_role FROM user
                    WHERE user_email = ?""", (user_email,))
    result = cur.fetchall()
    print(result)
    
    fetched_password    = result[0][0]
    fetched_role        = result[0][1]
    
    if bcrypt.checkpw(password_check, fetched_password):
        print(f"MATCH FOUND with <{fetched_role.upper()}> ROLE")
    else:
        print("NO MATCH FOUND, INCORRECT EMAIL OR PASSWORD")
    menu()
    return

def menu():
    """PROVIDES MENU OPTIONS AND DIRECTS USER TO RELELVANT FUNCTION"""
    print("1) ADD RECORD \n2) CHECK RECORDS")
    choice = input("SELECT FUNCTION: ").strip()
    while choice not in ["1", "2"]:
        choice = input("ERROR, INCORRECT OPTION TRY AGAIN: ").strip()
    if choice == "1":
        create_user_account()
    else:
        check_password()
    return
    
create_user_tables()
menu()