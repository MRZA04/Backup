import os
import time
import math
def Menu():
    print("WELCOME TO THE SHAPE CALCULATOR\n(google does the same thing as this program and if you are genuinly using this instead of google I suggest you get psychiatric help. or ask god to give you new brain whichever comes first :)\nDO YOU WANT TO CONTINUE (Y/N): ")
    option = input().lower().strip()
    if option == "y":
        print("GREAT, LOADING PROGRAM")
        time.sleep(2)
        os.system('cls')
        MainMenu()
    elif option == "n":
        print("EXITING THE PROGRAM")
        time.sleep(1)
        quit()
    else:
        print("SORRY THAT IS NOT A VALID CHOICE, TRY AGAIN")
        time.sleep(1)
        os.system('cls')
        Menu()

def MainMenu():
    print("PLEASE SELECT YOUR CHOSEN SHAPE\n1) SQUARE/RECTANGLE\n2) TRIANGLE\n3) CIRCLE\n4) PARALLELOGRAM\n5) TRAPEZOID ")
    Shape = input()
    if Shape == "1":
        os.system('cls')
        FourSides()
    elif Shape == "2":
        Triangle()
    elif Shape == "3":
        Circle()
    elif Shape == "4":
        Parallelogram()
    elif Shape == "5":
        Trapezoid()
    else:
        print("SORRY THAT IS NOT A VALID CHOICE, TRY AGAIN")
        time.sleep(2)
        os.system('cls')
        MainMenu()

def FourSides():
    try:
        Base = float(input("ENTER BASE: "))
        Height = float(input("ENTER HEIGHT: "))
    except ValueError:
        print("INVALID NUMBER, TRY AGAIN")
        time.sleep(2)
        os.system('cls')
        FourSides()
    else:
        Area = Base * Height
        if Base == Height:
            print("YOUR SHAPE IS A SQUARE, THE AREA IS", Area)
        else:
            print("YOUR SHAPE IS A RECTANGLE, THE AREA IS", Area)
        Repeat()

def Triangle():
    Base = float(input("ENTER BASE: "))
    if Base <= 0:
        print("INVALID NUMBER, TRY AGAIN")
        time.sleep(2)
        os.system('cls')
        Triangle()
    Height = float(input("ENTER HEIGHT: "))
    if Height <= 0:
        print("INVALID NUMBER, TRY AGAIN")
        time.sleep(2)
        os.system('cls')
        Triangle()
    Area = (Base * Height) / 2
    print("THE AREA OF YOUR TRIANGLE IS", Area)
    Repeat()

def Circle():
    Radius = float(input("ENTER THE RADIUS OF YOUR CIRCLE: "))
    if Radius <= 0:
        print("INVALID OPTION, TRY AGAIN")
        time.sleep(2)
        os.system('cls')
        Circle()
    Area = math.pi * (Radius ** 2)
    print("THE AREA OF YOUR CIRCLE IS ", Area)
    Repeat()

def Parallelogram():
    Base = float(input("ENTER BASE: "))
    if Base <= 0:
        print("INVALID NUMBER, TRY AGAIN")
        time.sleep(2)
        os.system('cls')
        Parallelogram()
    Height = float(input("ENTER HEIGHT: "))
    if Height <= 0:
        print("INVALID NUMBER, TRY AGAIN")
        time.sleep(2)
        os.system('cls')
        Parallelogram()
    Area = Base * Height
    print("THE AREA OF YOUR PARALLELOGRAM IS ", Area)
    Repeat()

def Trapezoid():
    Base1 = float(input("ENTER BASE 1 OF YOUR TRAPEZOID: "))
    if Base1 <= 0:
        print("INVALID NUMBER, TRY AGAIN")
        time.sleep(2)
        os.system('cls')
        Trapezoid()
    Base2 = float(input("ENTER BASE 2 OF YOUR TRAPEZOID: "))
    if Base2 <= 0:
        print("INVALID NUMBER, TRY AGAIN")
        time.sleep(2)
        os.system('cls')
        Trapezoid()
    Height = float(input("ENTER THE HEIGHT OF YOUR TRAPEZOID: "))
    if Height <= 0:
        print("INVALID NUMBER, TRY AGAIN")
        time.sleep(2)
        os.system('cls')
        Parallelogram()
    Area = ((Base1 + Base2) / 2) * Height
    print("THE AREA OF YOUR TRAPEZOID IS ", Area)
    Repeat()  
    
def Repeat():
    Repeat = input("DO YOU WANT TO CONTINUE TO ANOTHER SHAPE: Y/N").lower().strip()
    if Repeat == "y":
        print("TAKING YOU BACK TO MAIN MENU")
        time.sleep(2)
        os.system('cls')
        MainMenu()
    elif Repeat == "n":
        quit()
    else:
        print("INVALID OPTION, TRY AGAIN")
        time.sleep(2)
        os.system('cls')
        Repeat()

Menu()