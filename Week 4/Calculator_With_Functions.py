import os
import time
def Menu():
    print("CALCULATOR:")
    print("1)ADDITION\n2)SUBTRACTION\n3)MULTIPLICATION\n4)DIVISION\n5)EXPONENTIATION\n6)MODULUS")
    choice = input("INPUT OPERATION CHOICE: ")
    if choice == "1":
        inputs()
        Addition()
    elif choice == "2":
        inputs()
        Subtraction()
    elif choice == "3":
        inputs()
        Multiplication()
    elif choice == "4":
        inputs()
        Division()
    elif choice == "5":
        inputs()
        Exponentiation()
    elif choice == "6":
        inputs()
        Modulus()
    else:
        print("INVALID OPTION, TRY AGAIN")
        time.sleep(2)
        os.system('cls')
        Menu()

def inputs():
    global num1, num2
    try:
        num1 = float(input("INPUT FIRST NUMBER: "))
        num2 = float(input("INPUT SECOND NUMBER: "))
        return
    except ValueError:
        print("INVALID OPTIONS RESETTING PROGRAM")
        time.sleep(2)
        os.system('cls')
        Menu()

def Addition():
    sum = num1 + num2
    print(num1,"+",num2 ,"=", sum)

def Subtraction():
    total = num1 - num2
    print(num1, "-", num2 ,"=", total)

def Multiplication():
    product = num1 * num2
    print(num1, "X", num2, "=", product)

def Division():
    result = num1 / num2
    print(num1, "/", num2, "=", result)

def Exponentiation():
    expo = num1 ** num2
    print(num1, "to the power of", num2, "=", expo)

def Modulus():
    mod = num1 % num2
    print("Modulus of", num1, "and", num2, "is", mod)

Menu()